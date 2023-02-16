from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.
from django.db import models
from django.conf import settings

from django.contrib.contenttypes.fields import GenericRelation

class Tag(models.Model):
    value = models.TextField(max_length=100, unique=True)
    #posts = tags fix me
    def __str__(self):
        return self.value

class Comment(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True)
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    # above method will let them both be null or have a vlue at the same time 
    # and that wrong so we will change
    #to let just point to one of them
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(db_index=True)
    #content_object = GenericForeignKey()
    content_object = GenericForeignKey("content_type", "object_id")



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    #DB OPtimization
    published_at = models.DateTimeField(blank=True, null=True, db_index=True)
    
    title = models.TextField(max_length=100)
    slug = models.SlugField(unique=True)
    summary = models.TextField(max_length=500)
    content = models.TextField()
    
    tags = models.ManyToManyField(Tag, related_name="posts")

    comments = GenericRelation(Comment)

    def __str__(self):
        return self.title

class AuthorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    bio = models.TextField()

    def __str__(self):
        return f"{self.__class__.__name__} object for {self.user}"