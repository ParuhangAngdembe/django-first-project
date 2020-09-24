from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet)
router.register('category', views.categoryViewSet)

urlpatterns = [

    path('post-list/', views.postlist, name='post-list'),
    path('post-detail/<str:pk>/', views.postDetail, name='post-detail'),
    path('post-create/', views.postCreate, name='post-create'),
    path('post-update/<str:pk>/', views.postUpdate, name='post-update'),
    path('post-delete/<str:pk>/', views.postDelete, name='post-delete'),

    path('category-list/', views.categoryList, name='category-list'),
    path('category-detail/<str:pk>/', views.categoryDetail, name='category-detail'),
    path('category-create/', views.categoryCreate, name='category-create'),
    path('category-update/<str:pk>/', views.categoryUpdate, name='category-update'),
    path('category-delete/<str:pk>/', views.categoryDelete, name='category-delete'),

    path('', include(router.urls)),


]
