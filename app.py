from src.load_documents import load_pdf
from src.chunk_text import split_text
from src.create_embeddings import create_embeddings
from src.vector_store import create_faiss_index
from src.search import search
from src.rag_pipeline import generate_answer


print("Loading document...")

text = load_pdf("data/sample.pdf")

print("Chunking document...")

chunks = split_text(text)

print("Creating embeddings...")

embeddings, model = create_embeddings(chunks)

print("Building FAISS index...")

index = create_faiss_index(embeddings)

print("\nRAG system ready!")

while True:

    query = input("\nAsk a question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    retrieved_chunks = search(query, model, index, chunks)

    print("\nGenerating answer using LLM...\n")

    answer = generate_answer(query, retrieved_chunks)

    print("Answer:\n")
    print(answer)
