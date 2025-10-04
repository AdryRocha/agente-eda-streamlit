### agente-eda-streamlit

# Agente Autônomo para Análise Exploratória de Dados (EDA)

[https://static.streamlit.io/badges/streamlit_badge_black_white.svg](https://agente-eda-app-adryrocha25.streamlit.app/)

## Sobre o Projeto

Este projeto consiste em um agente de Inteligência Artificial desenvolvido em Python, capaz de realizar Análise Exploratória de Dados (EDA) em qualquer arquivo CSV. A aplicação possui uma interface web interativa onde o usuário pode conversar com seus dados em linguagem natural, solicitar análises, gerar gráficos e obter conclusões sintetizadas.

A aplicação foi implantada na nuvem e pode ser acessada publicamente através do link acima. Adicionalmente, as seções abaixo detalham como executar o projeto em um ambiente local ou via Google Colab.

Características
Interface web interativa e acessível via link público.

Suporte a múltiplos modelos de execução:

Nuvem (Principal): Google Gemini, via Streamlit Community Cloud.

Local (Alternativo): Ollama, para uso privado e offline.

Análise de qualquer arquivo CSV.

Geração automática de visualizações (histogramas, mapas de calor, etc.).

Processamento de perguntas em linguagem natural e capacidade de síntese de conclusões.

Execução Local (Opcional)
Para executar a aplicação em sua máquina local, siga os passos abaixo.

Requisitos
Python 3.10+

Ollama (opcional, para usar o modo local)

Configuração
Clone o repositório:

Bash

git clone https://github.com/AdryRocha/agente-eda-streamlit.git
cd agente-eda-streamlit
Crie e ative um ambiente virtual:

Bash

# Criar o ambiente
python -m venv venv

# Ativar no Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Ativar no macOS/Linux
source venv/bin/activate

Instale as dependências:

Bash

pip install -r requirements.txt
Configure o Ollama (se for usar o modo local):

Baixe e instale o Ollama em ollama.com.

Execute o seguinte comando no terminal para baixar o modelo correto:

Bash

ollama run llama3:8b
Como Usar Localmente
Inicie a aplicação:

Bash

streamlit run app.py
A aplicação abrirá no seu navegador. Na barra lateral, escolha o modelo (Ollama ou Gemini), carregue seu arquivo CSV e inicie a análise.

Execução via Google Colab (Opcional)
Para testar o agente em um ambiente na nuvem sem instalações locais, siga este guia.

Requisitos do Colab
Você precisará de duas chaves gratuitas:

Chave de API do Google Gemini: Obtenha em(https://aistudio.google.com/app/apikey).

Authtoken do ngrok: Crie uma conta em ngrok.com e copie o token do seu dashboard.

Instruções de Execução
Abrir o Notebook:

Acesse o Google Colab.

Vá em "Arquivo" -> "Fazer upload de notebook..." e selecione o arquivo Executar_Agente_EDA.ipynb (se fornecido).

Executar as Células:

Execute as células do notebook em ordem. A primeira instala as dependências, e as seguintes criam os arquivos do projeto.

Configurar e Iniciar:

Na última célula, substitua o placeholder pelo seu Authtoken do ngrok:

Python

NGROK_AUTH_TOKEN = "COLE_SEU_AUTHTOKEN_DO_NGROK_AQUI"
Execute a célula e aguarde a URL pública ser gerada.

Usar o Agente:

Clique na URL gerada, insira sua chave de API do Gemini na interface, faça o upload do arquivo CSV e inicie a análise.

Licença

MIT
