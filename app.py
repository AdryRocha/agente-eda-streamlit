# app.py (Versão Final para Deploy no GitHub e Streamlit Cloud)

import streamlit as st
import pandas as pd
import os
import re
from agent_core import create_eda_agent

st.set_page_config(page_title="Agente Autônomo de EDA", page_icon="🤖", layout="wide")
st.title("🤖 Agente Autônomo para Análise Exploratória de Dados (EDA)")
st.caption("Faça upload de um arquivo CSV e converse com seus dados em linguagem natural.")

def extract_filepath(text: str):
    pattern = r"(plots/[a-zA-Z0-9_.\-]+\.png)"
    match = re.search(pattern, text)
    return match.group(1) if match else None

# --- Gerenciamento de Segredos (API Key) ---
# A chave da API será lida dos "Secrets" da plataforma Streamlit
try:
    GEMINI_API_KEY = st.secrets
except:
    st.error("Chave de API do Google Gemini não encontrada. Por favor, configure-a nos segredos da aplicação.")
    GEMINI_API_KEY = None

# Inicializa o estado da sessão
if "messages" not in st.session_state:
    st.session_state.messages = # <--- LINHA CORRIGIDA
if "agent_executor" not in st.session_state:
    st.session_state.agent_executor = None
if "dataframe" not in st.session_state:
    st.session_state.dataframe = None

with st.sidebar:
    st.header("Configuração")
    st.info("Esta aplicação utiliza o Google Gemini para análise.")
    
    uploaded_file = st.file_uploader("Carregue seu arquivo CSV", type="csv")
    
    if uploaded_file is not None:
        if st.button("Iniciar Análise"):
            if not GEMINI_API_KEY:
                st.stop()
            else:
                with st.spinner("Carregando dados e inicializando o agente..."):
                    try:
                        df = pd.read_csv(uploaded_file)
                        st.session_state.dataframe = df
                        
                        st.session_state.agent_executor = create_eda_agent(
                            df, 
                            "Google Gemini", 
                            GEMINI_API_KEY
                        )
                        
                        st.session_state.messages = [{"role": "assistant", "content": "Agente inicializado com Google Gemini. Estou pronto para analisar!"}]
                        st.success("Agente pronto!")
                    except Exception as e:
                        st.error(f"Ocorreu um erro: {e}")

    if st.session_state.dataframe is not None:
        st.markdown("### Preview dos Dados")
        st.dataframe(st.session_state.dataframe.head())

# O restante do código da interface de chat permanece o mesmo
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        filepath = extract_filepath(message["content"])
        if filepath and os.path.exists(filepath):
            clean_content = re.sub(r"\s*e salvo em:.*\.png", "", message["content"])
            st.markdown(clean_content)
            st.image(filepath)
        else:
            st.markdown(message["content"])

if prompt := st.chat_input("Faça uma pergunta sobre seus dados..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if st.session_state.agent_executor is None:
        st.warning("Por favor, carregue um arquivo CSV e clique em 'Iniciar Análise'.")
    else:
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                try:
                    response = st.session_state.agent_executor.invoke({"input": prompt})
                    response_content = response['output']
                    st.session_state.messages.append({"role": "assistant", "content": response_content})
                    
                    filepath = extract_filepath(response_content)
                    if filepath and os.path.exists(filepath):
                        clean_content = re.sub(r"\s*e salvo em:.*\.png", "", response_content)
                        st.markdown(clean_content)
                        st.image(filepath)
                    else:
                        st.markdown(response_content)
                except Exception as e:
                    error_message = f"Ocorreu um erro: {e}"
                    st.error(error_message)
                    st.session_state.messages.append({"role": "assistant", "content": error_message})
                    
