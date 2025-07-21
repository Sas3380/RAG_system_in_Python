import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity 
import google.generativeai as genai 
from config import Config


class VectorStore:
    def __init__(self):
        self.config = Config()
        genai.configure(api_key=self.config.GEMINI_API_KEY)
        self.embedding_model = genai.GenerativeModel(self.config.EMBEDDING_MODEL)

        self.documents = []
        self.embeddings = []

    
    def embed_text(self, text):
        """embedding for a sinle text"""
        try:
            result = self.embedding_model.embed_content(text)
            return result['embedding']
        
        except Exception as e:
            print(f"Error embedding text: {e}")
            return None
        
    
    def build_vector_store(self, documents):
        """vector store for docs"""
        self.documents = documents 
        self.embeddings = []

        for doc in documents:
            embedding = self.embed_text(doc['text'])
            if embedding is not None:
                self.embeddings.append(embedding)

        self.embeddings = np.array(self.embeddings)
        print(f"Vector store built with {len(self.embeddings)} documents")

    
    def retrieve(self, query, top_k=None):
        """Retrieval for docs"""
        if top_k is None:
            top_k = self.config.TOP_K

        query_embedding = self.embed_text(query)
        if query_embedding is None:
            return []
        
        similarities = cosine_similarity(
            [query_embedding],
            self.embeddings
        )[0]

        top_indices = np.argsort(similarities)[-top_k][::1]
        return [self.documents[i] for i in top_indices]
    
