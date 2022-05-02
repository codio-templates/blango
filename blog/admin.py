from django.contrib import admin
from blog.models import Tag, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('slug', 'published_at')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('value',)