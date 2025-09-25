import streamlit as st

def get_user_role():
    if "role" not in st.session_state:
        st.session_state.role = None

    roles = ["Coordinator", "Student"]
    selected = st.selectbox("Select your role:", roles)
    st.session_state.role = selected
    return selected
