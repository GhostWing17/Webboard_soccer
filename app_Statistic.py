import pandas as pd
import numpy as np
import statsmodels as sm
import seaborn as sb
import streamlit as st
import matplotlib.pyplot as plt
from scipy.stats import normaltest
from warnings import simplefilter
from sklearn.preprocessing import MaxAbsScaler,LabelEncoder, RobustScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import mutual_info_classif, chi2, f_classif
import os
from mplsoccer import Pitch, VerticalPitch, PyPizza, add_image, FontManager
from PIL import Image
import bar_chart_race as bcr


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


def run_Statistic_app() :
    
    st.subheader('Scoring FOUR goals in ONE Premier League match!')
    
    
    df = pd.read_csv('data/EPL Standings 2000-2022.csv')
    table = pd.read_csv('data/points_table.csv')
    df2 = pd.read_csv('data/all_match_results.csv')


    st.subheader('년도별 프리미어리그 클럽 순위 확인')

    with st.expander('데이터 프레임 확인하기') :
        st.dataframe(df2)
    
    st.subheader('클럽 통계 데이터')
    st.dataframe( df.describe() )
    
    column_list = df.columns
    selected_columns = st.multiselect('살펴보실 컬럼을 선택해주세요.', column_list)
    X = df[selected_columns]
    st.dataframe(X)

    