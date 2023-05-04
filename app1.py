import pickle
import sklearn
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
ins_model = pickle.load(open('insurance_model.sav.pkl', 'rb'))

st.title('Insurance Charges Prediction')
st.markdown('Enter Values to Predict your Insurance Charge')

st.header("Insurance Charges Predictive System")
col1, col2 = st.columns(2)

with col1:
	age = form.number_input('Age', min_value=1, max_value=100, value=25)

with col2:
	sex = form.radio('Sex', ['Male', 'Female'])

with col1:
	bmi = form.number_input('BMI', min_value=10.0, max_value=50.0, value=20.0)

with col2:
	children = form.slider('Children', min_value=0, max_value=10, value=0)

with col1:
	region_list = ['Southwest', 'Northwest', 'Northeast', 'Southeast']
	region = form.selectbox('Region', region_list)

with col2:
	if form.checkbox('Smoker'):
    		smoker = 'yes'
	else:
    		smoker = 'no'
    
st.text('')
if st.button("Predict Charge"):
    result = ins_model.predict(
        np.array([[age, sex, bmi, children, region, smoker]]))
    st.text('The house price estimate is:' + '$' + result[0])
