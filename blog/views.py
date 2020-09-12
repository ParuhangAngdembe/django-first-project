from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse
posts = [
    {'author':'paruhang',
     'title': 'Blog post 1',
     'content': 'first post content',
     'date_posted': 'August 27, 2020'
     }, #dictionary
    {'author': 'paruhang',
     'title': 'Blog post 2',
     'content': 'second post content',
     'date_posted': 'August 28, 2020'
     }
]


def home( request ):
    context ={
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about( request ):
    return render(request, 'blog/about.html')

