import streamlit as st
import ansys.simai.core

st.title("🔑 Authentication")

# Insert a form
with st.form("Login"):
    st.markdown("#### Enter your credentials")
    
    my_organization = st.text_input("Organization", placeholder="eg. ansys")
    my_username = st.text_input("Username")
    my_password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if submit:
    try:
        simai = ansys.simai.core.SimAIClient(
            organization=my_organization,
            credentials={
                # neither of these are required, but if they are missing you will be
                # prompted to input them
                "username": my_username,
                "password": my_password,
            },
        )
        simai.wait()        
        st.success("Login successful")

        st.session_state["simai"] = simai

    except:
        st.error("Login failed")
    
else:
    pass
