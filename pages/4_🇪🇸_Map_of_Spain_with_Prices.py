import streamlit as st
from auth0_component import login_button
import streamlit.components.v1 as components
from streamlit_extras.mention import mention
import folium
import leafmap.foliumap as leafmap
from streamlit_folium import st_folium

st.set_page_config(page_title="MLheads",
                   page_icon="🤯",
                   layout="wide",
                   initial_sidebar_state="expanded")

st.title("Compare prices of cities in Spain 🇪🇸")

st.sidebar.info("Explore the real estate market in Spain! Meanwhile, walk through the city of Barcelona with the OpenStreetMap.")

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

# Set initial location to Barcelona
init_location = [41.385064, 2.173404]

m = folium.Map(location=init_location, zoom_start=10)

folium.Marker(
    init_location, popup="Barcelona", tooltip="Barcelona"
).add_to(m)

madrid_coords = [40.416775, -3.703790]

folium.Marker(
    madrid_coords, popup="Madrid", tooltip="Madrid"
).add_to(m)

st_data = st_folium(m, width=1440, height=640)