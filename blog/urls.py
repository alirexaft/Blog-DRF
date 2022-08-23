from django.urls import path
from .views import AllPosts, CreatePost, UpdatePost, MyPosts, DestroyPost, MyPostDetail

urlpatterns = [
    path('posts/<int:pk>/', AllPosts.as_view()),
    path('myposts/', MyPosts.as_view()),
    path('myposts/<int:pk>/', MyPostDetail.as_view()),
    path('posts/create/', CreatePost.as_view()),
    path('posts/delete/<int:pk>/', DestroyPost.as_view()),
    path('posts/update/<int:pk>/', UpdatePost.as_view()),
]
