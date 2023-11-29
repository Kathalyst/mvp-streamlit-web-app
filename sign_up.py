import streamlit as st
import re

def is_valid_email(email):
    # Simple email validation using regex
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email)

def is_valid_password(password):
    # Password must be at least 8 characters and contain both letters and numbers
    return len(password) >= 8 and any(char.isalpha() for char in password) and any(char.isdigit() for char in password)

def sign_up():
    st.markdown('<style>h1 { color: #71eea8; font-family: "Karla", sans-serif; }</style>', unsafe_allow_html=True)
    st.header("Sign Up")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if not is_valid_email(email):
            st.error("Please enter a valid email address.")
        elif not is_valid_password(password):
            st.error("Password must be at least 8 characters long and contain both letters and numbers.")
        elif password != confirm_password:
            st.error("Passwords do not match.")
        else:
            # Add your sign-up logic here
            st.success("Account created successfully!")

            # Redirect to a different page after sign-up
            #redirect_html = f'<script>window.location.href="http://localhost:8502/"</script>'
            #st.components.v1.html(redirect_html)
            st.markdown("### [Click here to unloack the experience!](http://localhost:8502/)")  # Replace "your_dashboard_url" with the actual URL


def sign_in():
    st.markdown('<style>h1 { color: #71eea8; font-family: "Karla", sans-serif; }</style>', unsafe_allow_html=True)
    st.header("Sign In")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Log In"):
        if not is_valid_email(email):
            st.error("Please enter a valid email address.")
        elif not is_valid_password(password):
            st.error("Invalid password. Password must be at least 8 characters long and contain both letters and numbers.")
        else:
            # Add your login logic here
            st.success("Logged in successfully!")

            # Redirect to a different page after login
            #redirect_html = f'<script>window.location.href="http://localhost:8502/"</script>'
            #st.components.v1.html(redirect_html)
            st.markdown("### [Click here to unloack the experience!](http://localhost:8502/)")  # Replace "your_dashboard_url" with the actual URL


def main():
    st.markdown('<style>h1 { color: #71eea8; font-family: "Poppins", sans-serif; }</style>', unsafe_allow_html=True)
    st.title("Welcome to Kathalyt!")

    # Display toggle buttons
    selected_option = st.radio("Choose an option:", ["Sign Up", "Log In"])

    # Show appropriate screen based on selected option
    if selected_option == "Sign Up":
        sign_up()
    elif selected_option == "Log In":
        sign_in()

if __name__ == "__main__":
    main()
