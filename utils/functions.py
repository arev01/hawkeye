import streamlit as st
import pyvista as pv
from stpyvista import stpyvista

from stpyvista.utils import start_xvfb

@st.dialog
def viewer():

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
    plotter.background_color = 'black'

    ## Send to streamlit
    stpyvista(plotter, key="pv_cube")
