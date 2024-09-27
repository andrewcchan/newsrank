import streamlit as st

st.write("Hello, World!")

import requests

url = "https://models.inference.ai.azure.com/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + st.secrets["GITHUB_MODEL_API"]
}
data = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
    ],
    "model": "Phi-3-medium-128k-instruct"
}

response = requests.post(url, headers=headers, json=data)
st.write(response.json())

