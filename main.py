import openai
import streamlit as st
import os

# Add sidebar content
st.sidebar.title("ChatGPT-")
#st.sidebar.markdown("This app demonstrates a ChatGPT-like clone using Streamlit and the OpenAI API.")
#st.sidebar.markdown("Enter your OpenAI API Key in the input field on the sidebar to get started.")

# Request API Key in the sidebar
#api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

openai.api_key = st.secrets["my_api_key"]

data=pd.read_csv("teststream.csv")
question="which striker has the most runs off bat?"
prompt = f"Dataset:\n{data}\nQuestion: {question}\nInsights:"

#prompt = "india are the best team in cricket and have played strong games in past 10 years winning in all countries home and away..Please summarise the sentence in 8 words"
model = "text-davinci-003"
response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=50)

generated_text = response.choices[0].text
st.write(generated_text)

