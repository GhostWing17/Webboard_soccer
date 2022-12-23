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


def run_liverpool_app() :
    
    img_url = 'https://wallpaperaccess.com/full/1088660.jpg'
    st.image(img_url)
    img_url = 'https://m.media-amazon.com/images/M/MV5BZDc2MTE3ZmQtOWQwNi00ZjBiLWFmZTctNzQ3Y2JlNmZiMWFmXkEyXkFqcGdeQXVyOTU5Njc3ODI@._V1_.jpg'
    st.image(img_url)
    
    df = pd.read_csv('data/EPL Standings 2000-2022.csv')
    df2 = pd.read_csv('data/all_players_stats.csv')
    table = pd.read_csv('data/points_table.csv')
    allresult = pd.read_csv('data/all_match_results.csv')
    
    
    # 리버풀 선수
    players = st.radio(
    "21 - 22 시즌 리버풀 상위권 선수들",
    ('수비수', '미드필더', '공격수'))
    
    stats_manutd = df2[df2['Team'] == 'Liverpool']
    
    midfield = stats_manutd[stats_manutd['Position'].isin(['Midfielder','Midfielder/Forward',
                                                       'Defender/Midfielder', 
                                                       'Defender/Midfielder/Forward'])]
    
    offensive = stats_manutd[stats_manutd['Position'].isin(['Forward'])]
    
    if players == '수비수':
        
        defensive = stats_manutd[stats_manutd['Position'].isin(['Goalkeeper', 'Defender'])]
        st2 = defensive.sort_values(by='Apearances', ascending=False)
        st.dataframe(st2)
    
    
    elif players == '미드필더':
        
        st3 = midfield.sort_values(by='Apearances', ascending=False).iloc[:10, :]
        st.dataframe(st3)
        
    elif players == '공격수' :
        
        st4 = offensive.sort_values(by='Apearances', ascending=False).iloc[:10, :]
        st.dataframe(st4)
    
    else:
        st.write("아무것도 선택하지 않으셨습니다.")
    
    