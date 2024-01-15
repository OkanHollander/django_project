from django.contrib import admin
from .models import Author, Post, Tag, Comment

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email_address")
    ordering = ["first_name", "last_name", "email_address"]
    search_fields = ["first_name", "last_name", "email_address"]
    list_filter = ["first_name", "last_name", "email_address"]

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", "slug")
    ordering = ["title", "author", "slug"]
    list_filter = ["title", "author", "slug"]

class TagAdmin(admin.ModelAdmin):
    ordering = ["caption"]
    list_filter = ["caption"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "user_name", "user_email",)
    ordering = ["user_name", "user_email", "content", "post"]
    list_filter = ["user_name", "user_email", "post"]
    search_fields = ["user_name", "user_email", "content",]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
