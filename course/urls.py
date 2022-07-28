from django.urls import path

from course import views

urlpatterns =[
    path('list_of_courses/', views.CourseListView.as_view(), name='list-of-courses')
]