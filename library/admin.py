from django.contrib import admin
from .models import Book, BookCopy, Borrowing

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn']
    search_fields = ['title', 'isbn']

class BookCopyAdmin(admin.ModelAdmin):
    list_display = ['book', 'copy_number', 'status']
    search_fields = ['book__title']

class BorrowingAdmin(admin.ModelAdmin):
    list_display = ['user', 'book_copy', 'borrow_date', 'due_date', 'fine']
    search_fields = ['user__username', 'book_copy__book__title']

admin.site.register(Book, BookAdmin)
admin.site.register(BookCopy, BookCopyAdmin)
admin.site.register(Borrowing, BorrowingAdmin)