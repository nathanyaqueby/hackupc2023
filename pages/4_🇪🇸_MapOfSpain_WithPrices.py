import streamlit as st
from auth0_component import login_button
from streamlit_extras.mention import mention
import pandas as pd
import numpy as np
import pydeck as pdk
import folium as fol

st.set_page_config(page_title="MLheads",
                   page_icon="🤯",
                   layout="wide",
                   initial_sidebar_state="expanded")

st.title("Compare prices of cities in Spain")
# st.markdown("Upload pictures of a property and our AI model will generate the perfect description based on the features in the images")

# sidebar
# st.sidebar.title("Navigation")

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

# Create a map centered on Spain
m = fol.Map(location=[40.416775, -3.703790], zoom_start=6)

# Add a marker for Madrid
fol.Marker([40.416775, -3.703790], popup='Madrid').add_to(m)

# Display the map in Streamlit
st.markdown(m._repr_html_(), unsafe_allow_html=True)


