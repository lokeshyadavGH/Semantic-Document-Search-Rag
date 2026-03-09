from src.load_documents import load_pdf
from src.chunk_text import split_text
from src.create_embeddings import create_embeddings
from src.vector_store import create_faiss_index
from src.search import search


print("Loading document...")

text = load_pdf("data/sample.pdf")

print("Splitting document into chunks...")

chunks = split_text(text)

print("Creating embeddings...")

embeddings, model = create_embeddings(chunks)

print("Creating FAISS index...")

index = create_faiss_index(embeddings)

print("Document search system ready!")

while True:

    query = input("\nAsk a question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    results = search(query, model, index, chunks)

    print("\nTop Relevant Results:\n")

    for r in results:
        print(r)
        print("\n---\n")