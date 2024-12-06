import os
from dotenv import load_dotenv
from pyairtable import Table
import streamlit as st

#  load env variables
load_dotenv()
# Variables d'environnement
AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
BASE_ID = os.getenv("BASE_ID")
TABLE_NAME = os.getenv("TABLE_NAME")

#connecte to my table
table = Table(AIRTABLE_API_KEY,BASE_ID,TABLE_NAME)


def createContact(name:str,email:str,phone:str,message:str):  
   
    data = {
        "name": name,
        "email": email,
        "phoneNumber": phone,
        "message": message,
    }
        
    try :
        response  =  table.create(data) 
        return response
    except Exception as e :
        st.toast(f"Error adding record")
       

 


       

  