import streamlit as st
from auth0_component import login_button

st.set_page_config(page_title="MLheads",
                   page_icon="🤯",
                   layout="wide",
                   initial_sidebar_state="expanded")

clientId = "JNM4ccGiddf0pF6uIGKAD5BKyaPWKVcB"
domain = "mlheads.us.auth0.com"

user_info = login_button(clientId, domain = domain)
st.write(user_info)
