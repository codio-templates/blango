from django.contrib import admin

# Register your models here.
from blog.models import Tag, Post

admin.site.register(Tag)
admin.site.register(Post)
