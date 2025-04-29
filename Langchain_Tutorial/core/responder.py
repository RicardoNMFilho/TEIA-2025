# core/responder.py
import streamlit as st
from .chain import criar_chain

def responder(pergunta):
    resultado = st.session_state.faiss_descricoes.similarity_search(pergunta, k=1)[0]
    nome_pdf = resultado.metadata["nome_pdf"]
    retriever = st.session_state.faiss_docs[nome_pdf].as_retriever()
    chain = criar_chain(retriever)

    resposta = chain.invoke({
        "input": pergunta,
        "chat_history": st.session_state.chat_history.messages
    })

    st.session_state.chat_history.add_user_message(pergunta)
    st.session_state.chat_history.add_ai_message(resposta["answer"])

    return resposta["answer"], nome_pdf
