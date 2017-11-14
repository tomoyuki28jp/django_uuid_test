from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['uuid', 'body']


admin.site.register(Post, PostAdmin)

