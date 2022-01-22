from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib import auth
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer,LoginSerializer
from rest_framework.permissions import IsAuthenticated


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            get_user_model().objects.create_user(**serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            serializer = UserSerializer(user)

            data = {'user': serializer.data}

            return Response(data, status=status.HTTP_200_OK)

            # failure
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

