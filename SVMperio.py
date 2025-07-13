import streamlit as st
import pandas as pd
import time

# Page setup
st.set_page_config(page_title="🦷 Periodontal Stage Predictor", layout="wide")
st.title("🦷 Periodontal Disease Stage Prediction")
st.markdown("Enter patient data below to predict the periodontal disease stage.")

# --- Session State to Track Doctor Button ---
if "show_doctor" not in st.session_state:
    st.session_state.show_doctor = False

# --- Sidebar Actions ---
st.sidebar.header("🧾 Next Steps")

# Show download button only after prediction
if "predicted_stage" in st.session_state:
    report_text = st.session_state.report_text
    st.sidebar.download_button("📄 Download Report", report_text, file_name="perio_prediction_report.txt")

    if st.sidebar.button("👨‍⚕️ Check with Doctor"):
        st.session_state.show_doctor = True

    if st.session_state.show_doctor:
        st.sidebar.markdown("### 📍 Nearest Dental Specialist")
        st.sidebar.markdown("- **SmileCare Dental Clinic**, MG Road")
        st.sidebar.markdown("- 📞 **+91-98765-43210**")
        st.sidebar.markdown("- 📧 **smilecare@example.com**")
        st.sidebar.success("💬 You can share the downloaded report during your visit.")
        st.sidebar.info("🧠 Tip: Ask about scaling, root planing, or antibiotics for advanced stages.")

# --- Patient Data Form ---
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

# --- Prediction Logic ---
if submitted:
    with st.spinner('Analyzing data and predicting...'):
        time.sleep(2)

    # Dummy logic for now
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

    
    st.subheader("📊 Prediction Result")
    st.success(f"🧠 Predicted Periodontal Stage: `{predicted_stage}`")

    report_text = f"""
🦷 Periodontal Disease Prediction Report

Predicted Stage: {predicted_stage}
------------------------------
Patient Data:
- HbA1c: {hba1c}%
- BMI: {bmi}
- TG: {tg}
- Chol: {chol}
- Age: {age}
- HDL: {hdl}
- LDL: {ldl}
- Urea: {urea}
- Creatinine: {creatinine}
- Cr: {cr}
- Gender: {gender}
- CLASS: {class_val}

⚠️ Please consult a dental professional for confirmation.
    """

    # Save state for sidebar access
    st.session_state.predicted_stage = predicted_stage
    st.session_state.report_text = report_text
