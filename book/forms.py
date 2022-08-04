from django import forms
from django.forms import TextInput

from book.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'book_name', 'author_first_name', 'author_last_name', 'book_year', 'book_type', 'book_rating',
            'book_quantity', 'book_description', 'image'
        ]

        widgets = {
            'book_name': TextInput(attrs={'placeholder': 'Please enter book name', 'class': 'form-control'}),
            'author_first_name': TextInput(
                attrs={'placeholder': 'Please enter author first name', 'class': 'form-control'}),
            'author_last_name': TextInput(
                attrs={'placeholder': 'Please enter author last name', 'class': 'form-control'}),
            'book_year': TextInput(attrs={'placeholder': 'Please enter book year', 'class': 'form-control'}),
            'book_type': TextInput(attrs={'placeholder': 'Please enter book type', 'class': 'form-control'}),
            'book_rating': TextInput(attrs={'placeholder': 'Please enter book rating', 'class': 'form-control'}),
            'book_quantity': TextInput(attrs={'placeholder': 'Please enter book quantity', 'class': 'form-control'}),
            'book_description': TextInput(
                attrs={'placeholder': 'Please enter a short description of the book', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = 'form-control'
