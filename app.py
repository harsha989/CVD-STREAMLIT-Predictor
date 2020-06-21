import streamlit as st
import pandas as pd
import numpy as np
import pickle

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
    age=st.number_input(label="Age",min_value=18)
    gender = st.selectbox('Select Gender',('Male','Female'))
    if gender=='Female':
    	gender=1
    elif gender=='Male':
    	gender=2
    height=st.number_input("Height",value=5.0)
    weight=st.number_input("Weight",min_value=60)
    ap_hi=st.number_input("Systolic blood pressure",min_value=120)
    ap_lo=st.number_input("Diastolic blood pressure",min_value=80)
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
    st.sidebar.markdown(
    	        "<style>.center {display: block;margin-left: auto;margin-right: auto;width: 100%;}</style>"
    			"<style>.div-2 {height:220px;}</style>"
    			"<div class='div-2',align='center'><br>"
    			"<a href='https://www.kaggle.com/sulianova/cardiovascular-disease-dataset'>"
    			"<img src='https://github.com/harsha989/hello/blob/master/Oncology_12.3.19.jpg' alt='Landscape' height='200' width='306'></a></div>",unsafe_allow_html=True)
    st.sidebar.markdown(
    	    	"<style>.center {display: block;margin-left: auto;margin-right: auto;width: 100%;}</style>"
    			"<style>.div-2 {height:220px;}</style>"
    			"<div class='div-2',align='center'><br>"
    			"<a href='https://www.linkedin.com/in/mittapallisriharsha'>"
    			"<img src='https://github.com/harsha989/hello/blob/master/Oncology_12.3.19.jpg' alt='Landscape' height='200' width='306'></a></div>",unsafe_allow_html=True)
    st.sidebar.markdown(
    	        "<style>.center {display: block;margin-left: auto;margin-right: auto;width: 100%;}</style>"
    			"<style>.div-2 {height:220px;}</style>"
    			"<div class='div-2',align='center'><br>"
    			"<a href='https://github.com/harsha989/CVD-Streamlit'>"
    			"<img src='https://github.com/harsha989/hello/blob/master/Oncology_12.3.19.jpg' alt='Landscape' height='200' width='306'></a></div>",unsafe_allow_html=True)
if __name__=='__main__':
    main()
