import streamlit as st
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

st.markdown("# Summarize Top 5 Hackerank Articles with Phi-3 :sparkles: ")

azure_url = "https://models.inference.ai.azure.com/chat/completions"
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
posts_urls = [post['url'] for post in posts]

# for each post get the 'kids' and make a request for each comment into a string
comments_per_post = {}
for post in posts:
    comments_per_post[post['url']] = []
    children_comments = []
    if 'kids' in post.keys():
        kids = post['kids']
        for kid in kids:
            comment = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{kid}.json").json()
            if 'text' in comment.keys():
                children_comments.append(comment['text']) 
    comments_per_post[post['url']] = ''.join(children_comments)[:32000] #8000 token limit
           
st.write('top 5 Hackerank Articles')
def get_summary(article_url):


    article_text = comments_per_post[article_url]
    data = {
        "messages": [
            {"role": "system", "content": "Summarize the comments into 5 bullet points the report the overall sentiment for the comments."},
            {"role": "user", "content": article_text
            },
        ],
        "model": "Phi-3-medium-128k-instruct"
    }

    response = requests.post(azure_url, headers=headers, json=data)
    data = response.json()
    return data['choices'][0]['message']['content']

for hn_url in posts_urls:
   
    st.markdown(f'- {hn_url}')
    st.markdown(f'  {get_summary(hn_url)}')


