import streamlit as st
from groq import Groq
st.set_page_config(page_title = "AI Interview Assistant", page_icon = "🪷",layout='centered')
st.title("AI Interview Assistant")
st.caption("Practice and Prepare for your Placements here")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFoundError):
  st.error("API Key is missing. Add it in Advanced settings")
  st.stop()
role = st.selectbox("Job Title",['Machine Learning Engineer','AI Engineer','Senior Software Engineer','DevOps Engineer'])
if role == "Other":
  st.text_input('Enter your Job Title','xxxxxxxxx')
model = st.selectbox('Model',['openai/gpt-oss-120b','openai/gpt-oss-20b'])
level = st.selectbox('Level',['Beginner','intermediate','Advance'])
mode = st.radio('Activity',['Generate Questions','Generate code Questions','Evaluate Answers','Improve Answers'])
if mode == 'Generate Questions':
  count = st.slider(1,10,5)
