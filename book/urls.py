from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from book import views, web_scraping

urlpatterns = [
    path('create_book/', views.BookCreateView.as_view(), name='create-book'),
    path('list_of_books/', views.BookListView.as_view(), name='list-of-books'),
    path('update_book/<int:pk>/', views.BookUpdateView.as_view(), name='update-book'),
    path('detail_book/<int:pk>/', views.BookDetailView.as_view(), name='detail-book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete-book'),
    path('emag_books', web_scraping.get_data_emag, name='emag-books')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)