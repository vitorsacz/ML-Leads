import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np


app = Flask(__name__)
CORS(app)

# Carregar o modelo treinado
with open('model_lead.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
    print("Modelo carregado com sucesso")

@app.route('/')
def index():
    return "Server is running"


@app.route('/api', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    
    # Extrair os dados do JSON
    quantidade_funcionarios = data['quantidade_funcionarios']
    tempo_mercado = data['tempo_mercado']
    utilizou_crm = data['utilizou_crm']
    tempo_navegacao_segundos = data['tempo_navegacao_segundos']
    
    # Criar um array numpy com os dados
    input_data = np.array([[quantidade_funcionarios, tempo_mercado, utilizou_crm, tempo_navegacao_segundos]])
    
    # Fazer a predição
    prediction = model.predict(input_data)
    
    
    return jsonify({'lead': int(prediction[0])})


if __name__ == '__main__':
    app.run(debug=True)

    
