import streamlit as st 
import numpy as np
import pandas as pd
import altair as alt 
from sklearn.model_selection import train_test_split
import scipy as sp
import seaborn as sns
from matplotlib import pyplot as plt
from collections import Counter
from itertools import chain
import datetime as dt
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon



# ===========================================
# Datasets
# ===========================================

# --------------
# Read
# --------------

cases_malaysia = pd.read_csv('covid19-public/epidemic/cases_malaysia.csv')
cases_state = pd.read_csv('covid19-public/epidemic/cases_state.csv')
clusters = pd.read_csv('covid19-public/epidemic/clusters.csv')
deaths_malaysia = pd.read_csv('covid19-public/epidemic/deaths_malaysia.csv')
deaths_state = pd.read_csv('covid19-public/epidemic/deaths_state.csv')
hospital = pd.read_csv('covid19-public/epidemic/hospital.csv')
icu = pd.read_csv('covid19-public/epidemic/icu.csv')
pkrc = pd.read_csv('covid19-public/epidemic/pkrc.csv')
tests_malaysia = pd.read_csv('covid19-public/epidemic/tests_malaysia.csv')
tests_state = pd.read_csv('covid19-public/epidemic/tests_state.csv')

population = pd.read_csv('covid19-public/static/population.csv')

# loading datasets
checkin_malaysia = pd.read_csv('covid19-public/mysejahtera/checkin_malaysia.csv')
checkin_malaysia_time = pd.read_csv('covid19-public/mysejahtera/checkin_malaysia_time.csv')
checkin_state = pd.read_csv('covid19-public/mysejahtera/checkin_state.csv')
trace_malaysia = pd.read_csv('covid19-public/mysejahtera/trace_malaysia.csv')

# load maps for schools
malaysia_map = gpd.read_file('random_dataset/mys_admbnda_adm1_unhcr_20210211.shp')
vax_school = pd.read_csv('covid19-public/vaccination/vax_school.csv')

# ---------------
# to dateTime
# ---------------
# change to date_time from object
cases_malaysia['date'] = pd.to_datetime(cases_malaysia['date'], errors='raise')
cases_state['date'] = pd.to_datetime(cases_state['date'], errors='raise')
clusters['date_announced'] = pd.to_datetime(clusters['date_announced'], errors='raise')
clusters['date_last_onset'] = pd.to_datetime(clusters['date_last_onset'], errors='raise')
deaths_malaysia['date'] = pd.to_datetime(deaths_malaysia['date'], errors='raise')
deaths_state['date'] = pd.to_datetime(deaths_state['date'], errors='raise')
hospital['date'] = pd.to_datetime(hospital['date'], errors='raise')
icu['date'] = pd.to_datetime(icu['date'], errors='raise')
pkrc['date'] = pd.to_datetime(pkrc['date'], errors='raise')
tests_malaysia['date'] = pd.to_datetime(tests_malaysia['date'], errors='raise')
tests_state['date'] = pd.to_datetime(tests_state['date'], errors='raise')


# basic data preparations

# change to date_time from object
checkin_malaysia['date'] = pd.to_datetime(checkin_malaysia['date'], errors='raise')
checkin_state['date'] = pd.to_datetime(checkin_state['date'], errors='raise')
trace_malaysia['date'] = pd.to_datetime(trace_malaysia['date'], errors='raise')
checkin_malaysia_time['date'] = pd.to_datetime(checkin_malaysia_time['date'], errors='raise')

# set index as date for timeseries indexing
checkin_malaysia.set_index('date', inplace=True)
checkin_state.set_index('date', inplace=True)
trace_malaysia.set_index('date', inplace=True)
checkin_malaysia_time.set_index('date', inplace=True)



# Registration
vaxreg_malaysia = pd.read_csv('citf-public/registration/vaxreg_malaysia.csv')
vaxreg_state = pd.read_csv('citf-public/registration/vaxreg_state.csv')

vaxreg_malaysia['date'] = pd.to_datetime(vaxreg_malaysia['date'], errors='raise')
vaxreg_state['date'] = pd.to_datetime(vaxreg_state['date'], errors='raise')

# vaccination 
vax_malaysia = pd.read_csv('citf-public/vaccination/vax_malaysia.csv')
vax_state = pd.read_csv('citf-public/vaccination/vax_state.csv')

vax_malaysia['date'] = pd.to_datetime(vax_malaysia['date'], errors='raise')
vax_state['date'] = pd.to_datetime(vax_state['date'], errors='raise')

# ------------------
# income cleaning
income = pd.read_csv('random_dataset/_202108260434240_mean-monthly-household-gross-income-by-state-malaysia.csv')
income.replace("n.a.", "0", inplace=True)
income.replace('N.Sembilan', 'Negeri Sembilan', inplace=True)
income.replace('P.Pinang', 'Pulau Pinang', inplace = True)
income.replace('W.P.KL', 'W.P. Kuala Lumpur', inplace=True)
income.replace('W.P.Labuan', 'W.P. Labuan', inplace=True)

