from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from trainer.forms import TrainerForm
from trainer.models import Trainer


class TrainerCreateView(CreateView):
    template_name = 'trainer/create_trainer.html'
    model = Trainer
    form_class = TrainerForm
    success_url = reverse_lazy('create-trainer')


class TrainerListView(ListView):
    template_name = 'trainer/list_of_trainers.html'
    model = Trainer
    context_object_name = 'all_trainers'

class TrainerUpdateView(UpdateView):
    template_name = 'trainer/update_trainer.html'
    model = Trainer
    form_class = TrainerForm
    success_url = reverse_lazy('list-of-trainers')

class TrainerDetailView(DetailView):
    template_name = 'trainer/detail_trainer.html'
    model = Trainer


class TrainerDeleteView(DeleteView):
    template_name = 'trainer/delete_trainer.html'
    model = Trainer
    success_url = reverse_lazy('list-of-trainers')

def delete_trainer(request, pk):
    Trainer.objects.filter(id=pk).delete()
    return redirect('list-of-trainers')