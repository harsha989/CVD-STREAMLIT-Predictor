import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image

image = Image.open('images/Oncology_12.3.19.jpg')
image1 = Image.open('images/linkedin.png')
image2 = Image.open('images/Github.jpg')

# Load the SVM Classifier model
filename = 'LR.pkl'
classifier = pickle.load(open(filename, 'rb'))

def predict(age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active):
	prediction=classifier.predict([[age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active]])
	print(prediction)
	return prediction

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")

def main():
    html_temp="""
    <div style="background-color:black;padding:10px">
    <h2 style="color:white;text-align:center;">CardioVascularDisease Predictor </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age=st.number_input(label="Age",min_value=15)
    gender = st.selectbox('Select Gender',('Male','Female'))
    if gender=='Female':
    	gender=1
    elif gender=='Male':
    	gender=2
    height=st.number_input("Height",value=5.0)
    weight=st.number_input("Weight",min_value=40)
    ap_hi=st.number_input("Systolic blood pressure",min_value=10)
    ap_lo=st.number_input("Diastolic blood pressure",min_value=10)
    cholesterol = st.selectbox("Cholesterol",("Normal","Above Normal", "Well Above Normal"))
    if cholesterol=="Normal":
    	cholesterol=1
    elif cholesterol=="Above Normal":
    	cholesterol=2
    elif cholesterol=="Well Above Normal":
    	cholesterol=3
    gluc = st.selectbox('Glucose',("Normal","Above Normal", "Well Above Normal"))
    if gluc=="Normal":
    	gluc=1
    elif gluc=="Above Normal":
    	gluc=2
    elif gluc=="Well Above Normal":
    	gluc=3
    smoke = st.selectbox('Smoking',("Yes", "No"))
    if smoke=="No":
    	smoke=0
    elif smoke=="Yes":
    	smoke=1
    alco = st.selectbox('Alcohol',("Yes", "No"))
    if alco=="No":
    	alco=0
    elif alco=="Yes":
    	alco=1
    active = st.selectbox('Physical Activity',("Yes", "No"))
    if active=="No":
    	active=0
    elif active=="Yes":
    	active=1
    result=""
    if st.button("Predict"):
    	result=predict(age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active)
    if result==0:	
        st.success("You Don't Have CardioVascularDisease")
    elif result==1:
    	st.success("You Have CardioVascularDisease")
    st.sidebar.image(image,use_column_width=True)
    st.sidebar.markdown(
                "[Kaggle Dataset](https://www.kaggle.com/sulianova/cardiovascular-disease-dataset)",unsafe_allow_html=True)
    st.sidebar.image(image1,use_column_width=True)
    st.sidebar.markdown(
                "[Linkedin Profile](https://www.linkedin.com/in/mittapallisriharsha)",unsafe_allow_html=True)
    st.sidebar.image(image2,use_column_width=True)
    st.sidebar.markdown(
                "[Github Page](https://github.com/harsha989/CVD-STREAMLIT-Predictor)",unsafe_allow_html=True)
if __name__=='__main__':
    main()
