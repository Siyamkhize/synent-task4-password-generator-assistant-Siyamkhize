import streamlit as st
from password_generator import generate_password

# Page configuration
st.set_page_config(
    page_title="Secure Password Generator",
    page_icon="🔐",
    layout="centered"
)

# App title and description
st.title("🔐 Secure Password Generator")
st.write("Generate high-entropy passwords with custom security levels.")

# Main input section
st.subheader("Security Level")

# Mode Selection
mode = st.radio(
    "Select Password Strength Mode:",
    ["Strong", "Super Strong"],
    help="Strong: Includes all character types. Super Strong: Forces multiple characters of each type for higher diversity."
)

st.subheader("Configuration")

# Use a slider (1 to 30)
default_len = 12 if mode == "Strong" else 16
min_len = 1 if mode == "Strong" else 8

length = st.slider(
    "Select Password Length:", 
    min_value=min_len, 
    max_value=30, 
    value=default_len,
    help="Super Strong mode requires at least 8 characters."
)

# Visual Strength Indicator
strength_score = 0
if length > 8: strength_score += 1
if length > 12: strength_score += 1
if length > 16: strength_score += 1
if mode == "Super Strong": strength_score += 1

st.write("Current Security Score:")
if strength_score <= 1:
    st.error("⚠️ Basic")
elif strength_score == 2:
    st.warning("⚡ Good")
elif strength_score == 3:
    st.info("💪 Strong")
else:
    st.success("🔥 Super Strong")

# Button to generate
if st.button("Generate Password", type="primary"):
    password = generate_password(length, mode)
    
    # Display the result
    st.success(f"Your {mode} password has been generated!")
    st.code(password, language="text")
    
    # Information about the password
    if mode == "Super Strong":
        st.info("✅ Super Strong: Guaranteed multiple Uppercase, Lowercase, Numbers, and Special characters.")
    elif length >= 4:
        st.info("✅ Strong: Guaranteed at least one of each character type.")

# Footer
st.markdown("---")
st.markdown("Created for **synent-task4-password-generator-assistant-Siyamkhize**")
