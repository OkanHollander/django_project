from django.contrib import admin
from .models import Book, Author, Address, Country

# Register your classes here.
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'postal_code', 'city',)
    list_filter = ('street', 'postal_code', 'city',)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'rating',)
    list_display = ('title', 'rating', 'author', 'is_bestselling',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address'),
    list_filter = ('first_name', 'last_name', 'address',)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code',)
    list_filter = ('name', 'code',)

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country, CountryAdmin)
