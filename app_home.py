import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import streamlit as st
from tkinter.tix import COLUMN
from pyparsing import empty


def run_home_app() :
    st.subheader('Welcome to the Premire League')
    img_url = 'https://siri.or.kr/wp/wp-content/uploads/2022/05/epl.png'
    st.image(img_url)
    
    ## Show videos
    st.subheader('프리미어리그 소개 영상')
    video_file = open('data/The Official Premier League Anthem.mp4', 'rb')
    st.video(video_file)

    st.text('이 대시보드는 영국 축구 리그인 프리미어리그를 분석해주는 내용입니다.')
    st.text('클럽 정보를 넣으면 해당 클럽 정보를 알려줍니다.')
    st.text('클럽 순위는 Statistic 탭을 확인하세요.')
    