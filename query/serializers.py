from rest_framework import serializers
from .models import Post


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'description','file_name','created_on')
