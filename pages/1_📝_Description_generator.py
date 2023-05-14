import streamlit as st
from auth0_component import login_button
import openai
from gradio_client import Client

st.set_page_config(page_title="MLheads",
                   page_icon="🤯",
                   layout="wide",
                   initial_sidebar_state="expanded",
                   menu_items={
                       'Get help': 'https://github.com/diaa-shalaby/HackUPC2023',
                       'Report a bug': "https://github.com/diaa-shalaby/HackUPC2023",
                    })

st.title("Real Estate Post Generator 🏠")
st.markdown("Upload pictures of a property and our AI model will generate the perfect description based on the features in the images")

st.markdown("""
    <style>
    .css-8hkptd {
            margin-right: 15px;
        }
    </style>""", unsafe_allow_html=True)

# clientId = "JNM4ccGiddf0pF6uIGKAD5BKyaPWKVcB"
# domain = "mlheads.us.auth0.com"

# user_info = login_button(clientId, domain = domain)
# st.write(user_info)

# # sidebar
# st.sidebar.title("Navigation")

with st.sidebar.form(key="form1"):
    st.title("Generate a Real Estate Description")

    # upload image(s)
    # st.subheader("Upload Image(s)")
    uploaded_file = st.file_uploader("Upload image(s)", accept_multiple_files=True)

    # insert house size in square meters
    # st.sidebar.subheader("Insert House Size in Square Meters")
    house_size = st.number_input("House Size (in m2)", min_value=0.0, max_value=10000.0, value=25.0, step=0.1)

    # insert number of bedrooms
    # st.sidebar.subheader("Number of Bedrooms")
    bedrooms = st.number_input("Number of Bedrooms", min_value=0, max_value=10, value=2, step=1)

    # insert number of bathrooms
    # st.sidebar.subheader("Number of Bathrooms")
    bathrooms = st.number_input("Number of Bathrooms", min_value=0, max_value=10, value=1, step=1)

    # submit button
    # st.sidebar.subheader("Generate text")
    submit = st.form_submit_button("Generate text", type="primary", use_container_width=True)

st.sidebar.image("images/logo.png", use_column_width=True)

# generate a real estate description if submit button is clicked
if submit:
    with st.spinner("Generating text..."):

        col3, col4 = st.beta_columns([7, 3])

        with col3:
            st.markdown(f"House size: `{house_size}`")
            st.markdown(f"Number of bedrooms: `{bedrooms}`")
            st.markdown(f"Number of bathrooms: `{bathrooms}`")
            st.markdown(f"Image(s): `{uploaded_file}`")

            openai.api_key = st.secrets["API_KEY"]

            prompt1 = f"Generate a catchy title based on the following features:\n\nHouse size: {house_size} m2\nNumber of bedrooms: {bedrooms}\nNumber of bathrooms: {bathrooms}\n\nImage(s): {uploaded_file}"
            prompt2 = f"Generate a minimum 300-word real estate description based on the following features:\n\nHouse size: {house_size} m2\nNumber of bedrooms: {bedrooms}\nNumber of bathrooms: {bathrooms}\n\nImage(s): {uploaded_file}"
            # st.write(f"GPT-3 Prompt: {prompt}")

            st.markdown("---")

            response1 = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt1,
                temperature=0.8,
                max_tokens=1000,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            response2 = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt2,
                temperature=0.8,
                max_tokens=1000,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            #st.write(f"GPT-3 Response\n{response}")
            title_result = response1['choices'][0]["text"]
            text_result = response2['choices'][0]["text"]

            st.markdown("## Generated Text")
            st.markdown(f"**{title_result}**")
            st.write(f"{text_result}")

            client = Client("https://tweakdoor-stabilityai-stable-diffusion-2-1.hf.space/")
            result = client.predict(
                            "Howdy!",	# str representing input in 'Input' Textbox component
                            api_name="/predict"
            )
            print(result)

        with col4:
            st.image("images/test_img.jpg", use_column_width=True)