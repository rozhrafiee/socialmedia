from rest_framework import serializers
from .models import UserProfile, Post, Like, Comment
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'bio', 'profile_pic', 'following', 'followers']

class PostSerializer(serializers.ModelSerializer):
    total_likes = serializers.ReadOnlyField()
    
    class Meta:
        model = Post
        fields = ['id', 'user', 'caption', 'image', 'created_at']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'text', 'created_at']
