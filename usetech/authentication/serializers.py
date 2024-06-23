from rest_framework import serializers


class RequestSerializer(serializers.Serializer):
    client_id = serializers.CharField(max_length=256)
