from django import forms
from django.forms import TextInput, EmailInput, DateTimeInput, Select

from student.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'is_olympic', 'address', 'email', 'description', 'trainer',
                  'start_date', 'end_date']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'age': TextInput(attrs={'placeholder': 'Please enter your age', 'class': 'form-control'}),
            'address': TextInput(attrs={'placeholder': 'Please enter your age', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your address', 'class': 'form-control'}),
            'description': TextInput(attrs={'placeholder': 'Please enter a description', 'class': 'form-control'}),
            'start_date': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_date': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'trainer': Select(attrs={'class': 'form-select'}),
        }
