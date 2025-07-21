# 🌟 News RAG System with Gemini API  

A modern **Retrieval-Augmented Generation (RAG)** system that fetches and summarizes the latest news using **Google's Gemini AI**. Perfect for staying updated without reading dozens of articles!  

---

## 🛠 Tech Stack & APIs  

### Core Tech  
- **Backend**: Python (Flask)  
- **Frontend**: HTML5, CSS3, JavaScript  
- **AI Engine**: Google Gemini API  
- **Vector Search**: Cosine similarity (scikit-learn)  

### Key Dependencies  
| Package | Purpose | Version |
|---------|---------|---------|
| `google-generativeai` | Gemini API access | >=0.3.0 |
| `Flask` | Web framework | >=2.0.0 |
| `python-dotenv` | Environment management | >=0.19.0 |
| `scikit-learn` | Vector similarity | >=1.0.0 |

---

## 💾 Storage Architecture  
- **Data Storage**: Local CSV files (`news_data_dedup.csv`)  
- **Vector Cache**: In-memory NumPy arrays  
- **Session Data**: Flask server memory
- **vectorDB**: Planning to add this also.

> 🚀 No external databases required - runs entirely locally for now!

---

## 🚀 Getting Started  

### Installation  
 -- Make sure to first create .env file in the main directory and store there your Gemini API key with name GEMINI_API_KEY
```bash
# Clone repository
git clone https://github.com/yourusername/news-rag-gemini.git
cd news-rag-gemini

# Install dependencies
pip install -r requirements.txt
