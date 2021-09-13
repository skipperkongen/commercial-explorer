import pandas as pd
import numpy as np
import streamlit as st
import pydeck as pdk
import random

# Config

st.set_page_config(layout="wide")

# Description

"""
# Butikker, forlystelser & logi.
> København
"""

# Data

df = pd.read_csv('commercial_kbh.csv').loc[:, [
    'lat', 'lon', 'kind', 'category'
]].dropna()

# Sidebar

st.sidebar.markdown('### Indstillinger')

radius = st.sidebar.slider('Radius', value=50, min_value=10, max_value=200)

category = st.sidebar.selectbox(
    'Vælg kategori',
     df['category'].unique())

all_kinds = list(sorted(df[df.category == category].kind.unique()))
kinds = st.sidebar.multiselect(
        "Vælg underkategorier", all_kinds, all_kinds
    )

## Render

df_selected = df[(df.category==category) & (df.kind.isin(kinds))]

st.write('Antal lokationer:', len(df_selected))

selected_layers = [
    pdk.Layer(
            "HexagonLayer",
            data=df_selected,
            get_position=['lon', 'lat'],
            auto_highlight=True,
            radius=radius,#75,
            opacity=0.4,
            elevation_scale=1,
            elevation_range=[5, 1000],
            extruded=True,
            coverage=1,
        )
]

mean_lat = df_selected.lat.mean()
mean_lon = df_selected.lon.mean()

if len(df_selected):
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={"latitude": mean_lat,
                            "longitude": mean_lon, "zoom": 11, "pitch": 50},
        layers=selected_layers
    ))
else:
    st.error("Vælg mere data for at vise kort")
