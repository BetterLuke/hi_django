from rest_framework import serializers


class CreateOneCompanyDtoSerializer(serializers.Serializer):
    companyName = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)
