import streamlit as st
import time 
import joblib
import pandas as pd 

pipeline = joblib.load("models/used_car_price_predictor.pkl")

df = pd.read_csv("data/raw/cars_dataset.csv")

st.sidebar.title("🚗 Used Car Price Predictor")
st.divider()
st.sidebar.markdown("---")

st.sidebar.subheader("📌 Model")
st.sidebar.write("Multiple Linear Regression")

st.sidebar.subheader("📊 Dataset")
st.sidebar.write("UK Used Car Dataset")

st.sidebar.subheader("📁 Input Features")
st.sidebar.write("9 Features")
st.sidebar.subheader("Model Performance")
st.sidebar.write("R2 Score : 0.88")

st.sidebar.subheader("👨‍💻 Developed By")
st.sidebar.write("Sahil")


model_list = sorted(df["model"].unique()) 
transmission_list = sorted(df["transmission"].unique())
fuel_type_list = sorted(df["fuelType"].unique())
make_list = sorted(df["Make"].unique())

st.title("🚗 Used Car Price Prediction")
st.markdown("Predict the **market value** of a used car using a \n"
"**Machine Learning (Multiple Linear Regression)** model.")




with st.container(border=True):

    st.subheader("🚘 Car Information")
    st.text("Fill All Details Carefully")

st.subheader("Enter Car Details")

col1 ,col2 = st.columns(2)
with col1:
    year =st.number_input("Choose Year", min_value = 1990, max_value =2025, value =2018)
    

with col2:
    Fuel_type = st.selectbox("Fuel Type", fuel_type_list)

col1 ,col2 = st.columns(2)
with col1:
    transmission_type = st.selectbox("Transmission" , transmission_list)
    

with col2:
    mileage =st.number_input("Choose Mileage :", min_value=1, value =18000)

col1 ,col2 = st.columns(2)

with col1:
    engine_size = st.number_input("Choose Engine Size:", min_value=0, value = 2) 

with col2:
    mpg = st.number_input("Choose MPG:", min_value=0, value =10)


tax =st.number_input("Tax:", min_value=0, value = 100)


model = st.selectbox("Choose Model Number :", model_list)


make = st.selectbox("Choose Make:", make_list)
filter_models= sorted(df[df["Make"] == make]["model"].unique())
model = st.selectbox("Choose Make", filter_models)


if st.button("Predict Price",type="primary", use_container_width=True):
    with st.spinner("Predicting..."):
        time.sleep(2)
        car_data = {
    "model": model,
    "year": year,
    "transmission": transmission_type,
    "mileage": mileage,
    "fuelType": Fuel_type,
    "tax": tax,
    "mpg": mpg,
    "engineSize": engine_size,
    "Make": make
    }

    input_data = pd.DataFrame([car_data]) 
    st.subheader("Input Data")
    st.dataframe(input_data)
    prediction = pipeline.predict(input_data)
    st.subheader("Predicted Price")
    st.success(f" £ {prediction[0]:,.2f}")
        
    st.success("Prediction Completed Successfully")
    st.toast("Prediction Completed Successfully")
