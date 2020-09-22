from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer

from .models import Post


# Create your views here.

@api_view(['GET'])
def test(request):
    return Response("test is on")


@api_view(['GET'])
def postlist(request):
    posts = Post.objects.all()
    serializers = PostSerializer(posts, many=True)
    return Response(serializers.data)
