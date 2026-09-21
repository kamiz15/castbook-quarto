# PACS manual (Quarto)

This repository contains the Quarto version of the PACS manual for the Preliminary Assessment of Contaminated Sites.

The manual documents PACS workflows, including local setup, site database use, analytical and empirical models, numerical models, and the AEM source designer.

## Preview locally

Install [Quarto](https://quarto.org/docs/get-started/) and run:

```bash
quarto preview
```

To render the full book:

```bash
quarto render
```

The rendered site is written to `_book/`, which is intentionally ignored by git.

## PACS application source

The PACS application code referenced by the local installation instructions is available at:

https://github.com/kamiz15/Groundwater-Contamination-Website