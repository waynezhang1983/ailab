import streamlit as st
import requests

url='http://47.144.126.180:8000/message?q='

with st.sidebar:
    apikey = st.text_input("Intelity API Key", key="apikey", type="password")
    "Ask Wayne for get apikey if you are interested"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Say something")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("assistant"):
        data = {
            'question': f"{prompt}"
        }
        url = url + apikey

        response = requests.post(url, json=data)
        if response.status_code == 401:
            st.markdown("apikey is not registered")
            st.session_state.messages.append({"role": "assistant", "content": "apikey is not registered"})
        else:
            st.markdown(response.json()["answer"])
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response.json()["answer"]})