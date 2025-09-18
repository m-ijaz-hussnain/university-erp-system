from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, BookCopy, Borrowing
from .forms import BookForm, BookCopyForm, BorrowingForm

@login_required
def manage_books(request):
    books = Book.objects.all()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_books')
    else:
        form = BookForm()
    return render(request, 'library/book_list.html', {'books': books, 'form': form})

@login_required
def manage_borrowing(request):
    borrowings = Borrowing.objects.filter(user=request.user)
    if request.method == 'POST':
        form = BorrowingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_borrowing')
    else:
        form = BorrowingForm()
    return render(request, 'library/borrowing.html', {'borrowings': borrowings, 'form': form})