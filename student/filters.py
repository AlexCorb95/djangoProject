import django_filters

from django import forms
from student.models import Student


class StudentFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains', label='Prenume')
    last_name = django_filters.CharFilter(lookup_expr='icontains', label='Nume')

    start_date_gte = django_filters.DateTimeFilter(field_name='start_date', lookup_expr='gte',
                                               widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))
    start_date_lte = django_filters.DateTimeFilter(field_name='start_date', lookup_expr='lte',
                                               widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))
    end_date_gte = django_filters.DateTimeFilter(field_name='end_date', lookup_expr='gte',
                                               widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))
    end_date_lte = django_filters.DateTimeFilter(field_name='end_date', lookup_expr='lte',
                                               widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'is_olympic', 'start_date_gte', 'start_date_lte', 'end_date_gte','end_date_lte',
                  'trainer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['first_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter a first name'})
        self.filters['last_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter a last name'})
        self.filters['age'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter age'})
        self.filters['is_olympic'].field.widget.attrs.update({'class': 'form-select'})
        # self.filters['start_date'].field.widget.attrs.update({'class': 'form-control'})
        # self.filters['end_date'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['trainer'].field.widget.attrs.update({'class': 'form-select'})
