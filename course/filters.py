import django_filters
from django import forms
from course.models import Module


class ModuleFilter(django_filters.FilterSet):
    name_of_course = django_filters.CharFilter(lookup_expr='icontains', label='Course name')
    start_date_gte = django_filters.DateTimeFilter(field_name='start_date', lookup_expr='gte',
                                                   widget=forms.DateTimeInput(
                                                       attrs={'type': 'datetime-local', 'class': 'form-control'}))
    start_date_lte = django_filters.DateTimeFilter(field_name='start_date', lookup_expr='lte',
                                                   widget=forms.DateTimeInput(
                                                       attrs={'type': 'datetime-local', 'class': 'form-control'}))
    end_date_gte = django_filters.DateTimeFilter(field_name='end_date', lookup_expr='gte',
                                                 widget=forms.DateTimeInput(
                                                     attrs={'type': 'datetime-local', 'class': 'form-control'}))
    end_date_lte = django_filters.DateTimeFilter(field_name='end_date', lookup_expr='lte',
                                                 widget=forms.DateTimeInput(
                                                     attrs={'type': 'datetime-local', 'class': 'form-control'}))

    class Meta:
        model = Module
        fields = ['name_of_course', 'name_of_trainer', 'course_duration', 'start_date_gte', 'start_date_lte',
                  'end_date_gte',
                  'end_date_lte']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['name_of_trainer'].field.widget.attrs.update({'class': 'form-select'})

        self.filters['course_duration'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter course duration'})
