from django.contrib import admin
from blog.models import Tag, Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
