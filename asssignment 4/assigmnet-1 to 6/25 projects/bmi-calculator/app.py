import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="🧮")

st.title("BMI Calculator 🧮")

# User input
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (cm):", min_value=1.0, step=0.1)

# Calculate BMI
if weight and height:
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    st.write(f"### Your BMI is: `{bmi:.2f}`")

    # Health status
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You are healthy.")
    elif 25 <= bmi < 29.9:
        st.info("You are overweight.")
    else:
        st.error("You are obese.")
