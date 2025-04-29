import os
import streamlit as st
from core.loader import adicionar_pdf
from core.responder import responder
from state.session import init_session

st.title("📄 Chat com PDFs (Local + Ollama)")

init_session()

uploaded_file = st.file_uploader("Suba um PDF", type=["pdf"])
if uploaded_file:
    path = os.path.join("tmp", uploaded_file.name)
    os.makedirs("tmp", exist_ok=True)
    with open(path, "wb") as f:
        f.write(uploaded_file.read())
    adicionar_pdf(path)
    st.success(f"PDF '{uploaded_file.name}' carregado com sucesso!")

pergunta = st.text_input("Pergunte algo:")
if pergunta:
    if not st.session_state.faiss_descricoes:
        st.warning("Envie pelo menos um PDF primeiro.")
    else:
        resposta, origem = responder(pergunta)
        st.markdown(f"**Resposta com base no PDF: _{origem}_**")
        st.markdown(resposta)

if st.checkbox("Mostrar histórico de conversa"):
    for msg in st.session_state.chat_history.messages:
        role = "🧑 Você" if msg.type == "human" else "🤖 Assistente"
        st.markdown(f"**{role}:** {msg.content}")