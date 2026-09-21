# Run PACS locally figure staging

Add future screenshots for the Run PACS locally chapter to this directory.

Reserved filenames:

- fig1-i-01.png
- fig1-i-02.png
- fig1-i-03.png
- fig1-i-04.png
- fig1-i-05.png
- fig1-i-06.png
- fig1-i-07.png
- fig1-i-08.png
- fig1-i-09.png

Use PNG where possible. Preserve the source resolution and target an effective
resolution of at least 300 DPI when a print-quality source is available.

When a screenshot is ready, replace its visible [SC] placeholder in
run_locally.qmd with a Quarto figure. For example:

~~~markdown
![Configuration file with required variable names visible.](images/run-locally/fig1-i-04.png){#fig-1-i-04 fig-align=center width=80%}
~~~

Use the filename form fig1-i-04.png and the cross-reference identifier form
fig-1-i-04. Increase the final two-digit sequence for additional figures in
the same chapter.
