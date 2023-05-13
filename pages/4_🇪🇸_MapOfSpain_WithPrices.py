import streamlit as st
from auth0_component import login_button
import streamlit.components.v1 as components
from streamlit_extras.mention import mention
import folium
import leafmap.foliumap as leafmap

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

# components.html("""
#             <html>
#             <head>
#             </head>

#             <iframe height="700" style="width: 100%;" scrolling="no" title="Spain OpenStreetMap" src="https://codepen.io/nqueby/embed/dygKrdm?default-tab=result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
#             See the Pen <a href="https://codepen.io/nqueby/pen/dygKrdm">
#             Spain OpenStreetMap</a> by Nathanya Queby Satriani (<a href="https://codepen.io/nqueby">@nqueby</a>)
#             on <a href="https://codepen.io">CodePen</a>.
#             </iframe>

#             </html>
#             """,
#             height=700,
#             scrolling=True
#             )

# Create a map centered on Spain
m = fol.Map(location=[40.416775, -3.703790], zoom_start=6)

# Add a marker for Madrid
fol.Marker([40.416775, -3.703790], popup='Madrid').add_to(m)

# Display the map in Streamlit
st.markdown(m._repr_html_(), unsafe_allow_html=True)
