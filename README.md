---
title: twin
app_file: app.py
sdk: gradio
sdk_version: 6.14.0
---

# Rosheeta's Career Twin

Welcome to the repository for **Rosheeta's Career Twin** — an autonomous, agentic AI chatbot designed to act as my digital representative. It uses Retrieval-Augmented Generation (RAG) and function calling to answer questions about my background, skills, and projects, and even collect contact information for follow-ups!

🔗 **Live Demo:** [https://twin-b6id.onrender.com](https://twin-b6id.onrender.com)

## ✨ Key Features
- **Agentic AI Chatbot**: Grounded strictly in my personal career documents (resume, project write-ups).
- **RAG Knowledge Base**: Uses a local semantic search engine with `text-embedding-3-small` and cosine similarity to fetch precise context from markdown and PDF files.
- **Function Calling**: Equipped with tools to seamlessly log unanswered questions and securely capture interested visitors' contact details via push notifications (Pushover).
- **Interactive UI**: A sleek, responsive Gradio web application with a modern dark/light mode interface.

## 🛠️ Tech Stack
- **Backend**: Python, OpenAI API (`gpt-4o` or `gpt-4o-mini`)
- **Frontend**: Gradio (with custom CSS/HTML injection)
- **Data Processing**: PyPDF, NumPy (for embeddings and cosine similarity)

## 🚀 Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rosheeta-sheth/my-career-twin.git
   cd my-career-twin
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   PUSHOVER_USER=your_pushover_user_key (optional)
   PUSHOVER_TOKEN=your_pushover_app_token (optional)
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```
   Open `http://127.0.0.1:7860` in your browser.
