---
output: github_document
title: "README"
---

<!-- README.md is generated from README.Rmd. Please edit that file -->

```{r setup, include = FALSE}
knitr::opts_chunk$set(
  collapse = TRUE,
  comment = "#>",
  fig.path = "man/figures/",
  out.width = "100%"
)
```
## What is it?

"abroca" is a python package to provide basic functionality for computing and visualizing the Absolute Between-ROC Area (ABROCA).

## Where to get it

The source code is currently hosted on GitHub at:
https://github.com/VaibhavKaushik3220/abroca
You can install the released version of abroca from [CRAN](https://CRAN.R-project.org) with:

```sh
# PyPI
pip install abroca
```


## Example

You can find the .ipynb file under example folder. It is a basic example which demonstrates the use of the `abroca` package to compute the ABROCA for a simple logistic regression classifier.

The link to download the data is given in the comments in the example file. Parameters are self explainatory through the example file.

The plot is automatically saved to a file instead of being displayed on-screen.

## Getting Help

If you encounter a clear bug, please file a minimal reproducible example on [github](https://github.com/VaibhavKaushik3220/abroca/issues), or contact the package maintainers directly (see the package documentation).
