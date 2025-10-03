# agent_core.py (Versão Final com Melhorias de Robustez e Compatibilidade)

import os
import pandas as pd
from dotenv import load_dotenv

from langchain_community.chat_models import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain.memory import ConversationBufferWindowMemory

# Importa a nossa classe EDAToolkit
from tools import EDAToolkit

load_dotenv()

def create_eda_agent(df: pd.DataFrame, model_provider: str, api_key: str = None):
    """
    Cria e configura um agente de EDA usando o provedor de modelo selecionado.
    """
    llm = None

    if "Ollama" in model_provider:
        print("Inicializando agente com Ollama (llama3:8b)...")
        llm = ChatOllama(model="llama3:8b", temperature=0)
    
    elif "Gemini" in model_provider:
        print("Inicializando agente com Google Gemini...")
        if not api_key:
            raise ValueError("Chave de API do Google é necessária para usar o Gemini.")
        
        # --- SUAS SUGESTÕES IMPLEMENTADAS ---
        # 1. Usando o modelo 'gemini-1.0-pro' para máxima compatibilidade.
        # 2. Adicionando 'convert_system_message_to_human=True' para robustez.
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.0-pro", 
            google_api_key=api_key, 
            temperature=0,
            convert_system_message_to_human=True 
        )
    
    else:
        raise ValueError("Provedor de modelo desconhecido ou não suportado.")

    # A criação da caixa de ferramentas permanece a mesma
    toolkit = EDAToolkit(df=df)
    tools = toolkit.get_tools()

    prompt = hub.pull("hwchase17/react-chat")
    memory = ConversationBufferWindowMemory(k=5, memory_key="chat_history", return_messages=True)
    agent = create_react_agent(llm, tools, prompt)
    
    # --- SUA SUGESTÃO IMPLEMENTADA ---
    # 3. Adicionando 'max_iterations' para evitar loops infinitos.
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=10 
    )
    return agent_executor

if __name__ == '__main__':
    print("Este script agora é destinado a ser executado via 'streamlit run app.py'")

