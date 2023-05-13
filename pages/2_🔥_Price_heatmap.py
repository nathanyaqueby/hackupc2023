import streamlit as st
from auth0_component import login_button
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(page_title="MLheads",
                   page_icon="🤯",
                   layout="wide",
                   initial_sidebar_state="expanded")

st.title("Real estate price range heatmap 🔥")
# st.markdown("Upload pictures of a property and our AI model will generate the perfect description based on the features in the images")

# sidebar
# st.sidebar.title("Navigation")

# load data
data = pd.read_json("preprocessed_10k.json").T

chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=41.403706,
        longitude=2.173504,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))

# # create a list of unique areas
# areas = data["area"].unique().tolist()

# with st.sidebar.form(key="form1"):
#     st.header("Insert an address or select the area to generate a heatmap")

#     # create a selectbox to choose an area
#     area = st.selectbox("Select an area", areas)

#     # filter data by area
#     data = data[data["area"] == area]

#     # create a list of unique price ranges
#     price_ranges = data["price_range"].unique().tolist()

#     # create a selectbox to choose a price range
#     price_range = st.selectbox("Select a price range", price_ranges)

#     # filter data by price range
#     data = data[data["price_range"] == price_range]

#     # create a list of unique property types
#     property_types = data["property_type"].unique().tolist()

#     # create a selectbox to choose a property type
#     property_type = st.selectbox("Select a property type", property_types)

#     # submit button
#     # st.sidebar.subheader("Generate text")
#     submit = st.form_submit_button("Generate heatmap", type="primary", use_container_width=True)

# # generate a heatmap of prices in the selected area, price range and property type as a map layer if submit button is clicked
# if submit:
#     with st.spinner("Generating heatmap..."):
#         st.write("Area: " + str(area))
#         st.write("Price range: " + str(price_range))
#         st.write("Property type: " + str(property_type))

#         # get the latitude and longitude of the area
#         latitude = data["latitude"].mean()

#         # create a map layer with the heatmap of prices
#         st.map(data)

#         # create a map layer with the locations of properties
#         st.map(data[["latitude", "longitude"]])