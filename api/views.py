from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import PostSerializer, CategorySerializer, TagSerializer

from .models import Post, Category, Tag

@api_view(['GET'])
def postlist(request):
    posts = Post.objects.all()
    serializers = PostSerializer(posts, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def postDetail(request, pk):
    posts = Post.objects.get(id = pk)
    serializers = PostSerializer(posts, many=False)
    return Response(serializers.data)

@api_view(['POST'])
def postCreate(request):
    serializers = PostSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
def postUpdate(request, pk):
    posts = Post.objects.get(id=pk)
    serializers = PostSerializer(instance= posts,data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def postDelete(request, pk):
    posts = Post.objects.get(id=pk)
    posts.delete()
    return Response("item deleted")

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



#------------------------------------category

@api_view(['GET'])
def categoryList(request):
    category = Category.objects.all()
    serializers = CategorySerializer(category, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def categoryDetail(request, pk):
    category = Category.objects.get(id = pk)
    serializers = CategorySerializer(category, many=False)
    return Response(serializers.data)

@api_view(['POST'])
def categoryCreate(request):
    serializers = CategorySerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
def categoryUpdate(request, pk):
    category = Category.objects.get(id=pk)
    serializers = CategorySerializer(instance= category,data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def categoryDelete(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return Response("category deleted")

class categoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer






