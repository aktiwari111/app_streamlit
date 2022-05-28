import streamlit as st

st.write("""
# Welcome To GLA University...
""")

st.write("""
## Superstar Amir Khan
""")
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


eq = st.text_input('Calculator')
print(type(eq),eq)
st.write('The current number is ', eval(eq))
