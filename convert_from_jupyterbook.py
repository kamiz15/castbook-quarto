#!/usr/bin/env python3
"""Convert the CASTbook (Jupyter Book / MyST) into a Quarto book project.

Reads SRC, writes a fresh DST (originals untouched). Transforms the MyST
directives actually used in this book: {figure}, admonitions, {sidebar},
{toggle}, dropdown-code admonitions, and the {numref}/{eq}/{ref} roles.
"""
import re, shutil
from pathlib import Path

SRC = Path(r"C:\Users\User\Downloads\CASTbook-main\CASTbook-main")
DST = Path(r"C:\Users\User\Downloads\CASTbook-main\castbook-quarto")

# admonition directive -> quarto callout class
CALLOUT = {
    "note": "note", "tip": "tip", "hint": "tip", "seealso": "note",
    "important": "important", "warning": "warning", "caution": "caution",
    "attention": "important", "error": "important", "danger": "important",
}


def esc(s):  # for title="..." attributes
    return s.replace('"', "'").strip()


def slug(s):  # valid pandoc/quarto id: lowercase, keep [a-z0-9_-]
    return re.sub(r'[^a-z0-9_-]+', '-', s.strip().lower()).strip('-')


def convert_figures(text):
    # closing ``` may sit directly after the option block (empty caption)
    pat = re.compile(
        r'^```\{figure\}[ \t]*(?P<path>\S+)[ \t]*\n'
        r'---\n(?P<opts>.*?)\n---\n'
        r'(?P<cap>.*?)```[ \t]*$',
        re.MULTILINE | re.DOTALL,
    )

    def repl(m):
        opts = {}
        for line in m.group("opts").splitlines():
            if ":" in line:
                k, _, v = line.partition(":")
                opts[k.strip()] = v.strip()
        cap = " ".join(l.strip() for l in m.group("cap").splitlines() if l.strip())
        attrs = []
        if opts.get("name"):
            attrs.append(f'#fig-{slug(opts["name"])}')
        if opts.get("align"):
            attrs.append(f'fig-align="{opts["align"]}"')
        w = opts.get("width") or opts.get("scale")  # scale%: approximated as width
        if w:
            attrs.append(f'width="{w}"')
        a = ("{" + " ".join(attrs) + "}") if attrs else ""   # no space before {
        return f'![{cap}]({m.group("path")}){a}'

    return pat.sub(repl, text)


def convert_dropdown_code(text):
    # {admonition} TITLE / :class: dropdown  wrapping a ```python block -> collapse callout
    pat = re.compile(
        r'^```\{(?:admonition|toggle)\}[ \t]*(?P<title>[^\n]*)\n'
        r':class:[ \t]*dropdown[ \t]*\n\n'
        r'```(?P<lang>\w*)\n(?P<code>.*?)\n```[ \t]*$',
        re.MULTILINE | re.DOTALL,
    )

    def repl(m):
        t = esc(m.group("title")) or "Show code"
        return (f'::: {{.callout-note collapse="true" title="{t}"}}\n'
                f'```{m.group("lang")}\n{m.group("code")}\n```\n:::')

    return pat.sub(repl, text)


def convert_directives(lines):
    """Line-stack pass: opens/closes for the remaining (code-free) directives.

    After convert_dropdown_code, no directive block contains a nested code
    fence, so a bare ``` unambiguously closes whatever the stack top is.
    """
    out, stack, i = [], [], 0
    open_dir = re.compile(r'^```\{(\w+)\}[ \t]*(.*)$')
    fence = re.compile(r'^```(\S*)[ \t]*$')
    while i < len(lines):
        line = lines[i]
        m = open_dir.match(line)
        if m:
            kind, arg = m.group(1), m.group(2).strip()
            # a following ":class: X" line refines the type
            klass = ""
            if i + 1 < len(lines) and lines[i + 1].strip().startswith(":class:"):
                klass = lines[i + 1].split(":", 2)[-1].strip()
                i += 1  # consume it
            if kind == "figure":            # leftover malformed figure: keep visible
                out.append(line); stack.append("dir"); i += 1; continue
            if kind == "sidebar":
                out.append("::: {.column-margin}")
                if arg:
                    out.append(f"**{arg}**\n")
                stack.append("dir"); i += 1; continue
            if kind == "toggle":
                out.append('::: {.callout-note collapse="true"}')
                stack.append("dir"); i += 1; continue
            if kind == "admonition":
                cc = CALLOUT.get(klass, "note")
                collapse = ' collapse="true"' if klass == "dropdown" else ""
                out.append(f'::: {{.callout-{cc}{collapse} title="{esc(arg)}"}}')
                stack.append("dir"); i += 1; continue
            if kind in CALLOUT:
                out.append(f'::: {{.callout-{CALLOUT[kind]}}}')
                stack.append("dir"); i += 1; continue
            # unknown directive: leave as-is but track fence
            out.append(line); stack.append("dir"); i += 1; continue
        f = fence.match(line)
        if f:
            info = f.group(1)
            if info:                         # ```lang  -> code open
                out.append(line); stack.append("code")
            else:                            # bare ``` -> close top (or open code)
                if stack and stack[-1] == "dir":
                    stack.pop(); out.append(":::")
                elif stack and stack[-1] == "code":
                    stack.pop(); out.append("```")
                else:
                    stack.append("code"); out.append("```")
            i += 1; continue
        out.append(line); i += 1
    return out


