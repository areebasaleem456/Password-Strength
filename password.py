import re
import streamlit as st

#page styling
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒", layout="centered")

st.title("🔒 Password Strength Checker")
st.write("This app checks the strength of your password and provides suggestions to make it stronger 🔍")

#Function to check password strenhth
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password)>=8:
        score +=1
    else:
        feedback.append("❌ Password should be **atleast 8 characters long**") 
    
    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score +=1
    else:
        feedback.append("❌ Password should contain **both uppercase (A-Z) and lowercase (a-z) letters**")
    if re.search(r"\d",password):
        score +=1
    else:
        feedback.append("❌ Password should contain **numbers (0-9)**")
    
    if re.search(r"[!@#$%^&*]",password):
        score +=1
    else:
        feedback.append("❌ Password should contain **special characters (!@#$%^&*)**")

    #display password strength
    if score== 4:
        st.success("✅ **Strong password!** - Your password is secure 🔒")
    elif score ==3:
        st.info("⚠️ **Medium strength password** - Your password is secure but can be improved 🔐")
    else:
        st.error("❌ **Weak password!** - Your password is not secure. Please update it 🔓")

    #feedback
    if feedback:
        with st.expander("Improvement Suggested"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong 🔐")

#button working
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
