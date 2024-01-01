from django.shortcuts import render

import logging
logger = logging.getLogger(__name__)
from blog.models import Post
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from datetime import timezone

# Create your views here.
# @cache_page(300)
# @vary_on_headers("Cookie")
# def index(request):
#     from django.http import HttpResponse
#     return HttpResponse(str(request.user).encode("ascii"))
#     posts = Post.objects.filter(published_at__lte=timezone.now())
#     logger.debug("Got %d posts", len(posts))
#     return render(request, "blog/index.html", {"posts": posts})


def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    logger.debug("Got %d posts", len(posts))
    return render(request, "blog/index.html", {"posts": posts})


