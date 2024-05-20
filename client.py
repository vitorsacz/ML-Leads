import requests
import json

# Dados do usuário
user_data = {
    "quantidade_funcionarios": 700,
    "tempo_mercado": 30,
    "utilizou_crm": 0,
    "tempo_navegacao_segundos":  2500
}


url = 'http://localhost:5000//api'

response = requests.post(url, json=user_data)

# Exibir a resposta
print(response.status_code)
print(response.json())

