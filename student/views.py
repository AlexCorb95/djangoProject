from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from student.models import Student


class StudentCreateView(CreateView):
    template_name = 'student/create_student.html'
    model = Student
    #fields = '__all__'
    fields = ['first_name', 'last_name', 'age', 'is_olympic', 'address', 'email', 'description',
              'start_date', 'end_date']
    success_url = reverse_lazy('create-student')