
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load the API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

st.set_page_config(page_title="Chatbot", page_icon="💬")
st.title("🧠 AI Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful, friendly AI assistant that gives short, clear answers."}
    ]

# Display past messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Input box
user_input = st.chat_input("Ask something")

if user_input:
    # Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content

    # Show assistant response
    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
