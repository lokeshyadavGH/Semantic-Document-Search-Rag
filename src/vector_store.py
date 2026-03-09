import faiss
import numpy as np


def create_faiss_index(embeddings):
    """
    Store embeddings inside FAISS vector database
    """

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    return index