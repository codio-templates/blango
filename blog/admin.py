from django.contrib import admin
from blog.models import Tag, Post, Comment


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('value',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('creator', 'content')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('author', 'title', 'slug', 'published_at')