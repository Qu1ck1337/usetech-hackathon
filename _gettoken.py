import requests

# Замените следующие значения на свои
server_url = "http://localhost:8080/"
realm_name = "master"
client_id = "popich"
client_secret = "LAtTOPDeVt3gv5BnJzGd0ukNiKI5p2HI"

# Получите токен
data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "client_credentials"
}
token_response = requests.post(f"{server_url}/realms/{realm_name}/protocol/openid-connect/token", data=data)
jwt_token = token_response.json().get('access_token')
print(jwt_token)