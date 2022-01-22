from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib import auth
from rest_framework.generics import GenericAPIView
from .serializers import QuerySerializer
from .models import Post
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from query import models

# Create your views here.
class QueryView(GenericAPIView):
    serializer_class = QuerySerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = QuerySerializer(data=request.data)
        if serializer.is_valid():
            Post.objects.create(**serializer.validated_data)
            #Uncomment below code once smtp is configured
            # subject = 'Query posted by {}'.format(serializer.validated_data['author'])
            # message = 'Hi {}, thank you for post query will provide proper response as soon posible.'.format(serializer.validated_data['author'])
            # send_mail( subject, message, settings.EMAIL_HOST_USER, [serializer.validated_data['author'],])
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

class UserPostsView(APIView):
    serializer_class = QuerySerializer
    permission_classes = (IsAuthenticated, )
    
    def get(self, request, email=None):
        if email:
            posts = models.Post.objects.get(author=email)
            serializer = QuerySerializer(posts, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        posts = models.Post.objects.all()
        serializer = QuerySerializer(posts, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)   
