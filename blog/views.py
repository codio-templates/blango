from django.shortcuts import render
# from .models import Post
from django.utils import timezone
from blog.models import Post

import logging
logger = logging.getLogger(__name__)
from blog.models import Post
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.utils import timezone

# Create your views here.

# def index(request):
#     return render(request, "blog/index.html") 
# @cache_page(300)
# @vary_on_headers("Cookie")
# def index(request):
#     from django.http import HttpResponse
#     return HttpResponse(str(request.user).encode("ascii"))
#     posts = Post.objects.filter(published_at__lte=timezone.now())
#     logger.debug("Got %d posts", len(posts))
#     return render(request, "blog/index.html", {"posts": posts})


def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now()).select_related("author")

    # posts = (
    # Post.objects.filter(published_at__lte=timezone.now())
    # .select_related("author")
    # .defer("created_at", "modified_at")
# )




    # logger.debug("Got %d posts", (posts))
    return render(request, "blog/index.html", {"posts": posts})


def get_ip(request):
  from django.http import HttpResponse
  return HttpResponse(request.META['REMOTE_ADDR'])

