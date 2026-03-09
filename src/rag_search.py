def search(query, model, index, chunks, k=3):
    """
    Search the FAISS index using a query
    """

    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, k)

    results = []

    for i in indices[0]:
        results.append(chunks[i])

    return results