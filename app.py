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
st.write("Generate high-entropy passwords with custom character sets and security levels.")

# Sidebar for Character Selection
st.sidebar.header("Character Sets")
include_upper = st.sidebar.checkbox("Uppercase (A-Z)", value=True)
include_lower = st.sidebar.checkbox("Lowercase (a-z)", value=True)
include_numbers = st.sidebar.checkbox("Digits (0-9)", value=True)
include_special = st.sidebar.checkbox("Special Characters (!@#$%^&*...)", value=True)

# Main input section
st.subheader("Security Level")

# Mode Selection
mode = st.radio(
    "Select Password Strength Mode:",
    ["Strong", "Super Strong"],
    help="Strong: Includes selected character types. Super Strong: Forces multiple characters of each selected type."
)

st.subheader("Configuration")

# Calculate min length based on selections
selected_count = sum([include_upper, include_lower, include_numbers, include_special])
if selected_count == 0:
    st.error("Please select at least one character set from the sidebar!")
    st.stop()

min_len = selected_count * 2 if mode == "Super Strong" else 1
default_len = max(12, min_len)

length = st.slider(
    "Select Password Length:", 
    min_value=1, 
    max_value=30, 
    value=default_len,
    help=f"Super Strong mode with current selection requires at least {min_len} characters."
)

# Visual Strength Indicator
strength_score = 0
if length > 8: strength_score += 1
if length > 12: strength_score += 1
if length > 16: strength_score += 1
if mode == "Super Strong": strength_score += 1
if selected_count == 4: strength_score += 1

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
    password = generate_password(
        length, mode, 
        include_upper, include_lower, include_numbers, include_special
    )
    
    # Display the result
    st.success(f"Your {mode} password has been generated!")
    st.code(password, language="text")
    
    # Information about the password
    st.info(f"Generated using: {'Uppercase, ' if include_upper else ''}{'Lowercase, ' if include_lower else ''}{'Numbers, ' if include_numbers else ''}{'Special' if include_special else ''}")

# Footer
st.markdown("---")
st.markdown("Created for **synent-task4-password-generator-assistant-Siyamkhize**")
