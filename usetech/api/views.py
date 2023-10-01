from authentication.models import Service, Client
import requests
from requests.adapters import HTTPAdapter, Retry
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import jwt


@api_view(['GET'])
def authentication(request):
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    private_key_url = "http://localhost:8080/realms/master"
    response = session.get(private_key_url)
    public_key_data = '-----BEGIN PUBLIC KEY-----\n' + response.json()["public_key"] + '\n-----END PUBLIC KEY-----'
    jwt_token = request.headers['JWT']
    try:
        payload = jwt.decode(jwt_token, key=public_key_data, algorithms=['RS256'], audience='account')
        print(payload["client_id"])
    except Exception:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def service1(request):
    return Response(status=status.HTTP_200_OK)
