from django.urls import path

from student import views

urlpatterns = [
    path('create_student/', views.StudentCreateView.as_view(), name='create-student'),
    path('list_of_students/', views.StudentListView.as_view(), name='list-of-students'),
    path('update_student/<int:pk>/', views.StudentUpdateView.as_view(), name='update-student'),
    path('detail_student/<int:pk>/', views.StudentDetaileView.as_view(), name='detail-student'),
    path('delete_student/<int:pk>/', views.StudentDeleteView.as_view(), name='delete-student'),
    path('delet_student_modal/<int:pk>/', views.delete_student, name='delete-student-modal'),
    path('inactive_student/<int:pk>/', views.inactive_student, name='inactive-student'),
    path('active_student/<int:pk>/', views.active_student, name='active-student'),
]
