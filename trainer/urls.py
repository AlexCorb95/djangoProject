from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from trainer import views

urlpatterns = [
    path('create_trainer/', views.TrainerCreateView.as_view(), name='create-trainer'),
    path('list_of_trainers/', views.TrainerListView.as_view(), name='list-of-trainers'),
    path('update_trainer/<int:pk>/', views.TrainerUpdateView.as_view(), name='update-trainer'),
    path('detail_trainer/<int:pk>/', views.TrainerDetailView.as_view(), name='detail-trainer'),
    path('delete_trainer/<int:pk>/', views.TrainerDeleteView.as_view(), name='delete-trainer'),
    path('delete_trainer_modal/<int:pk>/', views.delete_trainer, name='delete-trainer-modal'),
    path('students_of_trainer/<int:pk>/', views.get_students_of_trainer, name='students-of-trainer'),
    path('list_of_trainer_api/', views.TrainerApiView.as_view(), name='list-of-trainer-api')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)