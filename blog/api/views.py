from rest_framework import generics

from blog.api.serializers import PostSerializer
from blog.models import Post


from rest_framework.authentication import SessionAuthentication

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    authentication_classes = [SessionAuthentication]
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
