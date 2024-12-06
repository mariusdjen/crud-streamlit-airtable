import streamlit as st

class HomePage:
    def  display(self):
        st.title("Bonjour") 
        st.write("<p style='color:red'> Marius</p>", unsafe_allow_html=True)
