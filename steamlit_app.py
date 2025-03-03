import streamlit as st
import requests

st.title("FastAPI and Streamlit Integration")

response = requests.get("http://127.0.0.1:8000/")
data = response.json()

st.write(data)
