from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework import viewsets

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


@api_view(['POST'])
def postCreate(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
