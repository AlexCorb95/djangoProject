from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

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


class StudentUpdateView(UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('list-of-students')


class StudentDetaileView(DetailView):
    template_name = 'student/detail_student.html'
    model = Student


class StudentDeleteView(DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list-of-students')


def delete_student(request, pk):
    Student.objects.filter(id=pk).delete()
    return redirect('list-of-students')


def inactive_student(request, pk):
    Student.objects.filter(id=pk).update(active=False)
    return redirect('list-of-students')


def active_student(request, pk):
    Student.objects.filter(id=pk).update(active=True)
    return redirect('list-of-students')