import streamlit as st
import os

if st.session_state.get("role") == "Coordinator":
    with open("logs/diagnostics.log") as f:
        st.text_area("🧪 Diagnostic Overlay", f.read(), height=300)

if st.session_state.get("role") != "Coordinator":
    st.warning("Access denied. This page is for Coordinators only.")
    st.stop()

st.title("🧪 Diagnostic Logs")
log_path = "logs/diagnostics.log"

if os.path.exists(log_path):
    with open(log_path) as f:
        st.text(f.read())
else:
    st.info("No diagnostics logged yet.")
