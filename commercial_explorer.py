import pandas as pd
import numpy as np
import streamlit as st
import pydeck as pdk
import random

"""
# Shops, amenities & tourism.
> København
"""

df = pd.read_csv('commercial_kbh.csv').loc[:, [
    'lat', 'lon', 'kind', 'category'
]].dropna()

radius = st.sidebar.slider('Radius', value=50, min_value=10, max_value=200)

ALL_LAYERS = {
    cat: pdk.Layer(
            "HexagonLayer",
            data=df[df.category==cat],
            get_position=['lon', 'lat'],
            auto_highlight=True,
            radius=radius,#75,
            opacity=0.4,
            elevation_scale=1,
            elevation_range=[1, 1000],
            extruded=True,
            coverage=1,
        )
    for cat in df.category.unique()
}

st.sidebar.markdown('### Map Layers')
selected_layers = [
    layer for layer_name, layer in ALL_LAYERS.items()
    if st.sidebar.checkbox(layer_name, True)]

if selected_layers:
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={"latitude": 55.6836750,
                            "longitude": 12.5730280, "zoom": 11, "pitch": 50},
        layers=selected_layers
    ))
else:
    st.error("Please choose at least one layer above.")
