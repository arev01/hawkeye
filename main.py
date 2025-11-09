import streamlit as st
import time

from contextlib import contextmanager

HORIZONTAL_STYLE = """
<style class="hide-element">
    /* Hides the style container and removes the extra spacing */
    .element-container:has(.hide-element) {
        display: none;
    }
    /*
        The selector for >.element-container is necessary to avoid selecting the whole
        body of the streamlit app, which is also a stVerticalBlock.
    */
    div[data-testid="stVerticalBlock"]:has(> .element-container .horizontal-marker) {
        display: flex;
        flex-direction: row !important;
        flex-wrap: wrap;
        gap: 0.5rem;
        align-items: baseline;
    }
    /* Buttons and their parent container all have a width of 704px, which we need to override */
    div[data-testid="stVerticalBlock"]:has(> .element-container .horizontal-marker) div {
        width: max-content !important;
    }
    /* Just an example of how you would style buttons, if desired */
    /*
    div[data-testid="stVerticalBlock"]:has(> .element-container .horizontal-marker) button {
        border-color: red;
    }
    */
</style>
"""

@contextmanager
def st_horizontal():
    st.markdown(HORIZONTAL_STYLE, unsafe_allow_html=True)
    with st.container():
        st.markdown('<span class="hide-element horizontal-marker"></span>', unsafe_allow_html=True)
        yield

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

elif choice == "Use existing file":
    st.selectbox(
        "Geometry",
        ("Email", "Home phone", "Mobile phone"),
    )

elif choice == "Generate a new file":
    container = st.container(border=True)
    container.slider("Latent parameters", key="lp1")
    container.slider("Latent parameters", key="lp2")
    container.slider("Latent parameters", key="lp3")

st.text_input("Boundary conditions")

with st_horizontal():
    if st.button("Predict"):
        with st.spinner("Wait for it..."):
            time.sleep(5)
            
    st.button("Download", disabled=True)
