from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ["title", "price"]
    search_fields = ["title"]


admin.site.register(Book, BookAdmin)
