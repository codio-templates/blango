from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from blog.models import Post


def components(request):
    return render(request, "blog/components.html")

def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/list_all.html" , {"posts": posts})

    