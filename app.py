import streamlit as st

st.write("""
# Welcome To GLA University...
""")

"""
## Superstar Amir Khan
"""
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


eq = st.text_input('Calculator')
st.write('The current number is '+ str(eval( str(eq))))
