from django.urls import path

from intro import views

urlpatterns = [
    path('first_page/', views.show_name, name='first_page'),
    path('second_page/', views.show_my_text, name='second_page'),
    path('all_students/', views.all_students, name='all-students'),
]
