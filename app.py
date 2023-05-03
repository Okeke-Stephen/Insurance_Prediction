import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models
ins_model = pickle.load(open('insurance_model.sav', 'rb'))

# page title
st.title('Insurance Predictive Framework')
    
    
# getting the input data from the user
col1, col2, col3 = st.columns(3)
    
with col1:
  age = st.text_input('Age')
        
with col2:
   sex = st.text_input('Sex')

with col3:
  bmi = st.text_input('Body Mass Index')
    
with col1:
  children = st.sidebar.slider('Children', min_value=0, max_value=10, value=0, step = 1)
    
with col2:
    smoker = st.text_input('Smoker')
    
with col3:
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
    st.success('The insurance price estimate is: {}'.format(output))
