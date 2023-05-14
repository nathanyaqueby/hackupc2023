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

import dice_ml
from dice_ml.utils import helpers

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
    address = st.text_input("Address", value="C/ del Consell de Cent 313, Barcelona")

    # insert house size in square meters
    # st.sidebar.subheader("Insert House Size in Square Meters")
    house_size = st.number_input("House Size (in m2)", min_value=0.0, max_value=10000.0, value=100.0, step=0.1)

    # insert number of bedrooms
    # st.sidebar.subheader("Number of Bedrooms")
    bedrooms = st.number_input("Number of Bedrooms", min_value=0, max_value=10, value=2, step=1)

    # insert number of bathrooms
    # st.sidebar.subheader("Number of Bathrooms")
    bathrooms = st.number_input("Number of Bathrooms", min_value=0, max_value=10, value=1, step=1)

    # select explainability method
    # st.sidebar.subheader("Select Explainability Method")
    explainability_method = st.selectbox("Select Explainability Method", ["SHAP-1", "SHAP-2", "DiCE"])

    # submit button
    # st.sidebar.subheader("Generate text")
    submit = st.form_submit_button("Predict price", type="primary", use_container_width=True)

st.sidebar.image("images/logo.png", use_column_width=True)

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

# predictXtest(2)

def getingPlotPrediction(listFeatures):
    features = pd.DataFrame([listFeatures],columns=x_test.columns)
    shap_values = explainer(features)
    st_shap(shap.plots.force(shap_values), height=300)

features_to_analize= ['propRange','kitchenRange','bathroomRange','interiorRange']
d = dice_ml.Data(dataframe=df,continuous_features=list(x_test.columns), outcome_name='price')
    # We provide the type of model as a parameter (model_type)
m = dice_ml.Model(model=model, backend="sklearn", model_type='regressor')

def getCounterfacualUpgrFromTest(x):
    exp = dice_ml.Dice(d, m, method="genetic")
    pred = y_test.iloc[x]
    # Multiple queries can be given as input at once
    query_instances_housing = x_test[x:x+1]
    exp_dice = exp.generate_counterfactuals(query_instances_housing, total_CFs=2, 
                                            desired_range=[pred,pred+100_000],features_to_vary=features_to_analize)

    return exp_dice
    
def getCounterfacualUpgr(list_of_features):
    features = pd.DataFrame([list_of_features],columns=x_test.columns)
    exp = dice_ml.Dice(d, m, method="genetic")
    pred = model.predict(features)[0]
    # Multiple queries can be given as input at once
    exp_dice = exp.generate_counterfactuals(features, total_CFs=2, 
                                            desired_range=[pred,pred+100_000],features_to_vary=features_to_analize)

    return exp_dice

input_vals = [house_size, bedrooms, bathrooms]

# get the first row of the dataframe that matches the input values
try:
    y_test = df[(df['square_meters'] == house_size) & (df['bedrooms'] == bedrooms) & (df['bathrooms'] == bathrooms)][0]
except:
    y_test = [100,2,1,4.1,4.4,4.1,3.9]

if explainability_method == "SHAP-1":
    predictXtest(y_test, 'W')
elif explainability_method == "SHAP-2":
    predictXtest(y_test, 'F')
elif explainability_method == "DiCE":
    getCounterfacualUpgr(y_test)