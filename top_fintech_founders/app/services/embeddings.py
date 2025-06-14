import os
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from app.models.founder import FounderOut
from app.utils.cleaning import clean_text
from app.services.scoring import compute_score

# Verifica se o arquivo CSV existe
file_path = "app/data/founders_real.csv"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"⚠️ O arquivo '{file_path}' não foi encontrado. Crie o CSV com os dados reais primeiro.")

# Carregar e limpar os dados
df = pd.read_csv(file_path)
df["bio_clean"] = df["bio"].apply(clean_text)

# Criar embeddings e índice FAISS
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(df["bio_clean"].tolist())
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# Função principal de busca
def search_top_founders(query: str, top_k: int = 20):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), top_k)

    results = []
    for idx, dist in zip(I[0], D[0]):
        row = df.iloc[idx].to_dict()
        base_score = float(1 / (1 + dist))
        final_score = compute_score(row, base_score)

        results.append(FounderOut(
            name=row["name"],
            startup=row["startup"],
            bio=row["bio"],
            score=final_score,
            country=row.get("country", "")
        ))
    return results
