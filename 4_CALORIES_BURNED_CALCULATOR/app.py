import streamlit as st
import pandas as pd
import numpy as np
import joblib



nav = st.sidebar.radio("Navigation",["Information","Predict"])
if nav=="Information":
    st.markdown("<h1 style='text-align: center; color: grey;'>CALORIES BURNED CALCULATOR</h1>", unsafe_allow_html=True)
    left, middle, right = st.columns((0.1, 12, 2))
    with middle:
         st.text('')
         st.text('')
         st.image('calorie_calculator.jpg',width=800)


if nav=="Predict":

    model=joblib.load(open('model.joblib', 'rb'))

    st.write("Calories Burned Calculator App")

    gender = st.selectbox("Select Gender",("Male","Female"))

    if (gender == "Male"):
       g = 0
    else:
       g = 1

    age = st.number_input("Enter age: ")

    height = st.number_input("Enter Height: ")

    weight = st.number_input("Enter Weight: ")

    duration = st.number_input("Enter Workout Duration: ")

    heartrate = st.number_input("Enter HeartRate: ")

    bodytemp = st.number_input("Enter Body Temperature: ")

    prediction = model.predict(pd.DataFrame(columns = ['Gender','Age','Height','Weight','Duration','Heart_Rate','Body_temp'],
                                        data = np.array([g,age,height,weight,duration,heartrate,bodytemp]).reshape(1,7)))

    if st.button("Predict"):
       st.write("Calories burned")
       st.success(prediction)
