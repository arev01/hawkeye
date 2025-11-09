import streamlit as st
import time
from utils import functions.viewer


simai_project = st.selectbox(
    "Project",
    ("Email", "Home phone", "Mobile phone"),
    key="simai_project"
)

simai_workspace = st.selectbox(
    "Workspace",
    ("Email", "Home phone", "Mobile phone"),
    key="simai_workspace"
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
    with st.container(border=True):
    
        st.markdown("#### Generate new design")
    
        geomai_project = st.selectbox(
            "Project",
            ("Email", "Home phone", "Mobile phone"),
            key="geomai_project"
        )
        
        geomai_workspace = st.selectbox(
            "Workspace",
            ("Email", "Home phone", "Mobile phone"),
            key="geomai_workspace"
        )
        
        st.slider("Latent parameters", key="lp1")
        st.slider("Latent parameters", key="lp2")
        st.slider("Latent parameters", key="lp3")
        
        st.button("Generate")

st.text_input("Boundary conditions")

if st.button("Predict"):
    with st.spinner("Wait for it..."):
        time.sleep(5)
        
if st.button("Download"):
    viewer()
