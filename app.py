from flask import Flask, render_template, request
from rag_system import RAGSystem 
from data_loader import DataLoader 

app = Flask(__name__)
rag_system = RAGSystem()#make instance 

#initialize the rag system
@app.before_request
def initialize():
    print("Initializing RAG system...")
    data_loader = DataLoader()
    documents = data_loader.load_data()

    rag_system.vector_store.build_vector_store(documents)
    print("RAG system initialized")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        use_rag = 'use_rag' in request.form 
        response = rag_system.generate_response(query, use_rag)
        return render_template('index.html', response=response, query=query)
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)