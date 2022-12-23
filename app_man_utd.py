import pandas as pd
import numpy as np
import statsmodels as sm
import seaborn as sb
import streamlit as st
import matplotlib.pyplot as plt


df = pd.read_csv('data/EPL Standings 2000-2022.csv')
df2 = pd.read_csv('data/all_players_stats.csv')
table = pd.read_csv('data/points_table.csv')
allresult = pd.read_csv('data/all_match_results.csv')


def run_man_utd_app() :
    
    img_url = 'https://images6.alphacoders.com/969/thumb-1920-969527.jpg'
    st.image(img_url)
    
    
st.subheader('년도별 프리미어리그 클럽 순위 확인')
with st.expander('데이터 프레임 확인하기') :
    st.dataframe(df)
    
    st.subheader('클럽 통계 데이터')
    st.dataframe( df.describe() )