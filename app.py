import streamlit as st
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os

from groq import Groq
from utils import process_text

# Load env
load_dotenv()

# Initialize Groq
client = Groq(api_key="your_key_here")

st.set_page_config(page_title="AI Tutor", page_icon="📚")

st.title("📚 AI Tutor (RAG using Groq)")
st.write("Upload your PDF and ask questions!")

# Sidebar
st.sidebar.title("⚙️ Options")
option = st.sidebar.selectbox(
    "Choose Action",
    ["Ask Questions", "Generate Summary"]
)

# Upload PDF
pdf = st.file_uploader("Upload your PDF", type="pdf")

if pdf:
    pdf_reader = PdfReader(pdf)
    text = ""

    for page in pdf_reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    st.write(f"📄 Text loaded: {len(text)} characters")

    try:
        knowledge_base = process_text(text)

        # Function to get Groq response
        def get_groq_response(prompt):
            chat = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.1-8b-instant"

            )
            return chat.choices[0].message.content

        # 💬 Ask Questions
        if option == "Ask Questions":
            st.subheader("💬 Ask Questions")
            user_question = st.text_input("Enter your question")

            if user_question:
                docs = knowledge_base.similarity_search(user_question)

                prompt = f"""
                Answer the question using the context below.

                Context:
                {docs[0].page_content}

                Question:
                {user_question}
                """

                response = get_groq_response(prompt)

                if "history" not in st.session_state:
                    st.session_state.history = []

                st.session_state.history.append(("You", user_question))
                st.session_state.history.append(("AI", response))

                for role, msg in st.session_state.history:
                    st.write(f"**{role}:** {msg}")

        # 📄 Summary
        elif option == "Generate Summary":
            st.subheader("📄 Generate Summary")

            if st.button("Generate Summary"):
                summary = get_groq_response(
                    f"Summarize this:\n{text[:2000]}"
                )
                st.write(summary)

    except Exception as e:
        st.error(str(e))