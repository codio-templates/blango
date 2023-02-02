from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include

from blog.api.views import PostList, PostDetail

from rest_framework.authtoken import views

urlpatterns = [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token)
]