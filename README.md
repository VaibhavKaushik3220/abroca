## What is it?

"abroca" is a python package to provide basic functionality for computing and visualizing the Absolute Between-ROC Area (ABROCA).

## Install

The source code is currently hosted on [github](https://github.com/VaibhavKaushik3220/abroca) and Python package at [PyPi](https://pypi.org/project/abroca/)

```sh
# PyPI
pip install abroca
```

## Example

You can find the .ipynb file under example folder. It is a basic example which demonstrates the use of the `abroca` package to compute the ABROCA for a simple logistic regression classifier.

```sh
#Compute Abroca
slice = compute_abroca(df_test, pred_col = 'pred_proba' , label_col = 'returned',         
                       protected_attr_col = 'Gender', majority_protected_attr_val = 1,   
                       n_grid = 10000, plot_slices = True, file_name = 'slice_plot.png')
```
<img src="abroca/example/slice_plot.png" width="100%"/>

The plot is automatically saved to a file and is displayed on-screen. The link to download the data is given in the comments in the example file. Parameters are self explainatory through the example file. Parameter details below. 

* df - dataframe containing colnames matching pred_col, label_col and protected_attr_col
* pred_col - name of column containing predicted probabilities (string)
* label_col - name of column containing true labels (string)
* protected_attr_col - name of column containing protected attribute (should be binary) (string)
* majority_protected_attr_val name of 'majority' group with respect to protected attribute
* n_grid (optional) - number of grid points to use in approximation (numeric) (default of 10000 is more than adequate for most cases)
* plot_slices (optional) - if TRUE, ROC slice plots are generated and saved to file_name (boolean)
* lb (optional) - Lower limit of integration (use -numpy.inf for -infinity) Default is 0
* ub (optional) - Upper limit of integration (use -numpy.inf for -infinity) Default is 1
* limit (optional) - An upper bound on the number of subintervals used in the adaptive algorithm.Default is 1000
* file_name (optional) - File name (including directory) to save the slice plot generated

Reference Paper: 
Josh Gardner, Christopher Brooks, and Ryan Baker (2019). Evaluating the
Fairness of Predictive Student Models Through Slicing Analysis.
Proceedings of the 9th International Conference on Learning Analytics
and Knowledge (LAK19); March 4-8, 2019; Tempe, AZ, USA.
<https://doi.org/10.1145/3303772.3303791>

## Getting Help

If you encounter a clear bug, please file a minimal reproducible example on [github](https://github.com/VaibhavKaushik3220/abroca/issues), or contact the package maintainers directly (see the package documentation).