# --------------------------
# Dataset cleaning and merging ends here

# ======================================
# Streamlit
# ======================================


st.title("Simple visualization of MOH COVID-19 and CITF datasets")
st.header("Malaysia")


import altair as alt

# st.header("Deaths")
# st.subheader('Our Exploratory Data Analysis')
# st.markdown('Our EDA will first cover the data for Malaysia, followed by the states in Malaysia')
# st.markdown('')

# cases_my = alt.Chart(covid[covid["Country"]==cty]).encode(
#     x="Date",
#     y="New cases",
#     tooltip=["Date","Country","New cases"]
# ).interactive()

st.subheader('Cases Malaysia')

cases_malaysia
cases_my = alt.Chart(cases_malaysia).encode(
    x="date",
    y="cases_new",
    tooltip=["date","cases_new"]
).interactive()

st.altair_chart(cases_my.mark_line(color='firebrick'))


# ------------------
# Deaths
# ------------------

st.subheader('Deaths Malaysia')

deaths_malaysia
deaths_my = alt.Chart(deaths_malaysia).encode(
    x="date",
    y="deaths_new",
    tooltip=["date","deaths_new"]
).interactive()

st.altair_chart(deaths_my.mark_line(color='firebrick'))

# ------------------
# Bed utilization 
# ------------------

st.subheader('Beds utilization Malaysia')


hospital_view = hospital.copy()
hospital_view = hospital_view.groupby('date', as_index=False).sum()
hospital_view
hospital_view['covid_bed_utilization'] = (((hospital_view['hosp_covid']) / hospital_view['beds_covid']) * 100).round(2)

beds_my = alt.Chart(hospital_view).encode(
    x="date",
    y="covid_bed_utilization",
    tooltip=["date","covid_bed_utilization"]
).interactive()

st.altair_chart(beds_my.mark_line(color='firebrick'))

# -------------------
# Daily fully vaccine
# -------------------

# vax_malaysia 
st.subheader('Daily fully vaccinated')
vax_my = alt.Chart(vax_malaysia).encode(
    x='date',
    y='daily_full',
    tooltip=['date', 'daily_full']
).interactive()

st.altair_chart(vax_my.mark_line(color='firebrick'))

# ---------------
# Dropbox
# ---------------

cty = st.selectbox("Select state",cases_state["state"][:16])


st.subheader('Cumulutive vaccine given by state')
vax_state_trim = vax_state.iloc[-16:]
vax_state_trim = vax_state_trim.sort_values('cumul_full', ascending=False)

# vax_state_all = latest.sort_values("Confirmed",ascending=False)[["Country","Confirmed"]].head()

# confirm.reset_index(inplace = True,drop = True)

bar1 = alt.Chart(vax_state_trim).mark_bar().encode(
    x="cumul_full",
    y=alt.Y("state",sort="-x"),
    color=alt.Color("state",legend=None),
    #facet='state:N',
    tooltip = "cumul_full"
).interactive()

st.altair_chart(bar1)

st.subheader('Cumulative Full Vaccination Doses Given in Malaysia')
rec=alt.Chart(vax_malaysia).mark_area(color="green").encode(
    x="date:T",
    y="cumul_full:Q",
    tooltip=["date","cumul_full"]
).interactive()

st.altair_chart(rec)

st.subheader('Percentage of vaccinated population by state')
## Calculate percentage
## df_Q3 = pd.merge(vax_state_trim[['state', 'cumul_partial', 'cumul_partial_child', 'cumul_full', 'cumul_full_child']], population[['state', 'pop', 'pop_12']], on='state')
df_vax_state_perc = pd.merge(vax_state_trim[['state', 'cumul_partial', 'cumul_partial_child', 'cumul_full', 'cumul_full_child']], population[['state', 'pop', 'pop_12']], on='state')

df_vax_state_perc['perc_vax_full'] = (df_vax_state_perc['cumul_full'] / df_vax_state_perc['pop'] * 100).round(2)
df_vax_state_perc['perc_vax_part'] = (df_vax_state_perc['cumul_partial'] / df_vax_state_perc['pop'] * 100).round(2)

df_vax_state_perc = df_vax_state_perc.sort_values('perc_vax_full', ascending=False).sort_values('perc_vax_full', ascending=False)

bar1 = alt.Chart(df_vax_state_perc).mark_bar().encode(
    x="perc_vax_full",
    y=alt.Y("state",sort="-x"),
    color=alt.Color("state",legend=None),
    tooltip = ['state', "perc_vax_full"]
).interactive()

st.altair_chart(bar1)

bar1 = alt.Chart(df_vax_state_perc).mark_bar().encode(
    x="perc_vax_part",
    y=alt.Y("state",sort="-x"),
    color=alt.Color("state",legend=None),
    tooltip = ['state', "perc_vax_full"]
).interactive()

st.altair_chart(bar1)