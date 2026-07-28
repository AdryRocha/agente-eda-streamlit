# app.py (Versão Final Unificada para Execução Local e Deploy na Nuvem)

import streamlit as st
import pandas as pd
import os
import re
import traceback
from agent_core import create_eda_agent

st.set_page_config(page_title="Agente Autônomo de EDA", page_icon="🤖", layout="wide")
st.title("🤖 Agente Autônomo para Análise Exploratória de Dados (EDA)")
st.caption("Faça upload de um arquivo CSV e converse com seus dados em linguagem natural.")

def extract_filepath(text: str):
    """Extrai o caminho de um arquivo de imagem da resposta do agente."""
    pattern = r"(plots/[a-zA-Z0-9_.\-]+\.png)"
    match = re.search(pattern, text)
    return match.group(1) if match else None

# --- Gerenciamento Inteligente de API Key ---
# Tenta ler a chave dos "Secrets" do Streamlit Cloud primeiro.
# Se não encontrar, assume que estamos em um ambiente local.
api_key_from_secrets = None
try:
    # SUA SUGESTÃO IMPLEMENTADA: Acessa a chave específica dentro do objeto st.secrets
    api_key_from_secrets = st.secrets.get("GEMINI_API_KEY")
except (AttributeError, KeyError):
    # Isso é esperado em um ambiente local sem um arquivo secrets.toml
    pass

# Inicializa o estado da sessão
if "messages" not in st.session_state:
    st.session_state.messages = []
if "agent_executor" not in st.session_state:
    st.session_state.agent_executor = None
if "dataframe" not in st.session_state:
    st.session_state.dataframe = None

# --- Barra Lateral (Sidebar) ---
with st.sidebar:
    st.header("1. Configuração do Modelo")

    # Se a chave de API foi encontrada nos segredos, força o uso do Gemini (cenário de deploy).
    # Caso contrário, mostra o seletor para o usuário (cenário local).
    if api_key_from_secrets:
        model_provider = "Google Gemini (API, Gratuito com Chave)"
        st.info("Aplicação configurada para usar Google Gemini via API segura.")
        api_key = api_key_from_secrets
    else:
        model_provider = st.radio(
            "Escolha o modelo de linguagem:",
            ("Ollama (Local, 100% Gratuito)", "Google Gemini (API, Gratuito com Chave)")
        )
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
            # SUA SUGESTÃO IMPLEMENTADA: Validação robusta da chave de API
            final_api_key = api_key
            if "Gemini" in model_provider and (not final_api_key or final_api_key.strip() == ""):
                st.error("⚠️ Por favor, insira sua chave de API do Google para usar o Gemini.")
            else:
                with st.spinner("Carregando dados e inicializando o agente..."):
                    try:
                        df = pd.read_csv(uploaded_file)
                        st.session_state.dataframe = df

                        # SUA SUGESTÃO IMPLEMENTADA: Garante que a chave seja passada como uma string limpa
                        clean_api_key = final_api_key.strip() if final_api_key else None

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
                        st.error(
                            "❌ Não foi possível inicializar o agente. "
                            "Verifique a configuração do modelo e tente novamente."
                        )

                        # O erro completo aparece apenas nos logs do Streamlit.
                        traceback.print_exc()

    if st.session_state.dataframe is not None:
        st.markdown("### 📊 Preview dos Dados")
        st.dataframe(st.session_state.dataframe.head())

# --- Interface de Chat Principal ---
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
                    error_message = (
                        "❌ Não foi possível concluir a análise. "
                        "Verifique a configuração do modelo e tente novamente."
                    )
                
                    st.error(error_message)
                
                    # O erro completo aparece apenas nos logs do Streamlit.
                    traceback.print_exc()
                
                    st.session_state.messages.append(
                        {"role": "assistant", "content": error_message}
                    )
