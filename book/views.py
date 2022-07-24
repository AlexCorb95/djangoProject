from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from book.forms import BookForm
from book.models import Book


class BookCreateView(CreateView):
    template_name = 'book/create_book.html'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('create-book')


class BookListView(ListView):
    template_name = 'book/list_of_books.html'
    model = Book
    context_object_name = 'all_books'


class BookUpdateView(UpdateView):
    template_name = 'book/update_book.html'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('list-of-books')


class BookDetailView(DetailView):
    template_name = 'book/detail_book.html'
    model = Book


class BookDeleteView(DeleteView):
    template_name = ''
    model = Book
    success_url = reverse_lazy('list-of-books')


def delete_book(request, pk):
    Book.objects.filter(id=pk).delete()
    return redirect('list-of-books')
