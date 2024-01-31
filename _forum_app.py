import streamlit as st
import folium
from streamlit_folium import st_folium, folium_static
import folium.raster_layers

st.set_page_config(
        layout = "wide",
        initial_sidebar_state="collapsed")


# Function to create a folium map with an image overlay
def create_map(pixelated):
    map_ = folium.Map(location=[0, 0], zoom_start=2)
    image = folium.raster_layers.ImageOverlay(
        image='data/temp/img_layer.tiff',
        bounds=[[-90, -180], [90, 180]],
        pixelated=pixelated,
        name="Raster Layer"
    )
    image.add_to(map_)
    return map_


pixelated = st.checkbox("Pixelated Parameter", value=True)

# Layout with two columns
col1, col2 = st.columns([1, 1], gap="medium")

# Column 1: st_folium
with col1:
    st.write("st_folium visualization")
    map1 = create_map(pixelated=pixelated)
    st_folium(map1, use_container_width=True, height=600)

# Column 2: folium_static
with col2:
    st.write("folium_static visualization")
    map2 = create_map(pixelated=pixelated)
    folium_static(map2, height=600)
