import google.generativeai as genai
from config import Config 
from vector_store import VectorStore

class RAGSystem:
    def __init__(self):
        self.config = Config()
        genai.configure(api_key=self.config.GEMINI_API_KEY)
        self.vector_store = VectorStore()
        self.generation_model = genai.GenerativeModel(self.config.GENERATION_MODEL)

    def format_docs(self, documents):
        """format docs to include in user prompt(query)"""
        formatted = []
        for doc in documents:
            formatted.append(
                f"Title: {doc['title']},\n Description: {doc['description']}\n, Published: {doc['published_at']},\n URL: {doc['url']}\n"
            )
        
        return "\n".join(formatted)
    

    def generate_prompt(self, query, documents):
        """prompt with query"""
        context = self.format_docs(documents)

        return f"""
        You are a helpful assistant that answers questions using the provided context.
        Context: {context},
        Question: {query},
        Answer: 
        """
        
    def generate_response(self, query, use_rag=True):
        """generate response"""
        if use_rag:
            documents = self.vector_store.retrieve(query)
            prompt = self.generate_prompt(query, documents)

        else:
            prompt = query 

        try:
            response = self.generation_model.generate_content(prompt)
            return response.text 
        
        except Exception as e:
            return f"Error while generating response: {e}"
