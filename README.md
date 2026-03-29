# AI-Tutor-RAG
AI Tutor using RAG with Groq API and Streamlit
## 🚀 Overview
This project is an AI-powered tutor that allows users to upload PDF documents and ask questions. The system retrieves relevant information from the document and generates context-aware answers using a Large Language Model.

## 🧠 Features
- 📂 Upload PDF documents
- 💬 Ask questions from your PDF
- 🧠 Context-based answers using RAG
- 📄 Generate summaries
- ⚡ Fast responses using Groq API

## ⚙️ Tech Stack
- Python
- Streamlit
- LangChain
- FAISS (Vector Database)
- Groq API (LLaMA 3.1 model)
- HuggingFace Embeddings

## 🔄 How It Works
1. Upload PDF  
2. Text is extracted  
3. Text is split into chunks  
4. Embeddings are created  
5. Stored in FAISS  
6. User asks question  
7. Relevant chunks retrieved  
8. Groq LLM generates answer  

## 🛠️ Installation

```bash
pip install -r requirements.txt
