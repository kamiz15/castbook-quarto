# CASTbook → Quarto — conversion notes

The Jupyter Book (MyST) sources were mechanically converted to a Quarto **book**
project. Originals are untouched in `../CASTbook-main`.

## Build / preview

```bash
# one-time: install Quarto from https://quarto.org  (then, for PDF only:)
quarto install tinytex

cd castbook-quarto
quarto preview        # live HTML site with search + sidebar nav
quarto render         # build _book/ (HTML; add `--to pdf` for the handbook)
```

## What was converted automatically

| MyST source | Quarto output |
|---|---|
| ` ```{figure} ` blocks (~90) | `![caption](path){#fig-… fig-align=… width=…}` |
| `{note}/{tip}/{warning}/{caution}` | `::: {.callout-…}` |
| `{attention}/{error}` | `::: {.callout-important}` |
| `{admonition} Title` + `:class: dropdown` + code | collapsible `::: {.callout-note collapse="true"}` |
| `{sidebar}` | `::: {.column-margin}` |
| `` {numref}`fig` `` / `` {eq}`e` `` | `@fig-…` / `@eq-…` |
| `` {ref}`Text<tgt>` `` | `[Text](#tgt)` |
| `$$…$$(label)` | `$$…$$ {#eq-label}` |
| `(label)=` anchors, `.md` links | `{#label}` on heading, `.qmd` links |
| `_toc.yml` + `_config.yml` | `_quarto.yml` (book, parts → chapters) |

## Deliberate approximations (ponytail: fix only if it bites)

- **`scale:` → `width:`** — MyST `scale` isn't a true width; treated as `width="N%"`.
  Tune per-figure if any image looks off.
- **Duplicate figure IDs** — the *source* reuses `name:` values (two `cc`, two
  `An_mod`, etc.). 7 later definitions were suffixed `-2`; cross-references still
  point at the **first** instance (matching the source's own ambiguity).
- **Nested sections flattened** — Jupyter-Book `sections:` became sibling chapters
  under the same part (Quarto books don't nest chapters). Reorder in `_quarto.yml`
  if you want a different grouping.
- **Dropped dead `_toc` entry** `contents/toolbox/bscreen/bioscreen` (no such file
  in the source). The real BIOSCREEN page is `an_model/bioscreen.qmd`.
- **Orphan pages** — the `contents/**/CAST/*.qmd` snippets and a stray
  `toolbox/database.qmd` weren't in the original TOC; left out of the nav.

## Still worth a human pass

- `an_model/bioscreen.qmd` L70: source typo `{eq}` `` `eqbio2007` `` `)` renders a stray `)`.
- Confirm the two collapsible code callouts in `bioscreen.qmd` / `liedl2011.qmd`.
- Swap `theme: cosmo` in `_quarto.yml` for your brand once you pick one.
