import json
from http import HTTPStatus

from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from blog.models import Post
from blog.api.serializers import PostSerializer


def post_to_dict(post):
    return {
        "pk": post.pk,
        "author_id": post.author_id,
        "created_at": post.created_at,
        "modified_at": post.modified_at,
        "published_at": post.published_at,
        "title": post.title,
        "slug": post.slug,
        "summary": post.summary,
        "content": post.content,
    }


@csrf_exempt
def post_list(request):
    if request.method == "GET":
      posts = Post.objects.all()
      return JsonResponse({"data": PostSerializer(posts, many=True).data})
    elif request.method == "POST":
      serializer = PostSerializer(data=post_data)
      serializer.is_valid(raise_exception=True)
      post = serializer.save()


    return HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "GET":
      return JsonResponse(PostSerializer(post).data)
    elif request.method == "PUT":
      serializer = PostSerializer(post, data=post_data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return HttpResponse(status=HTTPStatus.NO_CONTENT)
    elif request.method == "DELETE":
        post.delete()
        return HttpResponse(status=HTTPStatus.NO_CONTENT)
    return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])
