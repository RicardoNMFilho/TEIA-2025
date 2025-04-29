# core/llm.py
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain.prompts import PromptTemplate

llm = ChatOllama(model="llama3.1:8b")
embeddings = OllamaEmbeddings(model="nomic-embed-text")

retriever_prompt = PromptTemplate.from_template(
    """Dado o histórico de conversa e a nova pergunta, reformule a pergunta para uma busca em documentos.

Histórico:
{chat_history}

Nova pergunta: {input}"""
)

qa_prompt = PromptTemplate.from_template(
    """Você é um assistente útil que responde com base nos documentos fornecidos.

Contexto:
{context}

Pergunta: {input}"""
)
