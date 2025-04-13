import re
import streamlit as st

st.set_page_config(page_title="Password Strength Checker By Aqsa Iqbal", page_icon="🔮", layout="centered")

# Custom Styling
st.markdown("""
    <style>
    .password-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 30px;
       
    }
    .stTextInput, .stButton {
        width: 60% !important;
        margin: 10px auto;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        padding: 10px;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h2 style='text-align:center;'>🔐 Password Strength Checker</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Enter your password below to check its security level. 🔍</p>", unsafe_allow_html=True)

# Spacer
st.markdown("###")

# Input Field
password = st.text_input("🔑 Enter your password:", type="password", help="Make sure your password is strong.")

# Function to check strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include **both uppercase (A-Z) and lowercase (a-z)** letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one number (0–9)**.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*)**.")

    # Show result
    if score == 4:
        st.success("✅ **Strong Password** – Your password is secure and ready to go! 🚀")
    elif score == 3:
        st.info("⚠ **Moderate Password** – Almost there! Just a little improvement needed.")
    else:
        st.error("❌ **Weak Password** – Your password needs improvement.")

    # Show feedback
    if feedback:
        with st.expander("🔍 Tips to Improve Your Password"):
            for tip in feedback:
                st.write(tip)

# Button Trigger
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠ Please enter a password first!")
