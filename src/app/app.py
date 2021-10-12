import streamlit as st
import example

st.title('Hello world')
nmbr = st.slider('choose one',0,5,2)
st.markdown('\n')
st.markdown('\n')
st.markdown('\n')
st.write(example.add_one(nmbr))