import streamlit as st
import time


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
    import pyvista as pv
    from stpyvista import stpyvista

    from stpyvista.utils import start_xvfb

    if "IS_XVFB_RUNNING" not in st.session_state:
      start_xvfb()
      st.session_state.IS_XVFB_RUNNING = True

    ## Initialize a plotter object
    plotter = pv.Plotter(window_size=[400,400])

    ## Create a mesh with a cube 
    mesh = pv.Cube(center=(0,0,0))

    ## Add some scalar field associated to the mesh
    mesh['myscalar'] = mesh.points[:, 2] * mesh.points[:, 0]

    ## Add mesh to the plotter
    plotter.add_mesh(mesh, scalars='myscalar', cmap='bwr')

    ## Final touches
    plotter.view_isometric()
    plotter.background_color = 'white'

    ## Send to streamlit
    stpyvista(plotter, key="pv_cube")
