# dm-project

Welcome to our Data Mining Project. 

Link to our website: https://tds-3301-sample.herokuapp.com/ 

# Setting up the environment for Jupyter Notebook
This notebook requires that you have pdarima==1.8.0

If you do not have this package installed, we strongly recommend you to follow the following steps to install the package. 

## 1. Copy Existing Environment
conda create --clone base --name pmdarima_test

## 2. Revert statsmodels to version 0.11
Check your package for statsmodels using `pip show statsmodels`. If the version is the same, move to 3.
- If you have a different version of statsmodels, `pip uninstall statsmodels`, followed by `pip install statsmodels==0.11`.

# 3. Install cython
pip install cython==0.29.18

# 4. Install pmdarima
pip install pmdarima==0.18
