This jupyter notebook requires pdarima==1.8.0

1. Copy existing environment
conda create --clone base --name pmdarima_test

2. Revert statsmodels to version 0.11
	- Check package version using 
		pip show statsmodels
	- if package already installed
		pip uninstall statsmodels
		pip install statsmodels==0.11

3. Install cython
	pip install cython==0.29.18

4. pip install pmdarima==1.8.0
