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
st.write("Generate strong and random passwords effortlessly.")

# Main input section
st.subheader("Configuration")

# Use a slider or number input as requested (1 to 30)
length = st.slider("Select Password Length:", min_value=1, max_value=30, value=12)

# Button to generate
if st.button("Generate Password", type="primary"):
    password = generate_password(length)
    
    # Display the result
    st.success("Your password has been generated!")
    st.code(password, language="text")
    
    # Information about the password
    if length >= 4:
        st.info("This password includes Uppercase, Lowercase, Numbers, and Special characters.")
    else:
        st.warning("Passwords shorter than 4 characters may not include all character types.")

# Footer
st.markdown("---")
st.markdown("Created for **synent-task4-password-generator-assistant-Siyamkhize**")
