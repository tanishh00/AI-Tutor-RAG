from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def process_text(text):
    if not text.strip():
        raise ValueError("❌ No text found in PDF")

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=700,
        chunk_overlap=100
    )

    chunks = text_splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    knowledge_base = FAISS.from_texts(chunks, embeddings)

    return knowledge_base