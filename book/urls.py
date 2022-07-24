from django.urls import path

from book import views

urlpatterns = [
    path('create_book/', views.BookCreateView.as_view(), name='create-book'),
    path('list_of_books/', views.BookListView.as_view(), name='list-of-books'),
    path('update_book/<int:pk>/', views.BookUpdateView.as_view(), name='update-book'),
    path('detail_book/<int:pk>/', views.BookDetailView.as_view(), name='detail-book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete-book')
]