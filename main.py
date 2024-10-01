import streamlit as st

st.title('This is a title')

st.write('This is a simple **text** :books:')

st.button('Reset', type = "primary")
if st.button('Say Hello'):
  st.write("Why Hello Thereee")
else:
  st.write("Goodbye")
