from django.shortcuts import render
# from .models import Post
from django.utils import timezone
from blog.models import Post

# Create your views here.
# def index(request):
#     return render(request, "blog/index.html")
def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})
