# CAST Manual Authoring Conventions

This file defines the Quarto source conventions for sections, lists, and
figures. The book configuration in `_quarto.yml` controls page order.

## Sections and numbering

1. Every QMD file has exactly one level-one heading (`#`) as its page title.
2. Major toolbox titles use Arabic numerals, for example
   `# 1. Analytical Model Toolbox {.unnumbered}`.
3. Model pages use lower-case Roman numerals, for example
   `# i. Liedl et al. (2005) Model {.unnumbered}`.
4. Sections within a page use level-two headings (`##`).
5. A subdivision below a level-two section is an unnumbered bold-italic run-in
   heading, for example `***Single computing interface***`. Do not use headings
   below level two.
6. Do not type compiler-like hierarchical numbers such as `14.0.0.11` into
   headings.

The `.unnumbered` class prevents Quarto's automatic Arabic numbering from being
added on top of the deliberate Arabic/Roman title prefix.

## Lists

Use ordinary Markdown numbering for procedural steps:

```md
1. First step
2. Second step
```

Use an HTML ordered list when upper-case letters are required:

```html
<ol type="A">
  <li>First convention</li>
  <li>Second convention</li>
</ol>
```

Roman numerals identify model pages; they are not generated from a Markdown
list.

## Figure directories and names

1. Each page keeps its figures in its own directory under the nearest `images`
   directory, for example `images/liedl2005/`.
2. PNG is preferred. Use 300 DPI for print graphics when an original print
   source is available. For screenshots, retain the native resolution rather
   than artificially resampling an image to 300 DPI.
3. A figure filename contains its type, Arabic chapter number, Roman model
   number, and a two-digit sequence:
   - Major chapter: `fig1-01.png`
   - Model subsection: `fig1-i-01.png`
4. Quarto's cross-reference ID uses the same components but must begin with
   `fig-`, for example `fig-1-i-01`. It must be unique in the whole manual.
5. Every figure has a meaningful caption and is referenced with `@fig-...`.

Example:

```md
![Conceptual setup of the Liedl et al. (2005) model.](images/liedl2005/fig1-i-01.png){#fig-1-i-01 fig-align="center" width="40%"}

See @fig-1-i-01.
```

If a figure is inserted between established figures, use the next unused
sequence number instead of renumbering existing references merely to close a
gap.
