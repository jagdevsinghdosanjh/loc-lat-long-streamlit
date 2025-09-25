import streamlit as st
from auth.login import authenticate_user
from auth.roles import get_user_role

# Set page config first
st.set_page_config(page_title="Location Dashboard", layout="wide")

# Authenticate user
if authenticate_user():
    st.success(f"Welcome, {st.session_state.role}!")
    st.markdown("Use the sidebar to navigate.")
else:
    st.stop()

# Main dashboard title
st.title("🧭 Location Lookup Dashboard")

# Get role from session
role = get_user_role()

# Role-based messaging
if role == "Coordinator":
    st.success("Welcome, Coordinator! You have full access to all tools.")
    st.markdown("- Use the sidebar to navigate between lookup, batch tools, exports, and diagnostics.")
elif role == "Student":
    st.info("Welcome, Student! You can use single and batch lookup tools.")
    st.markdown("- Export history and diagnostics are restricted.")
else:
    st.warning("Role not recognized. Limited access granted.")
    st.markdown("- Please contact your coordinator for full access.")