def convert_roles(text):
    # normalize a malformed double-backtick in the source: {ref}``x` -> {ref}`x`
    text = text.replace('{ref}``', '{ref}`').replace('{numref}``', '{numref}`')
    # equation label:  $$(label)  ->  $$ {#eq-label}
    text = re.sub(r'\$\$\((\w+)\)', lambda m: '$$ {#eq-' + slug(m.group(1)) + '}', text)
    # {numref}`Text<label>` / {numref}`label`
    text = re.sub(r'\{numref\}`([^`<]+)<([^>`]+)>`', lambda m: f'[{m.group(1)}](#fig-{slug(m.group(2))})', text)
    text = re.sub(r'\{numref\}`([^`<]+)`', lambda m: f'@fig-{slug(m.group(1))}', text)
    # {eq}`label`
    text = re.sub(r'\{eq\}`([^`]+)`', lambda m: f'@eq-{slug(m.group(1))}', text)
    # {ref}`figname_f2`  (bare ref that actually targets a figure, by naming convention)
    text = re.sub(r'\{ref\}`([A-Za-z0-9_]+_f\d+[a-z]?)`', lambda m: f'@fig-{slug(m.group(1))}', text)
    # {ref}`Text<target>` / {ref}`target`
    text = re.sub(r'\{ref\}`([^`<]+)<([^>`]+)>`', r'[\1](#\2)', text)
    text = re.sub(r'\{ref\}`([^`<]+)`', lambda m: f'[{m.group(1).strip()}](#{m.group(1).strip()})', text)
    # target anchor "(label)=" on its own line before a heading -> {#label} on heading
    text = re.sub(r'^\((\w+)\)=[ \t]*\n(#{1,6} .*?)[ \t]*#*[ \t]*$',
                  r'\2 {#\1}', text, flags=re.MULTILINE)
    # internal links  foo.md -> foo.qmd
    text = re.sub(r'(\]\([^)]+?)\.md([)#])', r'\1.qmd\2', text)
    return text


def convert_md(text):
    text = text.replace("\r\n", "\n")
    text = convert_dropdown_code(text)
    text = convert_figures(text)
    text = "\n".join(convert_directives(text.split("\n")))
    text = convert_roles(text)
    return text


def build_tree():
    # best-effort clear existing contents (the top dir may be locked by an
    # indexer/OneDrive on Windows, but its children can still be replaced)
    if DST.exists():
        for child in DST.iterdir():
            try:
                shutil.rmtree(child) if child.is_dir() else child.unlink()
            except OSError:
                pass
    def ignore(d, names):
        skip = {".git", "_build", "__pycache__"}
        return [n for n in names if n in skip or n == ".ipynb_checkpoints"]
    shutil.copytree(SRC, DST, ignore=ignore, dirs_exist_ok=True)
    # drop jupyter-book config files we replace
    for f in ["_toc.yml", "_config.yml", "conf.py", "requirements.txt"]:
        p = DST / f
        if p.exists():
            p.unlink()


