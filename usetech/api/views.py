from authentication.models import Service, Client
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import jwt


@api_view(['GET'])
def authentication(request):
    print(request.headers['Service'])
    if request.headers['Service'] == 'bomba':
       return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def service1(request):
    print(request.META.get('HTTP_service'))
    return Response(status=status.HTTP_200_OK)
