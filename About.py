import streamlit as st
from auth0_component import login_button

st.set_page_config(page_title="MLheads",
                   page_icon="🤯",
                   layout="wide",
                   initial_sidebar_state="expanded")

st.title("Real Estate Post Generator 🏠")
st.markdown("Upload pictures of a property and our AI model will generate the perfect description based on the features in the images")

clientId = "JNM4ccGiddf0pF6uIGKAD5BKyaPWKVcB"
domain = "mlheads.us.auth0.com"

user_info = login_button(clientId, domain = domain)
st.write(user_info)

# sidebar
st.sidebar.title("Navigation")

# upload image(s)
st.sidebar.subheader("Upload Image(s)")
uploaded_file = st.sidebar.file_uploader("Choose an image...", accept_multiple_files=True)

# insert house size in square meters
# st.sidebar.subheader("Insert House Size in Square Meters")
house_size = st.sidebar.number_input("House Size", min_value=0.0, max_value=10000.0, value=0.0, step=0.1)

# insert number of bedrooms
# st.sidebar.subheader("Number of Bedrooms")
bedrooms = st.sidebar.number_input("Number of Bedrooms", min_value=0, max_value=10, value=0, step=1)

# insert number of bathrooms
# st.sidebar.subheader("Number of Bathrooms")
bathrooms = st.sidebar.number_input("Number of Bathrooms", min_value=0, max_value=10, value=0, step=1)

# submit button
st.sidebar.subheader("Generate text")
