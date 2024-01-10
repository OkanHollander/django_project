from django.contrib import admin
from .models import Book, Author

# Register your classes here.
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'rating',)
    list_display = ('title', 'rating', 'author', 'is_bestselling')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name',)

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
