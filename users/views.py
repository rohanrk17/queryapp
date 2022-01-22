from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication import models
from authentication.serializers import  UserSerializer

# Create your views here.

class UserRolesView(APIView):
    
    def get(self, request, role=None):
        if role:
            users = models.CustomUser.objects.get(role=role)
            serializer = UserSerializer(users)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"status": "No records"}, status=status.HTTP_400_BAD_REQUEST)   
