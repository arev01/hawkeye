import streamlit as st
import time
import pyvista as pv
import numpy as np
from stpyvista import stpyvista

from stpyvista.utils import start_xvfb

if "IS_XVFB_RUNNING" not in st.session_state:
  start_xvfb()
  st.session_state.IS_XVFB_RUNNING = True


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
        
st.button("Download", disabled=True)

## Create coordinate data
x = np.arange(-10, 10, 0.25)
y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

## Set up plotter
plotter = pv.Plotter(window_size=[600,600])
surface = pv.StructuredGrid(x, y, z)
plotter.add_mesh(surface, color='teal', show_edges=True)

## Pass the plotter (not the mesh) to stpyvista
stpyvista(plotter, key="surface")

