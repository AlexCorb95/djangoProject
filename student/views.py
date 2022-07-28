from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from student.filters import StudentFilter
from student.forms import StudentForm
from student.models import Student
from trainer.models import Trainer


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'student/create_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('create-student')
    permission_required = 'student.add_student'


class StudentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students'
    permission_required = 'student.view_student'

    # def get_queryset(self):
    #     return Student.objects.filter(active=True)

    def get_context_data(self, **kwargs): #getting data from other tables
        data = super(StudentListView, self).get_context_data(**kwargs)

    #     all_trainers = Trainer.objects.all()
    #     data['trainers'] = all_trainers
    #
        students = Student.objects.all()
        myFilter = StudentFilter(self.request.GET, queryset=students)
        data['all_students'] = myFilter.qs
        data['my_filter'] = myFilter
        return data



class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('list-of-students')
    permission_required = 'student.update_s'


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'student/detail_student.html'
    model = Student
    permission_required = 'student.detail_s'


''


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list-of-students')
    permission_required = 'student.delete_s'


@login_required
@permission_required('student.delete_s')
def delete_student(request, pk):
    Student.objects.filter(id=pk).delete()
    return redirect('list-of-students')


@login_required
@permission_required('student.inactivate_student')
def inactive_student(request, pk):
    Student.objects.filter(id=pk).update(active=False)
    return redirect('list-of-students')


@login_required
def active_student(request, pk):
    Student.objects.filter(id=pk).update(active=True)
    return redirect('list-of-students')
