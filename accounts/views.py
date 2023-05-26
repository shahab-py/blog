from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer


class UserRegisterView(APIView):
    
    def post(self, request):
        
        srz_data = UserRegisterSerializer(data=request.POST)
        
        if srz_data.is_valid():
            srz_data.create(srz_data.validated_data)
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.error_messages, status=status.HTTP_400_BAD_REQUEST)
