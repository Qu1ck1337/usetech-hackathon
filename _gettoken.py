import requests

# Замените следующие значения на свои
server_url = "http://localhost:8080/"
realm_name = "master"
client_id = ['popich', 'bombastik', 'vova']
client_secret = ["tLRb9CTNa4RGBmDi9WI0BhpSRWnlBmT1", 'ECznp37WSqeZH16GhRjNF7ZXeFZ4W7Jl', 'ZdiA7itJCoQ13UPtIZf1KNWrYBWeLWzG']

# Получите токен
data = {
    "client_id": client_id[2],
    "client_secret": client_secret[2],
    "grant_type": "client_credentials"
}
token_response = requests.post(f"{server_url}/realms/{realm_name}/protocol/openid-connect/token", data=data)
jwt_token = token_response.json().get('access_token')
print(jwt_token)