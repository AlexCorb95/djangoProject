import django_filters
from django import forms

from trainer.models import Trainer


class TrainerFilter(django_filters.FilterSet):
    class Meta:
        model = Trainer
        fields = ['first_name',  'last_name']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.filters['first_name'].field.widget.attrs.update({'class': 'form-select'})
        self.filters['last_name'].field.widget.attrs.update({'class': 'form-select'})
