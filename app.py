import streamlit as st

st.markdown("# Summarize Top 5 Hackerank Articles :sparkles: ")

import requests

url = "https://models.inference.ai.azure.com/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + st.secrets["GITHUB_MODEL_API"]
}
data = {
    "messages": [
        {"role": "system", "content": "Summarize the user's input."},
        {"role": "user", "content": """
        support systems shows that six out of nine of these crucial processes have crossed their “planetary boundary.” These boundaries are not tipping points—it’s possible to recover from passing them—but they are thresholds signifying we’ve entered higher-risk territory.

On another worrying note, scientists found the planet is close to breaching a seventh planetary boundary: ocean acidification.


In its first edition, a report from the Potsdam Institute for Climate Impact Research (PIK) used years of data and assessments to evaluate the nine planetary boundaries. These life-support systems make Earth resilient and stable. Alarmingly, six of those boundaries have already been crossed, as a similar assessment last year also concluded. The new report adds to that finding, suggesting these six metrics are now moving further into the “red zone,” or what the researchers consider a high-risk zone.

“The overall diagnostic is that the patient, Planet Earth, is in critical condition,” says Johan Rockström, PIK director and pioneer of the Planetary Boundaries Framework, in a statement.

Boundaries that have already been exceeded have to do with climate change, freshwater availability, biodiversity, land use, nutrient pollution (such as phosphorus and nitrogen) and the introduction of synthetic chemicals and plastics to the environment.

Ocean acidification is one of the systems that has not yet crossed its planeta"""
        },
    ],
    "model": "Phi-3-medium-128k-instruct"
}

response = requests.post(url, headers=headers, json=data)
data = response.json()
st.markdown('## [Article #1](https://news.ycombinator.com/)')
st.write(data['choices'][0]['message']['content'])
st.markdown('## [Article #2](https://news.ycombinator.com/)')
st.write(data['choices'][0]['message']['content'])

