from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from book.forms import BookForm
from book.models import Book


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'book/create_book.html'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('create-book')
    permission_required = 'book.view_book'

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_book = form.save(commit=False)
            new_book.book_name = new_book.book_name.upper()
            new_book.save()
            return redirect('create-book')


class BookListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'book/list_of_books.html'
    model = Book
    context_object_name = 'all_books'
    permission_required = 'book.add_book'


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'book/update_book.html'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('list-of-books')
    permission_required = 'book.change_book'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'book/detail_book.html'
    model = Book
    permission_required = 'book.detail_b'


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = ''
    model = Book
    success_url = reverse_lazy('list-of-books')
    permission_required = 'book.delete_book'


@login_required
@permission_required('book.delete_book')
def delete_book(request, pk):
    Book.objects.filter(id=pk).delete()
    return redirect('list-of-books')
