# app.py (Versão Final e 100% para Deploy)

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

if "messages" not in st.session_state:
    st.session_state.messages = []
if "agent_executor" not in st.session_state:
    st.session_state.agent_executor = None
if "dataframe" not in st.session_state:
    st.session_state.dataframe = None

# Barra Lateral (Sidebar)
with st.sidebar:
    st.header("1. Configuração do Modelo")

    # Seletor de Modelo
    model_provider = st.radio(
        "Escolha o modelo de linguagem:",
        ("Ollama (Local, 100% Gratuito)", "Google Gemini (API, Gratuito com Chave)")
    )

    # Campo Condicional para a Chave de API
    api_key = None
    if "Gemini" in model_provider:
        api_key = st.text_input(
            "Insira sua Chave de API do Google AI Studio:", 
            type="password",
            key="google_api_key"
        )
        st.caption("Obtenha sua chave gratuita em [aistudio.google.com](https://aistudio.google.com/app/apikey)")

    st.header("2. Carregue seus Dados")
    uploaded_file = st.file_uploader("Carregue seu arquivo CSV", type="csv")

    if uploaded_file is not None:
        if st.button("Iniciar Análise"):
            # Validação para garantir que a chave foi inserida se Gemini for selecionado
            if "Gemini" in model_provider and (not api_key or api_key.strip() == ""):
                st.error("⚠️ Por favor, insira sua chave de API do Google para usar o Gemini.")
            else:
                with st.spinner("Carregando dados e inicializando o agente..."):
                    try:
                        df = pd.read_csv(uploaded_file)
                        st.session_state.dataframe = df

                        # CORREÇÃO: Garantir que api_key seja passado como string limpa
                        clean_api_key = api_key.strip() if api_key else None

                        # Passando a escolha do modelo e a chave para o backend
                        st.session_state.agent_executor = create_eda_agent(
                            df, 
                            model_provider, 
                            clean_api_key
                        )

                        st.session_state.messages = [
                            {"role": "assistant", "content": f"✅ Agente inicializado com {model_provider}. Estou pronto para analisar!"}
                        ]
                        st.success("🎉 Agente pronto!")
                    except Exception as e:
                        st.error(f"❌ Ocorreu um erro: {e}")
                        import traceback
                        st.code(traceback.format_exc())

    if st.session_state.dataframe is not None:
        st.markdown("### 📊 Preview dos Dados")
        st.dataframe(st.session_state.dataframe.head())

# Interface de Chat Principal
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
        st.warning("⚠️ Por favor, carregue um arquivo CSV e clique em 'Iniciar Análise'.")
    else:
        with st.chat_message("assistant"):
            with st.spinner("🤔 Pensando..."):
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
                    error_message = f"❌ Ocorreu um erro: {e}"
                    st.error(error_message)
                    st.session_state.messages.append({"role": "assistant", "content": error_message})
                    import traceback
                    st.code(traceback.format_exc())
                    
