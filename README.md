# Semantic Document Search using RAG

This project implements a semantic document search system using text embeddings and a FAISS vector database.

## Architecture

Document → Text Extraction → Chunking → Embeddings → FAISS Vector Database → Semantic Search

## Tech Stack

Python
Sentence Transformers
FAISS
NumPy

## Features

* PDF document ingestion
* Text chunking
* Embedding generation
* Vector similarity search
* Semantic search over documents

## Run the Project

Install dependencies

```id="jmejdz"
pip install -r requirements.txt
```

Run the application

```id="l2upcb"
python app.py
```

## Semantic Document Search using RAG

• Built a Retrieval-Augmented Generation (RAG) system using Sentence Transformers embeddings and FAISS vector search.  
• Integrated Llama3 via Ollama to generate context-aware answers using retrieved document content.  
• Designed a semantic search pipeline enabling efficient retrieval of relevant document chunks for AI-assisted knowledge discovery.

Tech Stack: Python, Sentence Transformers, FAISS, Llama3 (Ollama)

