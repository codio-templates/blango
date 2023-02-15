from rest_framework import generics

from blog.api.serializers import PostSerializer
from blog.models import Post

from rest_framework.authentication import SessionAuthentication

class PostList(generics.ListCreateAPIView):
    # only be accessible to those authenticated by the session,
    # authentication_classes = [SessionAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer