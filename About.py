import streamlit as st
from auth0_component import login_button
import streamlit.components.v1 as components
import leafmap.foliumap as leafmap

st.set_page_config(page_title="MLheads",
                   page_icon="🤯",
                   layout="wide",
                   initial_sidebar_state="expanded")

st.title("MLheads 🏠")
st.markdown("Explore the real estate market in Spain! Meanwhile, walk through the city of Barcelona with the OpenStreetMap below.")

st.markdown("""
    <style>
    .css-8hkptd {
            margin-right: 15px;
        }
    </style>""", unsafe_allow_html=True)

components.html("""
            <html>
            <head>
            </head>

            <iframe height="300" style="width: 100%;" scrolling="no" title="Spain OpenStreetMap" src="https://codepen.io/nqueby/embed/dygKrdm?default-tab=result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
            See the Pen <a href="https://codepen.io/nqueby/pen/dygKrdm">
            Spain OpenStreetMap</a> by Nathanya Queby Satriani (<a href="https://codepen.io/nqueby">@nqueby</a>)
            on <a href="https://codepen.io">CodePen</a>.
            </iframe>

            </html>
            """,
            height=700,
            scrolling=True
            )