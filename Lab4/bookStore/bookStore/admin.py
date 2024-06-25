from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'type', 'rate', 'views')
    search_fields = ('title', 'author_name', 'type')
    list_filter = ('type',)

admin.site.register(Book, BookAdmin)
