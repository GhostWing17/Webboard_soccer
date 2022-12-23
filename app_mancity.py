<<<<<<< HEAD
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


df = pd.read_csv('data/EPL Standings 2000-2022.csv')
df2 = pd.read_csv('data/all_players_stats.csv')
table = pd.read_csv('data/points_table.csv')
allresult = pd.read_csv('data/all_match_results.csv')


def run_mancity_app() :
    
    img_url = 'https://images3.alphacoders.com/969/thumb-1920-969547.jpg'
    st.image(img_url)
    img_url = 'https://cdnimg.vietnamplus.vn/t1200/Uploaded/mzdic/2021_05_13/man-city-premier-league-champions.jpg'
    st.image(img_url)
    
    
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
    

    
    
    # 맨시티 선수
    players = st.radio(
    "21 - 22 시즌 맨체스터 시티 상위권 선수들",
    ('수비수', '미드필더', '공격수'))
    
    stats_manutd = df2[df2['Team'] == 'Manchester City']
    
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
 
=======
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


df = pd.read_csv('data/EPL Standings 2000-2022.csv')
df2 = pd.read_csv('data/all_players_stats.csv')
table = pd.read_csv('data/points_table.csv')
allresult = pd.read_csv('data/all_match_results.csv')


def run_mancity_app() :
    
    img_url = 'https://images3.alphacoders.com/969/thumb-1920-969547.jpg'
    st.image(img_url)
    
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
    

    
    
    # 맨유 선수
    players = st.radio(
    "21 - 22 맨체스터 유나이티드 상위권 선수들",
    ('수비수', '미드필더', '공격수'))
    
    stats_manutd = df2[df2['Team'] == 'Manchester United']
    
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
 
 
 
st.subheader('년도별 프리미어리그 클럽 순위 확인')

with st.expander('데이터 프레임 확인하기') :
    st.dataframe(df)
    
    st.subheader('클럽 통계 데이터')
    st.dataframe( df.describe() )
>>>>>>> 7c28e84fee914c1472a54e7a08ba0335abfd9bab
