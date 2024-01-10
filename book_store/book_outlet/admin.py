from django.contrib import admin
from .models import Book

# Register your classes here.
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'rating',)
    list_display = ('title', 'rating', 'author', 'is_bestselling')



# Register your models here.
admin.site.register(Book, BookAdmin)