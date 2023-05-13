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

components.html("""
            <html>
            <head>
            </head>

            <iframe height="700" style="width: 100%;" scrolling="no" title="Spain OpenStreetMap" src="https://codepen.io/nqueby/embed/dygKrdm?default-tab=result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
            See the Pen <a href="https://codepen.io/nqueby/pen/dygKrdm">
            Spain OpenStreetMap</a> by Nathanya Queby Satriani (<a href="https://codepen.io/nqueby">@nqueby</a>)
            on <a href="https://codepen.io">CodePen</a>.
            </iframe>

            </html>
            """,
            height=700,
            scrolling=True
            )

# Set initial location to Madrid
init_location = [40.416775, -3.703790]

# Create a folium map object
# m = folium.Map(location=init_location, zoom_start=6)

# # Add a marker for Madrid
# folium.Marker(location=[40.416775, -3.703790], popup='Madrid').add_to(m)

# # Add a marker for Barcelona
# folium.Marker(location=[41.385064, 2.173404], popup='Barcelona').add_to(m)

# # Display the map in Streamlit
# st.markdown(folium.Map(location=init_location, zoom_start=6)._repr_html_(), unsafe_allow_html=True)

m = folium.Map(location=init_location, zoom_start=16)

folium.Marker(
    init_location, popup="Madrid", tooltip="Madrid"
).add_to(m)

barcelona_coords = [41.385064, 2.173404]

folium.Marker(
    barcelona_coords, popup="Barcelona", tooltip="Barcelona"
).add_to(m)

st_data = st_folium(m, width=640, height=640)