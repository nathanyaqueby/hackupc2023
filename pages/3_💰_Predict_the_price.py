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

# get the average prices per region
avg_prices_region = data.groupby('region')['price'].mean()

# get the average prices per city
avg_prices_city = data.groupby('city')['price'].mean()

