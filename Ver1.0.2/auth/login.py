import streamlit as st

def authenticate_user():
    st.sidebar.title("🔐 Login")

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    # Define roles and passwords manually
    users = {
        "coordinator": {"password": "honor123", "role": "Coordinator"},
        "student": {"password": "green123", "role": "Student"}
    }

    if st.sidebar.button("Login"):
        if username in users and password == users[username]["password"]:
            st.session_state.username = username
            st.session_state.role = users[username]["role"]
            st.success(f"Welcome, {st.session_state.role}!")
            return True
        else:
            st.error("Invalid username or password")
            return False

    # If already logged in
    if "role" in st.session_state:
        st.sidebar.success(f"Logged in as {st.session_state.role}")
        return True

    return False
