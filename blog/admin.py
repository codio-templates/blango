from django.contrib import admin
from blog.models import Tag, Post, Comment

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('published_at', 'title')

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)