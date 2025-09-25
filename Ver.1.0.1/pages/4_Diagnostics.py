import streamlit as st
import os

st.title("🧪 Diagnostic Logs")
log_path = "logs/diagnostics.log"

if os.path.exists(log_path):
    with open(log_path) as f:
        st.text(f.read())
else:
    st.info("No diagnostics logged yet.")
