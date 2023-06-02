from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Post
from .serializers import PostSerializer

class PostView(APIView):
    
    def get(self, request):
        posts = Post.objects.all()
        srz_data = PostSerializer(posts, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        srz_data = PostSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status = status.HTTP_400_BAD_REQUEST)
