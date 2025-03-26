import os
import requests

class DataStaxVectorStore:
    """Handles interactions with DataStax VectorDB."""
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://datastax-vector.com/api"

    def query(self, text):
        """Queries the vector database and retrieves the best match."""
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.post(f"{self.base_url}/query", json={"query": text}, headers=headers)
        return response.json()
