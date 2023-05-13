"""
This is the page where the user can predict the price of a house.
They will insert the features of the house and the model will predict the price with a regressor model
and display it to the user.
We also add an explainability method SHAP to explain the model's prediction.
"""
import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

st.set_page_config(page_title="MLheads",
                   page_icon="🤯",
                   layout="wide",
                   initial_sidebar_state="expanded")

st.title("Predict the price 💰")
# st.markdown("Upload pictures of a property and our AI model will generate the perfect description based on the features in the images")

# sidebar
# st.sidebar.title("Navigation")
st.markdown("""
    <style>
    .css-8hkptd {
            margin-right: 15px;
        }
    </style>""", unsafe_allow_html=True)

with st.sidebar.form(key="form1"):
    st.title("Insert the features of the house")

    # upload image(s)
    # insert address
    # st.sidebar.subheader("Insert Address")
    address = st.text_input("Address", value="Koningin Wilhelminaplein 13, Barcelona")

    # insert house size in square meters
    # st.sidebar.subheader("Insert House Size in Square Meters")
    house_size = st.number_input("House Size (in m2)", min_value=0.0, max_value=10000.0, value=25.0, step=0.1)

    # insert number of bedrooms
    # st.sidebar.subheader("Number of Bedrooms")
    bedrooms = st.number_input("Number of Bedrooms", min_value=0, max_value=10, value=2, step=1)

    # insert number of bathrooms
    # st.sidebar.subheader("Number of Bathrooms")
    bathrooms = st.number_input("Number of Bathrooms", min_value=0, max_value=10, value=1, step=1)

    # submit button
    # st.sidebar.subheader("Generate text")
    submit = st.form_submit_button("Predict price", type="primary", use_container_width=True)

# load data
data = pd.read_json("preprocessed_10k.json").T

# get the average prices per region
avg_prices_region = data.groupby('region')['price'].mean()

# get the average prices per city
avg_prices_city = data.groupby('city')['price'].mean()

