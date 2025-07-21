import os 
from dotenv import load_dotenv 

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    DATA_PATH = 'data/news_data_dedup.csv'
    EMBEDDING_MODEL = 'models/embedding-001'
    GENERATION_MODEL = 'gemini-2.5-flash'
    TOP_K = 5
    CHUNK_SIZE = 1000  