# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np
from streamlit_folium import folium_static
import folium
import re
import os
from geopy.geocoders import Nominatim
from pprint import pprint
from pandas.core.frame import DataFrame
# 위도, 경도 반환하는 함수
class mas():
    def __init__(self):
        self.pages=[]
    def run(self):
        
        mountain = pd.read_excel('mountain.xlsx', skiprows=[0,1])
        del mountain['NO.']
        
        mountain['산이름'] = mountain['산이름'].str.replace(r"\(.*\)","")
        name = mountain['산이름']
        
        name_ = st.sidebar.selectbox('선택하세요', name)
        st.table(mountain[mountain['산이름'].str.contains(name_)])


        m = folium.Map(location=[36.736429,127.801687], zoom_start=7)#기본지도
        m.add_child(folium.LatLngPopup())#클릭시 위도경도 표시
        app = Nominatim(user_agent='tutorial')#고유명칭으로 주소를 가져온다
        location = app.geocode(name_)#고유명칭으로 주소를 가져온다
        a=(location[1][0])#위도
        b=(location[1][1])#경도
        
        folium.Marker([a, b],tooltip=name_).add_to(m)#사이드바에서 클릭한 산을 마커 표시
        folium_static(m)#지도표시

        
        



























