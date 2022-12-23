import pandas as pd
import numpy as np
import statsmodels as sm
import seaborn as sb
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from scipy.stats import normaltest
from warnings import simplefilter
from matplotlib import rc
from matplotlib import font_manager
import platform

sb.set_style('darkgrid')
plt.rcParams['font.size'] = 14
plt.rcParams['figure.figsize'] = (36, 20)
plt.rcParams['figure.facecolor'] = '#00000000'


if platform.system() == 'Windows':
    rc('font', family='NanumGothic')
elif platform.system() == 'Darwin': # Mac
    rc('font', family='AppleGothic')
else: #linux
    rc('font', family='NanumGothic')

pd.options.plotting.backend
pd.set_option('max_colwidth', 600)
sb.set()
simplefilter('ignore')

# Set Matplotlib defaults
plt.style.use("seaborn-whitegrid")
plt.rc("figure", 
    autolayout=True, 
    figsize=(15, 5),
    frameon = True,
    edgecolor = 'black',
    titlesize = 20,
    titleweight = 'bold')
plt.rc(
    "axes",
    labelweight="bold",
    labelsize="large",
    titleweight="bold",
    titlesize=18,
    titlepad=12)
plt.rc(
    "legend",
    edgecolor = 'black',
    facecolor = 'white',
    fancybox  = True,
    fontsize  = 14,
    framealpha = 0.75,
    frameon = True,
    shadow = True,
    title_fontsize = 14)
plt.rc(
    "font",
    family = 'DejaVu Sans',
    weight = 'bold')

plot_params = dict(
    color="0.75",
    style=".-",
    markeredgecolor="0.25",
    markerfacecolor="0.25",
)



def run_total_app() :
    
    st.subheader('Scoring FOUR goals in ONE Premier League match!')
    
    
    df = pd.read_csv('data/EPL Standings 2000-2022.csv')
    table = pd.read_csv('data/points_table.csv')
    df2 = pd.read_csv('data/all_match_results.csv')

    
    st.subheader('클럽 통계 데이터')
    st.dataframe( df.describe() )
    
    
    st.subheader('21-22 시즌 프리미어리그 순위')   
    cl = ['Manchester City', 'Liverpool', 'Chelsea','Tottenham Hotspur']
    el = ['Arsenal']
    relegate = ['Burnley','Watford','Norwich City']
    cl_style = 'color:white; background-color:darkgreen;text-shadow: 3px 3px 3px black;'
    tott_style = 'color:white;background-color:darkorange;text-shadow: 3px 3px 3px black;'
    el_style = 'color:white;background-color:darkblue;text-shadow: 3px 3px 3px black;'
    rel_style = 'color:white;background-color:darkred;text-shadow: 3px 3px 3px black;'
    t1 = table.style.\
    applymap(lambda v:  cl_style if v in cl  else None)\
    .applymap(lambda v: tott_style  if v in ['Manchester United', 'West Ham United']  else None)\
    .applymap(lambda v: el_style  if v in el  else None)\
    .applymap(lambda v: rel_style  if v in relegate  else None)
    st1 = t1.set_caption('⚽ EPL Table Season 2021-2022 ⚽')
    st.dataframe(st1)
    

    with st.expander('리그 강등권 클럽 보기') :
        
        losers = (df[df.Pos >= 18])
        relegations = losers.Team.value_counts()
        fig2 = plt.figure(figsize=(12, 12))
        sb.barplot(x=relegations, y=relegations.index, palette = 'autumn')
        plt.title('Relegations between 2000-2022');
        plt.xlabel('Relegations');
        plt.ylabel('Team');
        st.pyplot(fig2)
    
    
    st.subheader('프리미어리그 21-22시즌 클럽 대진표 확인')
    with st.expander('클릭!') :
        st.dataframe(df2)
    
    
    st.subheader('프리미어리그 역대 우승 클럽 확인')
    winners = (df[df.Pos == 1])
    with st.expander('클릭!') :
        st.dataframe(winners)
        most_times_w = winners.Team.value_counts()
        fig1 = sb.catplot(y = 'Team', kind='count', data = winners, aspect = 2.5, order = most_times_w.index, palette = 'summer').set(title='2000-2022 Champion')
        st.pyplot(fig1)
    