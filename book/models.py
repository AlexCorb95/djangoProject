from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=45)
    author_first_name = models.CharField(max_length=30)
    author_last_name = models.CharField(max_length=30)
    book_year = models.CharField(max_length=4)
    book_type = models.CharField(max_length=30)
    book_rating = models.DecimalField(max_digits=4, decimal_places=2)
    book_available = models.BooleanField(default=True)
    book_quantity = models.IntegerField()
    book_description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book_name}-{self.author_first_name} {self.author_last_name}"