def convert_all():
    leftovers = []
    for md in list(DST.rglob("*.md")):
        text = convert_md(md.read_text(encoding="utf-8", errors="replace"))
        qmd = md.with_suffix(".qmd")
        qmd.write_text(text, encoding="utf-8")
        md.unlink()
        rel = qmd.relative_to(DST)
        for bad in (r'```\{', r'\{numref\}', r'\{eq\}', r'\{ref\}', r'\{figure\}'):
            for mm in re.finditer(bad, text):
                ln = text[:mm.start()].count("\n") + 1
                leftovers.append(f"{rel}:{ln}  {bad}")
                break
    return leftovers


def dedupe_fig_ids():
    """The source reuses figure `name:` values -> duplicate #fig- ids, which
    Quarto rejects. Suffix later definitions (-2, -3). References are left
    pointing at the first (original) instance."""
    seen, dupes = {}, 0
    for qmd in sorted(DST.rglob("*.qmd")):
        text = qmd.read_text(encoding="utf-8")
        def repl(m):
            nonlocal dupes
            fid = m.group(1)
            seen[fid] = seen.get(fid, 0) + 1
            if seen[fid] == 1:
                return m.group(0)
            dupes += 1
            return "{#fig-" + fid + f"-{seen[fid]}"
        text = re.sub(r'\{#fig-([a-z0-9_-]+)', repl, text)
        qmd.write_text(text, encoding="utf-8")
    return dupes


# ---- intro.md is the book landing page -> index.qmd ----
def make_index():
    intro = DST / "intro.qmd"
    if intro.exists():
        intro.rename(DST / "index.qmd")


QUARTO_YML = '''\
project:
  type: book
  output-dir: _book

book:
  title: "CAST - A site assessment tool"
  author: "P. K. Yadav, S. Birla, V. Baliga, A. Köhler, K. Aryal, I. Wani, and others"
  favicon: images/logo/icon1.png
  search: true
  repo-url: https://github.com/prabhasyadav/CASTbook
  repo-actions: [issue]
  sidebar:
    logo: images/logo/icon1.png
  page-footer:
    center: "All content licensed under CC BY-SA 4.0 unless otherwise specified."
  chapters:
    - index.qmd
    - part: "Quick online usage and offline installation"
      chapters:
        - contents/online/online_usage.qmd
        - contents/online/login.qmd
        - contents/online/quick_example.qmd
        - contents/offline/offline_installation.qmd
        - contents/offline/quick_example.qmd
        - contents/offline/updating.qmd
    - part: "Using CAST toolboxes"
      chapters:
        - contents/toolbox/database/database.qmd
        - contents/toolbox/an_model/an_model.qmd
        - contents/toolbox/an_model/liedl2005.qmd
        - contents/toolbox/an_model/chu2005.qmd
        - contents/toolbox/an_model/ham2004.qmd
        - contents/toolbox/an_model/liedl2011.qmd
        - contents/toolbox/an_model/bioscreen.qmd
        - contents/toolbox/em_model/em_model.qmd
        - contents/toolbox/em_model/birla2020.qmd
        - contents/toolbox/em_model/mg2006.qmd
        - contents/toolbox/num_model.qmd
        - contents/toolbox/mod_sel.qmd
    - part: "Development"
      chapters:
        - contents/develop/code_structure.qmd
        - contents/develop/code_libraries.qmd
        - contents/develop/code_develop.qmd
    - part: "Reference"
      chapters:
        - contents/ref/cite.qmd
        - contents/ref/version.qmd

format:
  html:
    theme: cosmo
    css: _static/custom.css
    number-sections: true
    toc: true
    fig-align: center
  pdf:
    documentclass: scrreport
    number-sections: true

crossref:
  fig-title: "Figure"
  fig-prefix: "Figure"
'''


def write_meta():
    (DST / "_quarto.yml").write_text(QUARTO_YML, encoding="utf-8")
    (DST / ".gitignore").write_text("/_book/\n/.quarto/\n", encoding="utf-8")


if __name__ == "__main__":
    build_tree()
    leftovers = convert_all()
    dupes = dedupe_fig_ids()
    make_index()
    write_meta()
    print(f"Wrote Quarto project to: {DST}")
    print(f"qmd files: {len(list(DST.rglob('*.qmd')))}")
    print(f"deduped figure ids: {dupes}")
    if leftovers:
        print("\nFILES NEEDING A MANUAL LOOK (unconverted MyST remnants):")
        for l in sorted(set(leftovers)):
            print("  " + l)
    else:
        print("No unconverted MyST directives/roles remain.")
