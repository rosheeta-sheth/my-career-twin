---
title: twin
app_file: app.py
sdk: gradio
sdk_version: 6.14.0
---

# Career Twin Chatbot

An AI chatbot that acts as a career assistant for my portfolio site. You can ask it about my background, projects, and skills — or leave your contact info if you want to get in touch.

🔗 **Live:** [https://twin-b6id.onrender.com](https://twin-b6id.onrender.com)

## What it does

- Answers questions about my experience and projects using my actual resume and write-ups (not hallucinated info)
- Uses semantic search to pull relevant context before responding
- Collects contact details from visitors and sends me a push notification via Pushover
- Suggests follow-up questions to keep the conversation going

## Stack

- Python + OpenAI API (gpt-4o-mini)
- Gradio for the UI
- Local vector search using text-embedding-3-small + cosine similarity for RAG
- PyPDF for parsing project documents

## Run locally

```bash
git clone https://github.com/rosheeta-sheth/my-career-twin.git
cd my-career-twin
pip install -r requirements.txt
```

Create a `.env` file:
```
OPENAI_API_KEY=your_key_here
PUSHOVER_USER=your_pushover_user_key
PUSHOVER_TOKEN=your_pushover_app_token
```

Then run:
```bash
python app.py
```

App will be at `http://localhost:7860`.
