import streamlit as st
from ansys.simai.core import SimAIClient


st.title("🔐 Authentication")

# Insert a form
with st.form("Login"):
    st.markdown("#### Enter your credentials")
    
    ORG_NAME = st.text_input("Organization", placeholder="eg. ansys")
    USERNAME = st.text_input("Username")
    PASSWORD = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if submit:
    try:
        client = SimAIClient(
            organization=ORG_NAME,
            credentials={
                # neither of these are required, but if they are missing you will be
                # prompted to input them
                "username": USERNAME,
                "password": PASSWORD,
            },
        )
        simai.wait()        
        st.success("Login successful")

        st.session_state["client"] = client

    except:
        st.error("Login failed")
    
else:
    pass
