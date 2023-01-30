from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.
from django.db import models
from django.conf import settings

from django.contrib.contenttypes.fields import GenericRelation

class Tag(models.Model):
    value = models.TextField(max_length=100)

    def __str__(self):
        return self.value

class Comment(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    # above method will let them both be null or have a vlue at the same time 
    # and that wrong so we will change
    #to let just point to one of them
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    #content_object = GenericForeignKey()
    content_object = GenericForeignKey("content_type", "object_id")



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    title = models.TextField(max_length=100)
    slug = models.SlugField()
    summary = models.TextField(max_length=500)
    content = models.TextField()
    
    tags = models.ManyToManyField(Tag, related_name="posts")

    comments = GenericRelation(Comment)

    def __str__(self):
        return self.title

