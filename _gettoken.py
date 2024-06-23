import requests
import os
from dotenv import load_dotenv

load_dotenv()

server_url = "http://localhost:8080/"
realm_name = "master"
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "client_credentials"
}

token_response = requests.post(f"{server_url}/realms/{realm_name}/protocol/openid-connect/token", data=data)
jwt_token = token_response.json().get('access_token')
print(jwt_token)
