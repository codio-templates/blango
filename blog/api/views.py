from rest_framework import generics

from blog.api.serializers import PostSerializer, UserSerializer
from blog.models import Post
from blog.api.permission import AuthorModifyOrReadOnly
from blango_auth.models import User
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser
from blog.api.serializers import PostSerializer, UserSerializer, PostDetailSerializer



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     permission_classes = [AuthorModifyOrReadOnly]
#     serializer_class = PostSerializer
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly ]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    authentication_classes = [SessionAuthentication]
    serializer_class = UserSerializer



