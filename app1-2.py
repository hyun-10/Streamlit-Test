# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np

from streamlit_folium import folium_static
import folium

from pages.pro2 import mas

app=mas()
st.title('mountain')

app.run()



    




























