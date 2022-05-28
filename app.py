import streamlit as st

st.write("""
# Welcome To GLA University...
""")

"""
## Superstar Amir Khan
"""
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)
