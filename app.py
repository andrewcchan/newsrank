import streamlit as st
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

st.markdown("# Summarize Top 5 Hackerank Articles with Phi-3 :sparkles: ")

url = "https://models.inference.ai.azure.com/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + st.secrets["GITHUB_MODEL_API"]
}
response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
ids = response.json()[:5]
posts = []
for id in ids:
    post = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json")
    posts.append(post.json())

# parse each post url
posts = [post['url'] for post in posts]
st.write('top 5 Hackerank Articles')
# markdown for each post in bullets
for post in posts:
    st.markdown(f'- {post}')


def get_summary(article_url):
    # use beautiful soup to get article text

    # dr = webdriver.Chrome()
    # dr.get("https://www.mobile.de/?lang=en")
    # article_text = BeautifulSoup(dr.page_source,"lxml")
    # article_text = bs4.BeautifulSoup(requests.get(article_url,headers={'User-Agent': 'Mozilla/5.0'}).text, "html.parser").get_text()

    article_text = "sdfsdfsdfsdf"
    st.write(article_text)
    data = {
        "messages": [
            {"role": "system", "content": "Summarize the user's input."},
            {"role": "user", "content": article_text
            },
        ],
        "model": "Phi-3-medium-128k-instruct"
    }

    response = requests.post(url, headers=headers, json=data)
    data = response.json()
    return data['choices'][0]['message']['content']

for url in posts:
   
    st.markdown(f'## {url}')
    st.write( get_summary(url))


