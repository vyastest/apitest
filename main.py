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


#prompt = "the massage was really good and reception guys sunil and imran very polite and they understand what customer requirements are my back was paining so they suggested me to take aroma massage it was relaxing.  massage was amazing super..Please summarise the sentence in 8 words"
#model = "text-davinci-003"
#response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=50)

#generated_text = response.choices[0].text
#st.write(generated_text)

from langchain.llms import OpenAI
#from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain.agents import create_csv_agent


import pandas as pd

# Create the Streamlit app
def main():
    st.title("CSV Agent App")

    # Create the agent
    agent = create_csv_agent(
        OpenAI(temperature=0),
        path="teststream.csv",  # Replace with the actual file path
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
    )

    # Get user input
    user_input = st.text_input("Enter your question:", "")

    if st.button("Ask"):
        # Run the agent based on user input
        response = agent.run(user_input)
        st.write("Agent's response:", response)

if __name__ == "__main__":
    main()
