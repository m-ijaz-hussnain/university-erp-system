from django import forms
from .models import Book, BookCopy, Borrowing

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn']

class BookCopyForm(forms.ModelForm):
    class Meta:
        model = BookCopy
        fields = ['book', 'copy_number', 'status']

class BorrowingForm(forms.ModelForm):
    class Meta:
        model = Borrowing
        fields = ['user', 'book_copy', 'borrow_date', 'due_date', 'return_date', 'fine']