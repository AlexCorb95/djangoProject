from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from trainer.forms import TrainerForm
from trainer.models import Trainer


class TrainerCreateView(CreateView):
    template_name = 'trainer/create_trainer.html'
    model = Trainer
    form_class = TrainerForm
    success_url = reverse_lazy('create-trainer')