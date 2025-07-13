import streamlit as st
import pandas as pd

st.set_page_config(page_title="🦷 Periodontal Stage Predictor", layout="wide")
st.title("🦷 Periodontal Disease Stage Prediction")
st.markdown("Enter patient data below to predict the periodontal disease stage. *(This version simulates prediction for testing.)*")

# Define feature names
feature_names = ['HbA1c', 'BMI', 'TG', 'Chol', 'AGE', 'HDL', 'LDL',
                 'Urea', 'Creatinine', 'Cr', 'Gender', 'CLASS']

st.header("📝 Patient Data Input")
with st.form("patient_form"):
    hba1c = st.number_input("HbA1c (%)", 0.0, 15.0, 5.0, step=0.1)
    bmi = st.number_input("BMI", 10.0, 50.0, 25.0, step=0.1)
    tg = st.number_input("Triglycerides (TG, mg/dL)", 50.0, 500.0, 150.0)
    chol = st.number_input("Cholesterol (Chol, mg/dL)", 100.0, 400.0, 200.0)
    age = st.number_input("Age (years)", 5, 100, 35)
    hdl = st.number_input("HDL (mg/dL)", 10, 100, 40)
    ldl = st.number_input("LDL (mg/dL)", 10, 250, 100)
    urea = st.number_input("Urea (mg/dL)", 10, 100, 30)
    creatinine = st.number_input("Creatinine (mg/dL)", 0.1, 5.0, 1.0)
    cr = st.number_input("Creatinine Ratio (Cr)", 0.1, 5.0, 1.2)
    gender = st.selectbox("Gender", ['M', 'F'])
    class_val = st.selectbox("CLASS (Diabetes Status)", ['N', 'Y', 'P'])

    submitted = st.form_submit_button("🔍 Predict Stage")

if submitted:
    # Simulated prediction logic (based on HbA1c)
    if hba1c >= 8:
        predicted_stage = "Stage IV"
    elif hba1c >= 7:
        predicted_stage = "Stage III"
    elif hba1c >= 6:
        predicted_stage = "Stage II"
    elif hba1c >= 5.5:
        predicted_stage = "Stage I"
    else:
        predicted_stage = "Healthy"

    # Show result
    st.subheader("📊 Prediction Result")
    st.markdown(f"### 🧠 Predicted Periodontal Stage: `{predicted_stage}`")
    st.markdown("This is a simulated prediction based on HbA1c. Once your model files are ready, this will be replaced with real SVM predictions.")
