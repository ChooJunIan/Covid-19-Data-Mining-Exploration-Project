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


cases_state = pd.read_csv('cases_state.csv')
tests_state = pd.read_csv('tests_state.csv')
tests_malaysia = pd.read_csv('tests_malaysia.csv')
cases_malaysia = pd.read_csv('cases_malaysia.csv')
clusters = pd.read_csv('clusters.csv')
population = pd.read_csv('population.csv')
cases_malaysia['date'] = pd.to_datetime(cases_malaysia['date'], errors='raise')
tests_malaysia['date'] = pd.to_datetime(tests_malaysia['date'], errors='raise')
cases_state['date'] = pd.to_datetime(cases_state['date'], errors='raise')
tests_state['date'] = pd.to_datetime(tests_state['date'], errors='raise')
cases_malaysia.drop(cases_malaysia.columns[4:], axis=1, inplace=True)
cases_malaysia.drop(cases_malaysia[cases_malaysia['date'] > '2021-09-10'].index, inplace=True)
tests_malaysia.drop(tests_malaysia[tests_malaysia['date'] > '2021-09-10'].index, inplace=True)
cases_malaysia.set_index('date', inplace=True)
tests_malaysia.set_index('date', inplace=True) 
merged_malaysia = pd.merge(left=cases_malaysia, right=tests_malaysia, how='inner', 
                           left_index=True, right_index=True)

st.title("Good day to you, dear reader!")
st.header("These are the findings for our group assignment!")

st.header("Question 3 (i)")
st.subheader('Our Exploratory Data Analysis')
st.markdown('Our EDA will first cover the data for Malaysia, followed by the states in Malaysia')
st.markdown('')
