import streamlit as st 
import numpy as np
import pandas as pd
import altair as alt 
from sklearn.model_selection import train_test_split
from collections import Counter
from itertools import chain
from sklearn.tree import DecisionTreeClassifier 
from sklearn.tree import DecisionTreeRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import confusion_matrix
from math import sqrt
from PIL import Image
from sklearn.feature_selection import SelectKBest, chi2, f_regression, mutual_info_regression, RFECV
from sklearn.linear_model import LinearRegression