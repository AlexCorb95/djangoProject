from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from student.models import Student
from trainer.forms import TrainerForm
from trainer.models import Trainer


class TrainerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'trainer/create_trainer.html'
    model = Trainer
    form_class = TrainerForm
    success_url = reverse_lazy('create-trainer')
    permission_required = 'trainer.add_trainer'


class TrainerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'trainer/list_of_trainers.html'
    model = Trainer
    context_object_name = 'all_trainers'
    permission_required = 'trainer.view_trainer'


class TrainerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'trainer/update_trainer.html'
    model = Trainer
    form_class = TrainerForm
    success_url = reverse_lazy('list-of-trainers')
    permission_required = 'trainer.change_trainer'


class TrainerDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'trainer/detail_trainer.html'
    model = Trainer
    permission_required = 'trainer.detail_t'


class TrainerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'trainer/delete_trainer.html'
    model = Trainer
    success_url = reverse_lazy('list-of-trainers')
    permission_required = 'trainer.delete_trainer'


@login_required
@permission_required('trainer.delete_trainer')
def delete_trainer(request, pk):
    Trainer.objects.filter(id=pk).delete()
    return redirect('list-of-trainers')


def get_students_of_trainer(request, pk):
    return render(request, 'trainer/students_of_trainer.html',
                  {'students_per_trainer': Student.objects.filter(trainer_id=pk),
                   'details_trainer': Trainer.objects.get(id=pk)})
