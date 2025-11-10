actual_email = "email"
actual_password = "password"

# Insert a form in the sidebar
with st.form("Login"):
    st.markdown("#### Enter your credentials")
    
    tenant = st.text_input("Tenant")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if submit and ( email == actual_email and password == actual_password ):
    # If the form is submitted and the email and password are correct,
    # Display a success message
    st.success("Login successful")
    
elif submit and ( email != actual_email or password != actual_password ):
    st.error("Login failed")
    
else:
    pass
