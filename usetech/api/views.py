import jwt
import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from authentication.models import Client, Service, UserService


@api_view(['GET'])
def authentication(request):
    private_key_url = "http://keycloak:8080/realms/master"
    response = requests.get(private_key_url)
    public_key_data = '-----BEGIN PUBLIC KEY-----\n' + response.json()["public_key"] + '\n-----END PUBLIC KEY-----'
    jwt_token = request.headers['JWT']

    try:
        payload = jwt.decode(jwt_token, key=public_key_data, algorithms=['RS256'], audience='account')
    except Exception:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    try:
        client_id = Client.objects.get(client_id=payload["client_id"])
        service = Service.objects.get(url__icontains=request.headers['Original-URI'])
        UserService.objects.get(
                client=client_id,
                service=service
            )
    except Exception:
        return Response(status=status.HTTP_403_FORBIDDEN)

    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def service1(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def service2(request):
    return Response(status=status.HTTP_200_OK)
