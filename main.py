import openai
import streamlit as st
import os
import pandas as pd
df=pd.read_csv("teststream.csv")

# Add sidebar content
st.sidebar.title("ChatGPT-")
#st.sidebar.markdown("This app demonstrates a ChatGPT-like clone using Streamlit and the OpenAI API.")
#st.sidebar.markdown("Enter your OpenAI API Key in the input field on the sidebar to get started.")

# Request API Key in the sidebar
#api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

openai.api_key = st.secrets["my_api_key"]

question="Which striker had the most total runs_off_bat?"
prompt = f"Dataset:\n{df}\nQuestion: {question}\nInsights:"

model = "text-davinci-003"
response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=100)

generated_text = response.choices[0].text
st.write(generated_text)

