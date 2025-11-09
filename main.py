import streamlit as st
import time

st.title("👋 Welcome to hawkeye!")

st.markdown("A Graphical User Interface (GUI) built around [PySimAI](https://simai.docs.pyansys.com).")

actual_email = "email"
actual_password = "password"

# Insert a form in the sidebar
with st.sidebar.form("Login"):
    st.markdown("#### Enter your credentials")
    organization = st.text_input("Organization")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if submit and ( email == actual_email and password == actual_password ):
    # If the form is submitted and the email and password are correct,
    # Display a success message
    st.sidebar.success("Login successful")
elif submit and ( email != actual_email or password != actual_password ):
    st.sidebar.error("Login failed")
else:
    pass

project =st.selectbox(
    "Project",
    ("Email", "Home phone", "Mobile phone"),
)
workspace = st.selectbox(
    "Workspace",
    ("Email", "Home phone", "Mobile phone"),
)
geometry = st.radio(
    "Geometry",
    (
        "Upload a new file",
        "Use existing file",
        "Generate a new file"
    ),
)

if geometry == "Upload a new file":
    st.file_uploader("")

elif geometry == "Use existing file":
    st.selectbox(
        "",
        ("Email", "Home phone", "Mobile phone"),
    )

elif geometry == "Generate a new file":
    container = st.container(border=True)
    st.markdown("#### Generate new design")
    container.slider("Latent parameters", key="lp1")
    container.slider("Latent parameters", key="lp2")
    container.slider("Latent parameters", key="lp3")
    if container.button("Generate"):
        with st.spinner("Wait for it..."):
            time.sleep(5)
    container.button("Download", disabled=True)

st.text_input("Boundary conditions")

if st.button("Predict"):
    with st.spinner("Wait for it..."):
        time.sleep(5)
st.button("Download", disabled=True)

