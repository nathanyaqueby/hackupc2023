import streamlit as st
from auth0_component import login_button
from streamlit_extras.mention import mention
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
st.markdown("""
    <style>
    .css-8hkptd {
            margin-right: 15px;
        }
    </style>""", unsafe_allow_html=True)

# tech support section
with st.sidebar.form(key='tech_support'):
    st.title("Contact")

    st.markdown("Get help with any technical issue you might experience.")

    mention(
    label="Website",
    icon="💻",
    url="https://restb.ai/",
    write="Website"
    )

    mention(
    label="Twitter",
    icon="🐤",
    url="https://twitter.com/restb_ai?lang=en",
    write="Twitter"
    )

    mention(
    label="GitHub",
    icon="⚙️",
    url="https://www.github.com/diaa-shalaby/HackUPC2023",
    write="GitHub"
    )

    # create a submit button
    if st.form_submit_button("Contact us", type="secondary", use_container_width=True):
        st.write("Submitted!")

# load data
data = pd.read_json("preprocessed_10k.json").T

# get the average prices per region
avg_prices_region = data.groupby('region')['price'].mean()

# get the average prices per city
avg_prices_city = data.groupby('city')['price'].mean()

chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [41.403706, 2.173504],
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
    height=900
))

# create a list of unique areas
cities = data["city"].unique().tolist()

with st.sidebar.form(key="form1"):
    st.header("Insert an address or select the area to generate a heatmap")

    # create a selectbox to choose an area
    city = st.selectbox("Select a city", cities)

    # filter data by area
    data = data[data["city"] == city]

    # submit button
    # st.sidebar.subheader("Generate text")
    submit = st.form_submit_button("Generate heatmap", type="primary", use_container_width=True)

with st.expander:
    col1, col2 = st.beta_columns(2)

    with col1:
        st.header("Average price per region")
        st.bar_chart(avg_prices_region)
    
    with col2:
        st.header("Average price per city")
        st.bar_chart(avg_prices_city)

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