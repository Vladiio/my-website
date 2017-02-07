from django.contrib import admin
from blog.models import Post, Category, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 2


class PostModel(admin.ModelAdmin):
    list_filter = ['post_date']
    inlines = [CommentInline]

admin.site.register(Post, PostModel)
admin.site.register(Category)
