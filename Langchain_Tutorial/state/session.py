# state/session.py
import streamlit as st
from langchain_community.chat_message_histories import ChatMessageHistory

def init_session():
    if "faiss_docs" not in st.session_state:
        st.session_state.faiss_docs = {}
        st.session_state.descricoes_pdf = []
        st.session_state.faiss_descricoes = None
        st.session_state.chat_history = ChatMessageHistory()
