# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium
from geopy.geocoders import Nominatim

st.title('mountain')



 

        

m = folium.Map(location=[36.736429,127.801687], zoom_start=7)#기본지도
m.add_child(folium.LatLngPopup())#클릭시 위도경도 표시
app = Nominatim(user_agent='tutorial')#고유명칭으로 주소를 가져온다
print(m)
        
        


        



















