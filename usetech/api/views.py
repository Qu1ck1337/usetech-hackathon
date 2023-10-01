from authentication.models import Service, Client, UserService
import requests
import json
from requests.adapters import HTTPAdapter, Retry
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import jwt
from django.http import HttpResponse


@api_view(['GET'])
def authentication(request):
    '''
    Service.objects.create(url='http://localhost:8080/service1/')
    Service.objects.create(url='http://localhost:8080/service2/')
    client = Client(client_id='popich')
    client.save()
    UserService.objects.bulk_create([
        UserService(
            client=Client.objects.get(client_id='popich'),
            allowed_service=Service.objects.get(url='http://localhost:8080/service1/')
        )
    ])
    '''
    print(Service.objects.all(), Client.objects.all(), UserService.objects.all())
    private_key_url = "http://keycloak:8080/realms/master"
    response = requests.get(private_key_url)
    public_key_data = '-----BEGIN PUBLIC KEY-----\n' + response.json()["public_key"] + '\n-----END PUBLIC KEY-----'
    jwt_token = request.headers['JWT']
    try:
        print(request.headers['Original-URI'])
        payload = jwt.decode(jwt_token, key=public_key_data, algorithms=['RS256'], audience='account')
        client_id = Client.objects.get(client_id=payload["client_id"])
        service = Service.objects.get(url__icontains=request.headers['Original-URI'])
        UserService.objects.get(
            client=client_id,
            service=service
        )
    except Exception as e:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def service1(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def service2(request):
    return Response(status=status.HTTP_200_OK)

