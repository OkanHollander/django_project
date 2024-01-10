from django.contrib import admin
from .models import Author, Post, Tag

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

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
