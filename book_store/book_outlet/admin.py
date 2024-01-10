from django.contrib import admin
from .models import Book

# Register your classes here.
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}



# Register your models here.
admin.site.register(Book, BookAdmin)