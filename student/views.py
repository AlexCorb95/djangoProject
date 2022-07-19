from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from student.forms import StudentForm
from student.models import Student


class StudentCreateView(CreateView):
    template_name = 'student/create_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('create-student')

class StudentListView(ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students'