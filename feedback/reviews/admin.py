from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_name','review_text', 'rating',)
    list_filter = ('user_name','review_text', 'rating',)
    search_fields = ('user_name',)

admin.site.register(Review, ReviewAdmin)
