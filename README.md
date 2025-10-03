# agente-eda-streamlit

# Agente Autônomo para Análise Exploratória de Dados (EDA)

## Sobre o Projeto

Este projeto consiste em um agente de Inteligência Artificial desenvolvido em Python, capaz de realizar Análise Exploratória de Dados (EDA) em qualquer arquivo CSV. A aplicação possui uma interface web interativa onde o usuário pode conversar com seus dados em linguagem natural, solicitar análises, gerar gráficos e obter conclusões sintetizadas.

## Características

- Interface web interativa
- Suporte a múltiplos modelos:
  - Ollama (local, gratuito)
  - Google Gemini (API)
- Análise de arquivos CSV
- Geração automática de visualizações
- Processamento em linguagem natural

## Requisitos do Sistema

- Python 3.10+
- Ollama (opcional, para modo local)

## Configuração Local

1. Clone o repositório:

    ```powershell
    git clone https://github.com/seu-usuario/agente-eda.git
    cd agente-eda
    ```

2. Crie e ative um ambiente virtual:

    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

3. Instale as dependências:

    ```powershell
    pip install -r requirements.txt
    ```

4. Configure o Ollama (opcional):

    - Baixe e instale o Ollama de [ollama.com](https://ollama.com)
    - Execute o modelo:

    ```powershell
    ollama run llama2
    ```

## Como Usar Localmente

1. Inicie a aplicação:

    ```powershell
    streamlit run app.py
    ```

2. Escolha o modelo:

    - Ollama (Local, 100% Gratuito)
    - Google Gemini (requer API key)

3. Carregue seus dados:

    - Faça upload do arquivo CSV
    - Clique em "Iniciar Análise"

4. Comece a análise:

    - Use o chat para fazer perguntas sobre seus dados
    - Solicite visualizações e análises estatísticas
    - Obtenha insights em linguagem natural

## Configurações Adicionais

- Para usar o Google Gemini, obtenha uma chave API em [Google AI Studio](https://aistudio.google.com/app/apikey)
- O Ollama deve estar em execução para usar o modo local

## Execução via Google Colab

Para testar o agente sem instalações locais, siga este guia detalhado.

### Requisitos do Colab

Você precisará de duas chaves gratuitas:

1. **Chave API do Google Gemini**
    - Acesse [Google AI Studio](https://aistudio.google.com/app/apikey)
    - Faça login e clique em "Create API key"
    - Copie a chave gerada

2. **Authtoken do ngrok**
    - Crie uma conta em [ngrok.com](https://ngrok.com)
    - No dashboard, acesse "Your Authtoken"
    - Copie o token

### Instruções de Execução

1. **Abrir o Notebook**
    - Acesse o [Google Colab](https://colab.research.google.com)
    - Vá em "Arquivo" -> "Fazer upload de notebook..."
    - Selecione `Executar_Agente_EDA.ipynb`

2. **Executar Células de Configuração**
    - Execute as células em ordem (Shift + Enter)
    - Célula 1: Instala dependências
    - Células 2-4: Criam arquivos do projeto

3. **Configurar e Iniciar**
    - Na Célula 5, substitua:

    ```python
    NGROK_AUTH_TOKEN = "COLE_SEU_AUTHTOKEN_DO_NGROK_AQUI"
    ```

    - Execute a célula
    - Aguarde a URL pública ser gerada

4. **Usar o Agente**
    - Clique na URL gerada
    - Insira sua chave API do Gemini
    - Faça upload do arquivo CSV
    - Inicie a análise via chat

### Informações Importantes

- O link é temporário e funciona apenas enquanto o Colab estiver ativo
- A execução é totalmente na nuvem, sem necessidade de instalações locais
- Recomendado usar o Chrome para melhor compatibilidade

## Licença

MIT
