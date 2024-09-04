"""
Utility Module
"""
import streamlit as st

def new_line(no_lines=1):
    """Create a new line in the Streamlit app."""
    for _ in range(no_lines):
        st.write('\n')
