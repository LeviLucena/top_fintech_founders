<p align="center">

  <!-- Linguagem principal -->
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  </a>

  <!-- Framework Backend -->
  <a href="https://fastapi.tiangolo.com/">
    <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  </a>

  <!-- Vetorização -->
  <a href="https://www.sbert.net/">
    <img src="https://img.shields.io/badge/Sentence_Transformers-5C2D91?style=for-the-badge&logo=semantic-release&logoColor=white" alt="Sentence Transformers" />
  </a>

  <!-- FAISS -->
  <a href="https://github.com/facebookresearch/faiss">
    <img src="https://img.shields.io/badge/FAISS-005571?style=for-the-badge&logo=github&logoColor=white" alt="FAISS" />
  </a>

  <!-- Pandas -->
  <a href="https://pandas.pydata.org/">
    <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  </a>

  <!-- Streamlit (opcional) -->
  <a href="https://streamlit.io/">
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  </a>

  <!-- License -->
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT License" />

</p>

![Gemini_Generated_Image_ap1iorap1iorap1ihhhh2222](https://github.com/user-attachments/assets/60be5a7d-71bf-45a1-8359-8213bcb218bb)

# 🚀 Top Fintech Founders API

Uma API inteligente para destacar os 20 fundadores emergentes de fintechs com base em análise semântica e pontuação via IA. Ideal para rankings rápidos, dashboards e insights estratégicos.

## 📌 Funcionalidades
- Rankeamento automático de fundadores com base em seus perfis e bios
- Busca semântica usando embeddings (SentenceTransformer + FAISS)
- Sistema de pontuação ajustável com base em palavras-chave e critérios técnicos
- API leve com FastAPI, pronta para integração
- Suporte a dashboards via Streamlit

## Desafios Técnicos
### 1. 📥 Coleta de Dados
- Fontes: Raspar LinkedIn (via APIs não oficiais ou serviços como PhantomBuster) e blogs especializados em fintech (ex: TechCrunch, Fintech Futures, Contxto, etc.).

### Abordagem:
- Criar um scraper com BeautifulSoup ou Playwright para blogs.
- Para LinkedIn, utilizar ferramentas como SerpAPI, PhantomBuster ou importar dados existentes.
- Usar critérios como número de funcionários, fundação recente, rondas de investimento, palavras-chave (ex: open banking, DeFi).

### 2. 🧹 Limpeza e Enriquecimento de Dados
- Padronizar nomes, empresas, cargos.
- Remover duplicatas, normalizar campos (data, localização, etc).
- Enriquecer com APIs de investimento (ex: Crunchbase ou Dealroom) para validar estágio da startup.

### 3. 🧠 Modelagem - Sistema de Pontuação com IA
Modelo: Criar um agente com LangChain + OpenAI.

- Usar embeddings (text-embedding-ada-002) para vetorização dos perfis e artigos.
- Construir um índice com FAISS para busca semântica.
- Cada fundador é ranqueado com base em:
- Influência no setor (presença online, publicações).
- Inovação (palavras-chave extraídas via NLP).
- Crescimento (funcionários no LinkedIn + funding).

### 4. 🧪 Validação
- Verificar amostragem dos top 10-20 com um analista (ou parceiro) para confirmar relevância.
- Comparar resultados do agente com uma abordagem manual simples (baseline).
- Adicionar logs e métricas de confiança à resposta do agente (ex: score de similaridade, fontes encontradas).

### 5. 🚀 Deploy - Prototipagem
- Construir um endpoint FastAPI com rota /top-founders que aceita filtros (ex: país, nicho fintech).
- Retorno: JSON com nome, startup, score, razão do ranqueamento e link da fonte.
- Frontend opcional: um dashboard leve com Streamlit ou apenas uma página HTML com fetch().

---
## 🔍 Endpoint principal: /top-founders
Obtém a lista dos fundadores mais relevantes com base em uma busca semântica.

## URL
`GET /top-founders`
## Parâmetros de consulta

| Parâmetro   | Tipo    | Requisito | Descrição                                                         | Valor padrão             |
|-------------|---------|------------|-------------------------------------------------------------------|--------------------------|
| `query`     | string  | obrigatório| Termo de busca para encontrar fundadores relevantes (exemplo: *open finance*, *pix*, *fintech*) | —                        |
| `top_k`     | int     | opcional    | Quantidade de resultados desejados                                | 20                       |

---
Acesse a documentação interativa em:
> 👉 http://127.0.0.1:8000/docs

![image](https://github.com/user-attachments/assets/97abb0be-ef9b-441b-9bf2-2a935e31f211)

---
### 🛠️ Ferramentas Utilizadas
- 🖥️ Stack: Python, LangChain, Scikit-learn (para scoring e análise), Pandas (para manipulação de dados), Streamlit, FAISS (para indexação e busca), OpenAI, FastAPI.
- 🌐 Raspagem: Playwright/PhantomBuster + BeautifulSoup.
- 🤖 IA: Embeddings + Indexação + Classificação Regrada.
- 🚀 Deploy: Container leve (Docker) rodando na Vercel/Render/HuggingFace Spaces.

## 📁 Estrutura do Projeto
```bash
top_fintech_founders/
├── app/
│   ├── __init__.py
│   ├── main.py               # Ponto de entrada FastAPI
│   ├── api/
│   │   └── routes.py         # Endpoints da API
│   ├── services/
│   │   ├── embeddings.py     # Lógica de embeddings e busca com FAISS
│   │   ├── scoring.py        # Sistema de pontuação ou ranking (regra ou ML)
│   │   └── scraping.py       # Funções para raspar LinkedIn, blogs etc.
│   ├── models/
│   │   └── founder.py        # Modelos Pydantic usados na API
│   ├── data/
│   │   └── founders.csv      # Base temporária de dados (mock/scrape)
│   └── utils/
│       └── cleaning.py       # Limpeza e normalização de dados
│
├── notebooks/
│   └── exploratory_analysis.ipynb  # EDA e protótipos
├── requirements.txt
├── README.md
└── run.sh                    # Script para rodar localmente
```

## ✅ Descrição dos Componentes
- **app/main.py**: *Inicializa a aplicação e importa as rotas.*
- **api/routes.py**: *Define o endpoint /top-founders.*
- **services/embeddings.py**: *Carrega modelo SentenceTransformer, gera embeddings, inicializa FAISS.*
- **services/scoring.py**: *Sistema de ranqueamento simples ou baseado em heurísticas.*
- **services/scraping.py**: *Web scrapers para LinkedIn/blogs (ex: BeautifulSoup, Playwright, PhantomBuster).*
- **models/founder.py**: *Estrutura do output (FounderOut).*
- **utils/cleaning.py**: *Funções de limpeza, normalização e enrich.*
- **data/founders.csv**: *Pode conter os dados mockados ou raspados.*
- **notebooks/**: *Espaço para prototipagem, validações com LangChain etc.*

---

## 📥 Instalação local
```bash
# Clone este repositório
https://github.com/LeviLucena/top_fintech_founders.git

# Crie o ambiente virtual (opcional)
python -m venv venv
venv\Scripts\activate  # ou source venv/bin/activate no Linux/macOS

# Instale as dependências
pip install -r requirements.txt

# Execute o servidor
python -m uvicorn app.main:app --reload
```

## 📊 Dashboard opcional com Streamlit
execute o arquivo em outro terminal 
```bash
streamlit run dashboard.py
```
Acesse: http://localhost:8501

| Imagem 1 | Imagem 2 |
| -------- | -------- |
| ![image](https://github.com/user-attachments/assets/6d1b4f9a-68b8-454f-87da-b565c87e37fb) | ![image](https://github.com/user-attachments/assets/925ff08a-def7-48ba-875a-e332008a3e91) |

---

## 🧩 Visão geral: Como usar PhantomBuster com seu projeto
✅ Fluxo típico:
1. Configura um Phantom na web (ex: LinkedIn Search Export)
2. Ele raspa os dados de perfis e exporta para CSV ou JSON
3. Você baixa esse arquivo (ou pega a URL da API do Phantom)
4. Usa no seu código Python (read_csv() ou requests.get(...))

## 🚀 Passo a passo para usar o PhantomBuster
### 1. Crie uma conta grátis
- Acesse: https://phantombuster.com
- Crie uma conta (você ganha 20 minutos de automações por dia no plano gratuito)

### 2. Escolha o Phantom “LinkedIn Search Export”
>Vá em: https://phantombuster.com/phantombuster?category=LinkedIn
- Selecione "LinkedIn Search Export"
- Clique em “Use this Phantom”

### 3. Conecte sua sessão do LinkedIn
O site vai te pedir para instalar a extensão do PhantomBuster no navegador<br>
Ela captura automaticamente sua session cookie do LinkedIn (você não precisa colocar senha)

### 4. Configure a busca
Exemplo de busca:
>https://www.linkedin.com/search/results/people/?keywords=foundador%20fintech%20brasil

- Limite: ~100 perfis por execução gratuita
- Defina as colunas desejadas: nome, cargo, empresa, bio curta

### 5. Execute e baixe o resultado
- Após a execução, baixe o arquivo .csv com os dados dos fundadores
- Ou copie a URL da API do PhantomBuster (caso queira automatizar com requests.get())

---

## 📦 Como usar no seu código Python
### Opção 1: Importar localmente
```bash
import pandas as pd

df = pd.read_csv("linkedin_founders.csv")  # arquivo baixado do Phantom
``` 

### Opção 2: Consumir diretamente da URL do Phantom
```bash
import pandas as pd

url = "https://api.phantombuster.com/api/v2/agent/xxxxxx/output"
df = pd.read_csv(url)
```

> ⚠️ Essa URL exige seu API Key e Agent ID, que a própria plataforma te fornece.

## 🤝 Contributions
Feel free to contribute, suggest improvements, or report issues to help develop this project.

## 📄 License
This project is licensed under the MIT License — see [LICENSE](https://github.com/github/gitignore/blob/main/LICENSE) for details.
