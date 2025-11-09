import streamlit as st
import time

project =st.selectbox("Project")
workspace = st.selectbox("Wokspace")
choice = st.radio("Choice",
    [
    "Upload a new file",
    "Use existing file",
    "Generate a new file"]
)

if choice == "Upload a new file":
    st.file_uploader("")

elif choice == "Use existing file":
    st.selectbox("Geometry")

elif choice == "Generate a new file":
    st.selectbox("Project")
    st.selectbox("Workspace")

    st.slider("Latent parameters")

st.text_input("Boundary conditions")

with st.button("Predict"):
    st.spinner("Wait for it..."):
    time.sleep(5)

st.button("Download", disabled=True)
