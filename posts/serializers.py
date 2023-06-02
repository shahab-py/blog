from rest_framework import serializers

from .models import Post, Comment



class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'content'
        )
        
        
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = (
            'title',
            'content',
            'comment',
            'reply'
        )