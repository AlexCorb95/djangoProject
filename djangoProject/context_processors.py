from django.shortcuts import render

from trainer.models import Trainer


def get_all_trainers(request):
    return {'trainers': Trainer.objects.all()}

