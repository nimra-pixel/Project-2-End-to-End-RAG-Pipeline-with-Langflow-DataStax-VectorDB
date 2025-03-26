import os
import requests
from fastapi import FastAPI, HTTPException
from langflow import process_text
from datastax_vector import DataStaxVectorStore

# Initialize FastAPI
app = FastAPI()

# Initialize DataStax Vector Database
vector_store = DataStaxVectorStore(api_key=os.getenv("DATASTAX_API_KEY"))

@app.post("/query")
def query_rag_pipeline(input_text: str):
    """Processes user input through the RAG pipeline using Langflow & DataStax."""
    try:
        processed_text = process_text(input_text)
        response = vector_store.query(processed_text)
        return {"query": input_text, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
