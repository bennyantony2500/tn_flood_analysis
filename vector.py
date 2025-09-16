from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

import os
import pandas as pd

# Load the flood dataset
df = pd.read_csv("tamilnadu_floods_2024.csv")

# Initialize embeddings model
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Vector DB location
db_loc = "./chroma_tn_floods_db"

# Check if DB already exists
exist = not os.path.exists(db_loc)

if exist:
    documents = []
    ids = []

    for i, row in df.iterrows():
        # Build a textual representation for embedding
        page_text = (
            f"District: {row['District']}, Date: {row['Date']}, "
            f"Flood level: {row['Flood_Level_m']}m, Rainfall: {row['Rainfall_mm']}mm, "
            f"Affected population: {row['Affected_Population']}, "
            f"Damages: {row['Damages_Crores_INR']} crores INR"
        )

        document = Document(
            page_content=page_text,
            metadata={
                "district": row["District"],
                "date": row["Date"],
                "flood_level_m": row["Flood_Level_m"],
                "rainfall_mm": row["Rainfall_mm"],
                "affected_population": row["Affected_Population"],
                "damages_crores_inr": row["Damages_Crores_INR"]
            },
            id=str(i)
        )

        ids.append(str(i))
        documents.append(document)

# Create Chroma vector store
vector_store = Chroma(
    collection_name="tn_floods",
    persist_directory=db_loc,
    embedding_function=embeddings
)

# Add documents if DB is being created for the first time
if exist:
    vector_store.add_documents(documents=documents, ids=ids)

# Set retriever for semantic search
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)
