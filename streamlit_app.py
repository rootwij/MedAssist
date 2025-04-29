import streamlit as st
import requests

st.set_page_config(page_title="MedAssist - Symptom Checker", layout="centered")
st.title("🩺 MedAssist: Symptom Checker")

st.markdown("Enter your symptoms and get a doctor recommendation with confidence score.")

user_input = st.text_area("Describe your symptoms:", placeholder="e.g., I have tightness in my chest and trouble breathing")

if st.button("Get Recommendation") and user_input.strip():
    with st.spinner("Analyzing your symptoms..."):
        response = requests.post("https://medassist-301f.onrender.com/route", json={"text": user_input})
        st.success("Result")
        st.write(response.json()["intent"])
