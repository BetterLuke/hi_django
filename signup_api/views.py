from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.request import Request

from signup_api.serializers import CompanySerializer


# Create your views here.
class Companies(generics.GenericAPIView):
    serializer_class = CompanySerializer

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": {"company": serializer.data}},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"status": "error", "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
