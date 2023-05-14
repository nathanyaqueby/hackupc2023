import streamlit as st
from auth0_component import login_button
import streamlit.components.v1 as components
from streamlit_extras.mention import mention
import folium
import leafmap.foliumap as leafmap
from streamlit_folium import st_folium
import pandas as pd

st.set_page_config(page_title="MLheads",
                   page_icon="🤯",
                   layout="wide",
                   initial_sidebar_state="expanded",
                   menu_items={
                       'Get help': 'https://github.com/diaa-shalaby/HackUPC2023',
                       'Report a bug': "https://github.com/diaa-shalaby/HackUPC2023",
                    })

st.title("Average prices to live in provinces in Spain 🇪🇸")

st.sidebar.info("How much does it cost to live in different provinces of Spain? Click on the markers to find out!")

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

st.sidebar.image("images/logo.png", use_column_width=True)

# Puts all provinces in an array (https://www.indomio.es/en/mercado-inmobiliario/ -> Data)
df = pd.read_csv('spainProvinces.csv')
spainProvList = [list(row) for row in df.values]

# Makes map (w/ Barcelona as start)
m = folium.Map(location=[41.3851,2.1734], zoom_start=6)

# Populates a marker at each province of Spain
for x in spainProvList:
    if x[3] > 5:
        icon = folium.Icon(color="blue")
    elif x[3] < 2:
        icon = folium.Icon(color="orange")
    else:
        icon = folium.Icon(color="red")
    
    folium.Marker(
        location=[x[1], x[2]], popup=f"{x[0]}", tooltip=f"€{x[3]}", icon=icon
    ).add_to(m)

st_data = st_folium(m, width=1440, height=640)