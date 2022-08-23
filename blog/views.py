from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsAuthorOrAdminOrReadonly
from .models import Post
from .serializers import PostSerializer


class CreatePost(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UpdatePost(UpdateAPIView):
    permission_classes = (IsAuthenticated, IsAuthorOrAdminOrReadonly)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DestroyPost(DestroyAPIView):
    permission_classes = (IsAuthenticated, IsAuthorOrAdminOrReadonly)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AllPosts(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class MyPosts(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.filter(author=self.request.user)
        return queryset


class MyPostDetail(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.filter(author=self.request.user)
        return queryset
