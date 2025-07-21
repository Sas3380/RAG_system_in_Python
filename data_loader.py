import pandas as pd 
from config import Config 

class DataLoader:
    def __init__(self):
        self.config = Config()

    def load_data(self):
        """load the data and preprocesses"""
        try:
            df = pd.read_csv(self.config.DATA_PATH)
            df = df.dropna(subset=['title', 'description'])
            df['text'] = df['title'] + "." + df['description']
            return df.to_dict('records')
        
        except Exception as e:
            print(f"Error while loading and preprocessing data: {e}")
            return []
        
        