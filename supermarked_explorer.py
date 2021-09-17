import pandas as pd
import numpy as np
import streamlit as st
import pydeck as pdk
import random
import seaborn as sns

"""
# Supermarkeder
> København
"""

df = pd.read_csv('https://raw.githubusercontent.com/skipperkongen/commercial-explorer/main/supermarkeder_kbh.csv').loc[:, [
    'lat', 'lon', 'brand', 'branch'
]].dropna()
df['size'] = 75

brands = df.brand.unique()

palette = np.array(sns.color_palette("tab10")) * 255

colors = {
    brand: list(palette[i]) #[random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    for i, brand in enumerate(brands)
}

ALL_LAYERS = {
    brand: pdk.Layer(
        "ScatterplotLayer",
        data=df[df.brand==brand],
        get_position=['lon', 'lat'],
        pickable=True,
        opacity=0.8,
        stroked=True,
        filled=True,
        radius_scale=1,
        radius_min_pixels=1,
        radius_max_pixels=100,
        line_width_min_pixels=1,
        get_radius="size",
        get_fill_color=colors[brand], # [255, 140, 0]
        get_line_color=[0, 0, 0],
    )
    for brand in brands
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
        layers=selected_layers,
        tooltip={"text": "{brand},\n{branch}"}
    ))
else:
    st.error("Please choose at least one layer above.")
