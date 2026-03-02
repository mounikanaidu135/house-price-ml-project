import streamlit as st
import requests

st.title("House Price Prediction")

area = st.number_input("Area (sqft)")
bedrooms = st.number_input("Bedrooms")
age = st.number_input("House Age")

if st.button("Predict Price"):

    response = requests.post(
        "http://localhost:5000/predict",
        json={
            "area": area,
            "bedrooms": bedrooms,
            "age": age
        }
    )

    result = response.json()

    st.success(f"Predicted Price: {result['predicted_price']}")