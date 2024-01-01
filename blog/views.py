from django.shortcuts import render

import logging
logger = logging.getLogger(__name__)
from blog.models import Post

# Create your views here.
def index(request):
    logger.info("Test 123 !!")
    posts = Post.objects.filter()
    logger.debug("Got %d posts", len(posts))

    return render(request, "blog/index.html")
