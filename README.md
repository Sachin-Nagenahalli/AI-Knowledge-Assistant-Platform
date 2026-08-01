# 🤖 AI Knowledge Assistant Platform

> A production-ready Retrieval-Augmented Generation (RAG) platform that enables users to organize, index, search, and chat with private document collections using local Large Language Models powered by Ollama.

---

# 🚀 Features

### 📂 Collection Management
- Create and manage document collections
- Delete collections
- Organize knowledge into separate workspaces

### 📄 Document Management
- Upload PDF documents
- Automatic document indexing
- SHA-256 duplicate detection
- Delete indexed documents

### 🔍 Semantic Search
- Vector embeddings using Ollama
- ChromaDB vector database
- Top-K similarity retrieval
- Context-aware search

### 💬 AI Knowledge Assistant
- Retrieval-Augmented Generation (RAG)
- Natural language question answering
- Source citations
- Confidence score for every response

### 🗄 Data Storage
- SQLite for metadata
- ChromaDB for vector embeddings

### 🖥 User Interface
- FastAPI REST API
- Interactive Swagger Documentation
- Streamlit Web Interface

### 🐳 Deployment
- Docker support
- Docker Compose
- Persistent storage
- Production-ready architecture

---

# 🏗 System Architecture

```
                    +----------------------+
                    |   Streamlit Frontend |
                    +----------+-----------+
                               |
                               ▼
                    +----------------------+
                    |    FastAPI Backend   |
                    +----------+-----------+
                               |
        +----------------------+----------------------+
        |                      |                      |
        ▼                      ▼                      ▼
 +---------------+     +---------------+     +----------------+
 |   SQLite DB   |     |   ChromaDB    |     |     Ollama     |
 | Metadata      |     | Vector Store  |     | LLM & Embedding|
 +---------------+     +---------------+     +----------------+
                               |
                               ▼
                  Retrieval-Augmented Generation
```

---

# 🛠 Technology Stack

| Category | Technology |
|----------|------------|
| Backend | FastAPI |
| Frontend | Streamlit |
| Database | SQLite |
| Vector Database | ChromaDB |
| ORM | SQLAlchemy |
| LLM | Qwen 2.5 (Ollama) |
| Embeddings | EmbeddingGemma |
| PDF Processing | PyPDF |
| Deployment | Docker |

---

# 📁 Project Structure

```text
AI-Knowledge-Assistant-Platform/

├── app/
│   ├── api/
│   ├── core/
│   ├── indexing/
│   ├── models/
│   ├── rag/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── frontend/
│   ├── components/
│   ├── pages/
│   └── app.py
│
├── data/
├── storage/
├── logs/
├── tests/
├── scripts/
│
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

---

# ⚙ Installation

## Clone the Repository

```bash
git clone https://github.com/Sachin-Nagenahalli/AI-Knowledge-Assistant-Platform.git

cd AI-Knowledge-Assistant-Platform
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🦙 Install Ollama

Download Ollama:

https://ollama.com

Pull the required models:

```bash
ollama pull qwen2.5:3b

ollama pull embeddinggemma
```

Start Ollama:

```bash
ollama serve
```

---

# ▶ Running the Backend

```bash
uvicorn app.main:app --reload
```

Swagger UI:

```
http://localhost:8000/docs
```

---

# ▶ Running the Frontend

```bash
streamlit run frontend/app.py
```

Application:

```
http://localhost:8501
```

---

# 🐳 Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

Run in Background

```bash
docker compose up -d
```

---

# 📚 REST API

## Collections

| Method | Endpoint |
|---------|----------|
| GET | `/collections` |
| POST | `/collections` |
| DELETE | `/collections/{id}` |

---

## Documents

| Method | Endpoint |
|---------|----------|
| POST | `/collections/{id}/documents/upload` |
| GET | `/documents` |
| DELETE | `/documents/{id}` |

---

## Search

| Method | Endpoint |
|---------|----------|
| GET | `/search` |

---

## Chat

| Method | Endpoint |
|---------|----------|
| POST | `/chat` |

---

# 🧠 RAG Workflow

```text
User Question
      │
      ▼
Generate Query Embedding
      │
      ▼
Semantic Search (ChromaDB)
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Prompt Builder
      │
      ▼
Ollama (Qwen 2.5)
      │
      ▼
AI Response
      │
      ▼
Answer + Sources + Confidence
```

---

---

# 🔮 Future Improvements

- User Authentication
- Conversation History
- Multi-user Support
- Hybrid Search (BM25 + Vector)
- Streaming Responses
- Role-Based Access Control
- Cloud Deployment
- CI/CD Pipeline
- Document Versioning

---

# 👨‍💻 Author

**Sachin Nagenahalli**

M.Sc. Biotechnology

AI Engineering & Bioinformatics Enthusiast

GitHub:
https://github.com/Sachin-Nagenahalli

LinkedIn:
*(Add your LinkedIn profile)*

---

# 🙏 Acknowledgements

- FastAPI
- Streamlit
- ChromaDB
- SQLAlchemy
- Ollama
- Qwen
- PyPDF

---

# 📄 License

This project is licensed under the MIT License.
