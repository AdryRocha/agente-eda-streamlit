# 🤖 Agente Autônomo para Análise Exploratória de Dados (EDA)

Agente de Inteligência Artificial desenvolvido em Python para analisar arquivos CSV por meio de comandos em linguagem natural.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://agente-eda-app-adryrocha25.streamlit.app/)

## 🌐 Demonstração online

A aplicação está implantada no Streamlit Community Cloud e pode ser acessada pelo endereço:

[https://agente-eda-app-adryrocha25.streamlit.app/](https://agente-eda-app-adryrocha25.streamlit.app/)

O usuário pode carregar um arquivo CSV e solicitar análises como:

- descrição geral do conjunto de dados;
- estatísticas descritivas;
- contagem de valores;
- geração de histogramas;
- gráficos de dispersão;
- mapas de correlação;
- síntese das conclusões obtidas durante a conversa.

## 📌 Sobre o projeto

O projeto implementa um agente autônomo de Análise Exploratória de Dados — EDA.

O agente interpreta as perguntas do usuário, seleciona a ferramenta adequada, executa a análise sobre o DataFrame e apresenta os resultados em linguagem natural.

A solução utiliza o padrão ReAct — Reasoning and Acting — para permitir que o modelo decida quando e como utilizar cada ferramenta disponível.

Também foi implementada memória conversacional, permitindo que o agente recupere resultados anteriores e produza uma síntese consolidada das análises realizadas.

## ✨ Principais funcionalidades

- Upload de arquivos CSV.
- Interface web interativa com Streamlit.
- Consultas aos dados em linguagem natural.
- Seleção autônoma de ferramentas.
- Estatísticas descritivas.
- Contagem de valores por coluna.
- Geração de histogramas.
- Geração de gráficos de dispersão.
- Geração de mapas de calor de correlação.
- Memória conversacional.
- Síntese das conclusões anteriores.
- Execução com Google Gemini em nuvem.
- Execução local alternativa com Ollama.
- Proteção das credenciais por Secrets.
- Tratamento amigável de erros e limites temporários da API.

## 🧰 Tecnologias utilizadas

- Python
- Streamlit
- LangChain
- Google Gemini
- Ollama
- Llama 3
- Pandas
- Matplotlib
- Seaborn
- python-dotenv
- Git e GitHub

## 🏗️ Arquitetura da solução

A aplicação foi organizada em três camadas principais:

```text
agente-eda-streamlit/
├── app.py
├── agent_core.py
├── tools.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── docs/
│   └── relatorio-agente-eda.pdf
└── notebooks/
    └── executar-agente-eda-colab-seguro.ipynb
```

### `app.py`

Responsável pela interface Streamlit, upload do CSV, histórico da conversa, exibição das respostas e visualização dos gráficos.

### `agent_core.py`

Responsável pela inicialização do modelo, criação do agente ReAct, configuração da memória e integração das ferramentas.

Na implantação atual em nuvem, o agente utiliza:

```text
gemini-3.6-flash
```

### `tools.py`

Contém as ferramentas especializadas de análise de dados disponibilizadas ao agente, como:

- visão geral do dataset;
- estatísticas descritivas;
- contagem de valores;
- histograma;
- gráfico de dispersão;
- mapa de correlação.

## ▶️ Como testar a aplicação online

1. Acesse a [demonstração no Streamlit](https://agente-eda-app-adryrocha25.streamlit.app/).
2. Clique em **Browse files**.
3. Selecione um arquivo CSV.
4. Clique em **Iniciar Análise**.
5. Faça perguntas sobre os dados.

Exemplos:

```text
Faça uma descrição geral dos dados.
```

```text
Mostre-me a distribuição da coluna Amount em um histograma.
```

```text
Existe alguma correlação entre as variáveis?
```

```text
Qual é a contagem de valores da coluna Class?
```

```text
Com base nas análises realizadas, quais são as principais conclusões?
```

## 💻 Execução local

### Requisitos

- Python 3.10 ou superior;
- Git;
- Ollama, somente para execução local com modelos de código aberto;
- chave da API do Google Gemini, somente para execução com Gemini.

### 1. Clone o repositório

```bash
git clone https://github.com/AdryRocha/agente-eda-streamlit.git
cd agente-eda-streamlit
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

No Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

No macOS ou Linux:

```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Inicie a aplicação

```bash
streamlit run app.py
```

A aplicação será aberta no navegador, normalmente no endereço:

```text
http://localhost:8501
```

## 🦙 Execução local com Ollama

Instale o Ollama a partir do site oficial e baixe o modelo utilizado pelo projeto:

```bash
ollama run llama3:8b
```

Depois, execute:

```bash
streamlit run app.py
```

Na barra lateral da aplicação, escolha a opção de execução local com Ollama.

## 🔐 Configuração segura do Gemini

As chaves e tokens não devem ser escritos diretamente no código nem enviados ao GitHub.

### Streamlit Community Cloud

No painel de configuração do aplicativo, adicione o Secret no formato TOML:

```toml
GEMINI_API_KEY = "SUA_CHAVE_DO_GEMINI"
```

A chave fica armazenada no ambiente do Streamlit e não aparece no repositório.

### Execução local com Secrets

Crie o arquivo:

```text
.streamlit/secrets.toml
```

Adicione:

```toml
GEMINI_API_KEY = "SUA_CHAVE_DO_GEMINI"
```

Confirme que o `.gitignore` contém:

```gitignore
.streamlit/secrets.toml
.env
```

Nunca envie esses arquivos ao GitHub.

## 📓 Execução pelo Google Colab

Uma versão segura do notebook está disponível em:

[Executar Agente EDA no Google Colab](notebooks/executar-agente-eda-colab-seguro.ipynb)

Para executar o notebook, cadastre os seguintes valores no painel **Secrets** do Google Colab:

```text
GEMINI_API_KEY
NGROK_AUTH_TOKEN
```

As credenciais são acessadas em tempo de execução e não ficam armazenadas no notebook.

Não substitua placeholders por chaves diretamente nas células.

## 📄 Documentação técnica

O relatório completo apresenta:

- escolha das tecnologias;
- arquitetura da solução;
- funcionamento do agente;
- ferramentas implementadas;
- memória conversacional;
- testes realizados;
- execução local;
- deploy no Streamlit;
- capturas da aplicação e dos resultados.

[Consultar relatório técnico](docs/relatorio-agente-eda.pdf)

## ⚠️ Limitações conhecidas

- O plano gratuito da API Gemini possui limite temporário de chamadas.
- Uma única pergunta pode exigir mais de uma chamada ao modelo devido ao funcionamento do agente ReAct.
- Caso o limite seja atingido, a aplicação orienta o usuário a aguardar antes de tentar novamente.
- Arquivos muito grandes podem aumentar o tempo de carregamento e o consumo de memória.
- As respostas produzidas pelo modelo devem ser confrontadas com os resultados calculados pelas ferramentas.
- Algumas conclusões geradas pelo LLM podem representar recomendações gerais e não resultados estatisticamente comprovados.
- A aplicação realiza análise exploratória e não substitui uma validação técnica completa por um cientista ou analista de dados.

## 🔒 Segurança e privacidade

- Nenhuma chave de API é armazenada no código-fonte.
- As credenciais são carregadas por Secrets.
- Arquivos enviados são processados durante a sessão da aplicação.
- Para dados confidenciais, recomenda-se a execução local com Ollama.
- Não envie dados pessoais, sigilosos ou protegidos para uma demonstração pública.

## 🚀 Melhorias futuras

- Validação automática das conclusões geradas pelo modelo.
- Separação entre resultados calculados, hipóteses e recomendações.
- Exportação de relatórios em PDF.
- Inclusão de novas ferramentas estatísticas.
- Suporte a arquivos Excel e Parquet.
- Observabilidade detalhada das chamadas do agente.
- Testes automatizados das ferramentas e da interface.
- Controle de tamanho e amostragem de datasets muito grandes.

## 👩‍💻 Autora

**Adriana Rocha Castro de Paula**

- GitHub: [AdryRocha](https://github.com/AdryRocha)
- LinkedIn: [adrianarochacp](https://www.linkedin.com/in/adrianarochacp)

## 📜 Licença

Este projeto está disponibilizado sob a licença MIT.
