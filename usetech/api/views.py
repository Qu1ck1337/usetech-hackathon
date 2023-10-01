from authentication.models import Service, Client
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import jwt


@api_view(['GET'])
def authentication(request):
    public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAukToMbbOi6ntGRYuSzcVRZiv2hI/mSZ3sT3huUT33v8x6XgB7HGw37irfdaFBcN5Rbxtb9/cDdOHM0hKyKNKvUktsqjPTnaGe8CDJUGtLWamLgGBYAabKyln1tMxFi2+qV9FU87IOit213/HYz/pEfQNl+z2C9ht+mitpB/BmyakOPhVov9oa0g7aVLrMaAfVmaadeGjDxAvFvHFI9vdaLhu50Q1Dyr3gVbnC5xIT9o3GV3Lh3O/EntvxUaytLyeZPfQ3jv50gWZePuaGFdlm+1Av4Od2Fw7NAO+xCnOltROrJBqylGDV/I5/LfAJC3YF3e3kQv/SqCKLY4l5Cx08QIDAQAB'
    public_key_data = '-----BEGIN PUBLIC KEY-----\n' + public_key + '\n-----END PUBLIC KEY-----'
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
