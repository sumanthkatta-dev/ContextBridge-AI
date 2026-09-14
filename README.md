# 🔗 RAG-MCP Explorer

**Decoupled Vector Search Interface - Powered by FastMCP and ChromaDB**

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](#) [![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-teal.svg)](#) [![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Store-orange.svg)](#) [![Status](https://img.shields.io/badge/Status-Frontend_In_Development-yellow.svg)](#)

> A full-stack web application bridging the gap between raw document embeddings and a functional, user-facing search dashboard.

**🚧 Development Status:** The core backend architecture (FastAPI, ChromaDB, MCP embeddings) is currently implemented. The vanilla HTML/CSS/JS frontend is in the active design phase. The mockups below illustrate the target UI architecture currently being built.

---

### The Architecture Shift

| The Old Way (Script-Based MCP) | The RAG-MCP Way (Decoupled Web UI) |
| :--- | :--- |
| Executed primarily via terminal or CLI wrappers. | Accessed via a responsive, browser-based dashboard. |
| Opaque retrieval process with raw JSON outputs. | Transparent context retrieval with visual confidence scores. |
| Coupled tightly to FastMCP standard I/O. | Decoupled FastAPI backend with direct ChromaDB interfacing. |
| Difficult to demonstrate to non-technical stakeholders. | Streamlined drag-and-drop ingestion and natural language querying. |

---

### Core Engineering Features

**Decoupled Backend**
Transitions the original script-based MCP implementation into a robust REST API using FastAPI. It handles PDF chunking, embedding generation, and direct ChromaDB querying without relying on JSON-RPC over SSE.

**Framework-Free Frontend (In Progress)**
The planned user interface is designed to be built entirely with Vanilla HTML5, CSS3, and JavaScript. It utilizes modern CSS properties (backdrop-filters, CSS variables) to achieve a dark-mode glassmorphism aesthetic without the overhead of React or Tailwind.

**Traceable Context**
Search queries do not just return an AI-generated summary; the dashboard explicitly renders the exact text chunks (with page numbers and relevance scores) retrieved from the vector database to ensure complete data provenance.

---

### UI Architecture Mockups

**1. Home Screen (Upload & Search)**
*(Target ingestion interface for file parsing and initial query execution)*

![Home Screen Mockup](home_screen.png) 


**2. Retrieval Dashboard**
*(Target search result interface displaying AI summaries alongside retrieved ChromaDB context chunks)*

![Dashboard Mockup](Dashboard.png)

---

### How It Works (3 Steps)

1. **Ingest:** Drag and drop a PDF into the dashboard. 
2. **Process:** The FastAPI backend chunks the document, generates custom embeddings, and indexes them in ChromaDB.
3. **Retrieve:** Submit a natural language query. The system performs a similarity search and returns both a synthesized answer and the raw contextual excerpts.

---

### Run It Locally (Backend Only)

To test the current backend infrastructure locally:

```bash
# 1. Clone the repository
git clone [https://github.com/sumanthkatta-dev/rag-mcp-explorer.git](https://github.com/sumanthkatta-dev/rag-mcp-explorer.git)

# 2. Install backend dependencies
pip install -r requirements.txt

# 3. Initialize the FastAPI server
uvicorn app:app --reload --port 3000
