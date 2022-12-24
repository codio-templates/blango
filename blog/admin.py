from django.contrib import admin
from blog.models import Tag, Post

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('summary', 'content')

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)