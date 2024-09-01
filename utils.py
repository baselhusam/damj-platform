import streamlit as st

def new_line(n=1):
    for _ in range(n):
        st.write('\n')

def mid_col(streamlit_component):
    col1, col2, col3 = st.columns([1,0.5,1])
    with col2:
        return streamlit_component