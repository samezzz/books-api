from django.contrib import admin
from .models import Book

admin.site.site_header = "GraphQL"

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year_published', 'review')

# Register your models here.
admin.site.register(Book, BookAdmin) 