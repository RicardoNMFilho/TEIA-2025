# core/loader.py
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from .llm import llm, embeddings
import streamlit as st

def adicionar_pdf(caminho_pdf):
    nome_pdf = os.path.basename(caminho_pdf)
    if nome_pdf in st.session_state.faiss_docs:
        return

    loader = PyPDFLoader(caminho_pdf)
    pages = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = splitter.split_documents(pages)

    st.session_state.faiss_docs[nome_pdf] = FAISS.from_documents(docs, embeddings)

    texto = "\n".join([doc.page_content for doc in pages])[:3000]
    prompt = f"Resuma em até duas frases sobre o que trata o seguinte documento:\n\n{texto}"
    descricao = llm.invoke(prompt).content.strip()

    doc_desc = Document(page_content=descricao, metadata={"nome_pdf": nome_pdf})
    st.session_state.descricoes_pdf.append(doc_desc)
    st.session_state.faiss_descricoes = FAISS.from_documents(
        st.session_state.descricoes_pdf, embeddings
    )
