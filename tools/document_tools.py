
# tools/document_tools.py
import os
from typing import List, Dict
from langchain.tools import tool
from sentence_transformers import SentenceTransformer
from sklearn.cluster import HDBSCAN
import numpy as np
import config

embedding_model = SentenceTransformer(config.EMBEDDING_MODEL)

@tool
def list_markdown_files(directory: str = config.INPUT_DATA_DIR) -> List[str]:
    print(f"--- Eseguo tool: list_markdown_files in '{directory}' ---")
    markdown_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".md")]
    return markdown_files

@tool
def read_file_content(filepath: str) -> str:
    print(f"--- Eseguo tool: read_file_content su '{filepath}' ---")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Errore: {e}"

@tool
def create_embeddings(texts: List[str]) -> List[List[float]]:
    print(f"--- Eseguo tool: create_embeddings su {len(texts)} testi ---")
    embeddings = embedding_model.encode(texts, convert_to_tensor=False)
    return embeddings.tolist()

@tool
def cluster_texts(embeddings: List[List[float]]) -> Dict[int, int]:
    print(f"--- Eseguo tool: cluster_texts su {len(embeddings)} vettori ---")
    embeddings_np = np.array(embeddings)
    clusterer = HDBSCAN(min_cluster_size=2, min_samples=1, metric='euclidean')
    clusterer.fit(embeddings_np)
    return {i: int(label) for i, label in enumerate(clusterer.labels_)}
