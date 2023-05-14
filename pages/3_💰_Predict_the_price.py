"""
This is the page where the user can predict the price of a house.
They will insert the features of the house and the model will predict the price with a regressor model
and display it to the user.
We also add an explainability method SHAP to explain the model's prediction.
"""
import streamlit as st
import pandas as pd
from streamlit_shap import st_shap
import shap
from sklearn.model_selection import train_test_split
shap.initjs()
# import ridge
from sklearn.linear_model import Ridge

st.set_page_config(page_title="MLheads",
                   page_icon="🤯",
                   layout="wide",
                   initial_sidebar_state="expanded")

st.title("Predict the price 💰")
# st.markdown("Upload pictures of a property and our AI model will generate the perfect description based on the features in the images")

# sidebar
# st.sidebar.title("Navigation")
st.markdown("""
    <style>
    .css-8hkptd {
            margin-right: 15px;
        }
    </style>""", unsafe_allow_html=True)

with st.sidebar.form(key="form1"):
    st.title("Insert the features of the house")

    # upload image(s)
    # insert address
    # st.sidebar.subheader("Insert Address")
    address = st.text_input("Address", value="Koningin Wilhelminaplein 13, Barcelona")

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
    submit = st.form_submit_button("Predict price", type="primary", use_container_width=True)

# load data
data = pd.read_json("preprocessed_sample.json")
df = data.T
df = df.reset_index()

# get the average prices per region
# avg_prices_region = data.groupby('region')['price'].mean()

# get the average prices per city
# avg_prices_city = data.groupby('city')['price'].mean()

# display images after clicking the submit button
# if submit:
#     with st.spinner("Churning out predictions..."):
#         st.markdown("## Predicted price and relevant features")
#         st.image("images/shap1.png", use_column_width=True)
#         st.image("images/shap2.png", use_column_width=True)

new_column_names = {
    'image_data_r1r6_property': 'propRange',
    'image_data_r1r6_kitchen': 'kitchenRange',
    'image_data_r1r6_bathroom': 'bathroomRange',
    'image_data_r1r6_interior': 'interiorRange'
}

df = df.rename(columns=new_column_names)
df = df[['price','square_meters','bedrooms','bathrooms','propRange','kitchenRange','bathroomRange','interiorRange']]

# remove rows with nan values
df = df.dropna()

# set x and y
x = df.drop('price', axis = 1)
y = df['price']

# split the data into train and test
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.2, random_state=42)

# convert all columns to float
for i in df.columns:
    df[i] = df[i].astype(float)

# use Ridge regression to predict the price
model = Ridge(alpha=10, random_state=42)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

# use SHAP to explain the model's prediction
explainer = shap.Explainer(model, x_train)
shap_values = explainer(x_test)

#############
def predictXtest(num_to_predict,typePlot ='F'):
    print("The real price is ", y_test.iloc[num_to_predict])
    if typePlot=='W':
       st_shap(shap.plots.waterfall(shap_values[num_to_predict]), height=300)
    else: 
        st_shap(shap.plots.force(shap_values[num_to_predict]), height=300)

predictXtest(2, 'W')
predictXtest(4)

def getingPlotPrediction(listFeatures):
    features = pd.DataFrame([listFeatures],columns=x_test.columns)
    shap_values = explainer(features)
    st_shap(shap.plots.force(shap_values), height=300)

getingPlotPrediction([100,2,2,3,5,4,6])