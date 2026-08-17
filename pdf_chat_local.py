import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.chains import ConversationalRetrievalChain

st.set_page_config(page_title="PDF Chatbot (Local LLM)", layout="centered")
st.title("📄 Chat with your PDF (Local LLM)")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    loader = PyPDFLoader("temp.pdf")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(chunks, embeddings)

    llm = Ollama(model="mistral")

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm,
        retriever=db.as_retriever(search_kwargs={"k": 3})
    )

    user_query = st.text_input("Ask a question from the PDF:")

    if user_query:
        result = qa_chain({
            "question": user_query,
            "chat_history": st.session_state.chat_history
        })

        st.session_state.chat_history.append((user_query, result["answer"]))

        for q, a in st.session_state.chat_history:
            st.markdown(f"**You:** {q}")
            st.markdown(f"**Bot:** {a}")
