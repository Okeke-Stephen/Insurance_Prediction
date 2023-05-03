'''import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models
ins_model = pickle.load(open('insurance_model.sav', 'rb'))

# page title
st.title('Insurance Predictive Framework')
    
    
# getting the input data from the user
col1, col2 = st.columns(2)
    
with col1:
  age = st.text_input('Age')
        
with col2:
   sex = st.text_input('Sex')
   if (sex == 'male'):
    male = 1
    female = 0
   else:
    male = 0
    fmale = 1

with col1:
  bmi = st.text_input('Body Mass Index')
    
with col2:
  children = st.sidebar.slider('Children', min_value=0, max_value=10, value=0, step = 1)
    
with col1:
    smoker = st.text_input('Smoker')
    
with col2:
  region = st.text_input('Region')
  if (region == 'Region Northwest'):
    region_northwest = 1
    region_southeast = 0
    region_southwest = 0
        
  elif (region == 'Region Southeast'):
      region_northwest = 0
      region_southeast = 1
      region_southwest = 0

  else:
      region_northwest = 0
      region_southeast = 0
      region_southwest = 1

# creating a button for Prediction

# creating a button for Prediction
if st.button("Predict"):
    output = ins_model.predict([[age, sex,	bmi,	children,	smoker,	region]])
    output = '$' + str(output)
    st.success('The insurance price estimate is: {}'.format(output))'''
    
    

import pickle
import sys
from streamlit_option_menu import option_menu   
import pandas as pd 
import streamlit as st 
from pycaret.regression import load_model, predict_model 

sys.setrecursionlimit(15000)
st.set_page_config(page_title = "Insurance Charges Prediction")

@st.cache_data(allow_output_mutation=True)
def get_model():
    return load_model('insurance_model')

def predict_model(model, data):
    predictions = predict_model(model, data=data)
    return predictions['Label'][0]

model  = get_model()

st.title("Insurance Charges Predictive System")

# getting the input data from the user
col1, col2 = st.columns(2)

with col1:
    form = st.form('charges')

with col2:
    age = form.number_input('Age', min_value=1, max_value=100, value=25)
    
with col1:
    sex = form.radio('Sex', ['Male', 'Female'])
    
with col2:
    bmi = form.number_input('BMI', min_value=10.0, max_value=50.0, value=20.0)

with col1:
    children = form.slider('Children', min_value=0, max_value=10, value=0)

with col2:
    region_list = ['Southwest', 'Northwest', 'Northeast', 'Southeast']

with col1:
    region = form.selectbox('Region', region_list)

with col2:
    if form.checkbox('Smoker'):
        smoker = 'yes'
    else:
        smoker = 'no'
    
predict_button = form.form_submit_button('Predict')

input_dict = {
    'age':age,
    'sex':sex.lower(),
    'bmi':bmi,
    'children': children,
    'smoker': smoker,
    'region': region.lower()
}

input_df = pd.DataFrame([input_dict])

if predict_button:
    output = predict_model(model, input_df)
    st.success("The predicted charges are ${: .2f}".format(output))

