import streamlit as st
import time
from utils.functions import viewer
from ansys.simai.core import SimAIClient


st.title("⚗️ Prediction")

PROJECT_NAME = st.selectbox(
    "Project",
    (i.name for i in st.session_state["client"].projects.list()),
    key="simai_project"
)
project = st.session_state["client"].projects.get(name=PROJECT_NAME)

WORKSPACE_NAME = st.selectbox(
    "Workspace",
    (i.name for i in project.workspaces()),
    key="simai_workspace"
)
workspace = st.session_state["client"].workspaces.get(name=WORKSPACE_NAME)

choice = st.radio(
    "Choice",
    (
        "Upload a new file",
        "Use existing file",
        "Generate a new file"
    ),
)

if choice == "Upload a new file":
    st.file_uploader("Geometry")
    st.success("File successfully uploaded")

elif choice == "Use existing file":
    GEOMETRY_NAME = st.selectbox(
        "Geometry",
        (i.name for i in st.session_state["client"].geometries.list(workspace=workspace)),
    )
    geometry = st.session_state["client"].geometries.get(name=GEOMETRY_NAME)

elif choice == "Generate a new file":
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
