import streamlit as st
import pandas as pd
import time

# --- Page Setup ---
st.set_page_config(page_title="🦷 Periodontal Stage Predictor", layout="wide")
st.title("🦷 Periodontal Disease Stage Prediction")
st.markdown("Enter all patient data to get a predicted periodontal disease stage.")

# --- Session State Initialization ---
if "show_doctor" not in st.session_state:
    st.session_state.show_doctor = False

# --- Sample Input Guidelines ---
st.markdown("💡 **Example Input Guidelines:**")
st.markdown("""
- HbA1c: 5.5 – 7.5%  
- BMI: 18.5 – 29.9  
- TG: 100 – 200 mg/dL  
- Cholesterol: 150 – 250 mg/dL  
- HDL: 40 – 60 mg/dL  
- LDL: 100 – 160 mg/dL  
- Urea: 20 – 50 mg/dL  
- Creatinine: 0.8 – 1.4 mg/dL  
- Cr Ratio: 1.0 – 2.0  
- Gender: M / F  
- CLASS: N (Normal), Y (Yes), P (Pre-diabetic)
""")

# --- Form for Patient Input ---
st.header("📝 Patient Data Input")
with st.form("patient_form"):
    hba1c = st.number_input("HbA1c (%)", min_value=0.0, max_value=15.0, step=0.1, format="%.2f", placeholder="e.g., 5.6")
    bmi = st.number_input("BMI", min_value=0.0, max_value=60.0, step=0.1, format="%.2f", placeholder="e.g., 22.5")
    tg = st.number_input("Triglycerides (TG, mg/dL)", min_value=0.0, max_value=1000.0, step=0.1, format="%.2f", placeholder="e.g., 150")
    chol = st.number_input("Cholesterol (Chol, mg/dL)", min_value=0.0, max_value=600.0, step=0.1, format="%.2f", placeholder="e.g., 180")
    age = st.number_input("Age (years)", min_value=0, max_value=120, placeholder="e.g., 45")
    hdl = st.number_input("HDL (mg/dL)", min_value=0, max_value=200, placeholder="e.g., 50")
    ldl = st.number_input("LDL (mg/dL)", min_value=0, max_value=300, placeholder="e.g., 120")
    urea = st.number_input("Urea (mg/dL)", min_value=0, max_value=200, placeholder="e.g., 30")
    creatinine = st.number_input("Creatinine (mg/dL)", min_value=0.0, max_value=10.0, step=0.1, format="%.2f", placeholder="e.g., 1.1")
    cr = st.number_input("Creatinine Ratio (Cr)", min_value=0.0, max_value=10.0, step=0.1, format="%.2f", placeholder="e.g., 1.2")
    gender = st.selectbox("Gender", ["Select", "M", "F"])
    class_val = st.selectbox("CLASS (Diabetes Status)", ["Select", "N", "Y", "P"])

    submitted = st.form_submit_button("🔍 Predict Stage")

# --- Prediction Logic ---
if submitted:
    if gender == "Select" or class_val == "Select":
        st.error("Please select valid options for Gender and CLASS.")
    else:
        with st.spinner("Analyzing..."):
            time.sleep(1.5)

        # Dummy logic for prediction
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

        # Save to session state for sidebar
        report = f"""
🦷 Periodontal Disease Prediction Report

Predicted Stage: {predicted_stage}

Patient Info:
- HbA1c: {hba1c}%
- BMI: {bmi}
- TG: {tg}
- Cholesterol: {chol}
- Age: {age}
- HDL: {hdl}
- LDL: {ldl}
- Urea: {urea}
- Creatinine: {creatinine}
- Cr Ratio: {cr}
- Gender: {gender}
- CLASS: {class_val}
"""
        st.session_state.predicted_stage = predicted_stage
        st.session_state.report = report

# --- Sidebar: Next Steps ---
if "predicted_stage" in st.session_state:
    st.sidebar.header("🧾 Next Steps")

    st.sidebar.download_button(
        label="📄 Download Report",
        data=st.session_state.report,
        file_name="perio_report.txt"
    )

    if st.sidebar.button("👨‍⚕️ Check with Doctor"):
        st.session_state.show_doctor = True

    if st.session_state.show_doctor:
        st.sidebar.markdown("### 📍 Nearest Dental Specialist")
        st.sidebar.markdown("- **SmileCare Dental Clinic**, MG Road")
        st.sidebar.markdown("- 📞 +91-98765-43210")
        st.sidebar.markdown("- 📧 smilecare@example.com")
        st.sidebar.success("💬 You can share the downloaded report during your visit.")

