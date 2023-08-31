import openai
import streamlit as st

# Add sidebar content
st.sidebar.title("ChatGPT-")
#st.sidebar.markdown("This app demonstrates a ChatGPT-like clone using Streamlit and the OpenAI API.")
#st.sidebar.markdown("Enter your OpenAI API Key in the input field on the sidebar to get started.")

# Request API Key in the sidebar
#api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

openai.api_key = SECRET_API_KEY

prompt = "the massage was really good and reception guys sunil and imran very polite and they understand what customer requirements are my back was paining so they suggested me to take aroma massage it was relaxing.  massage was amazing super..Please summarise the sentence in 8 words"
model = "text-davinci-003"
response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=50)

generated_text = response.choices[0].text
st.write(generated_text)
