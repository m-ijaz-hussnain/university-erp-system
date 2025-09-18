from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title

class BookCopy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copy_number = models.IntegerField()
    status = models.CharField(max_length=10, choices=[('available', 'Available'), ('borrowed', 'Borrowed')])

class Borrowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    fine = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)