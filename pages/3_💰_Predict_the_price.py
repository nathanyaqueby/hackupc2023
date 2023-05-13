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


# load data
data = pd.read_json("preprocessed_10k.json").T

# get a list of all the cities
cities = data["city"].unique().tolist()

# get a list of all the provinces
# neighborhoods = data["neigborhood"].unique().tolist()

street = st.text_input("Street", "C/ de Balmes 75")
# set up a dropdown menu to select the state between Hamburg, Berlin and Bremen
# province = st.selectbox("Select a state", ["Hamburg", "Berlin", "Bremen"], index=0)
province = "Barcelona"
country = "Spain"

city = st.selectbox("Select a state", cities, index=0)

geolocator = Nominatim(user_agent="GTA Lookup")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
location = geolocator.geocode(street+", "+city+", "+province+", "+country)

lat = location.latitude
lon = location.longitude

st.write("Latitude = {}, Longitude = {}".format(lat, lon))