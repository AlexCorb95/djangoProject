from django import forms
from django.forms import TextInput, DateTimeInput
from trainer.models import Trainer


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['first_name', 'last_name', 'department', 'course', 'description', 'start_date', 'end_date']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'department': TextInput(attrs={'placeholder': 'Please enter your department', 'class': 'form-control'}),
            'course': TextInput(attrs={'placeholder': 'Please enter your course', 'class': 'form-control'}),
            'description': TextInput(attrs={'placeholder': 'Please enter a description', 'class': 'form-control'}),
            'start_date': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_date': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
