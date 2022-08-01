import django_filters
from django.shortcuts import render, redirect
from django.views.generic import ListView

from course.filters import ModuleFilter
from course.models import Module
from trainer.models import Trainer
from trainer.views import TrainerListView


class CourseListView(ListView):
    template_name = 'course/list_of_courses.html'
    model = Module
    context_object_name = 'all_courses'

    def get_context_data(self, **kwargs):
        data = super(CourseListView, self).get_context_data(**kwargs)

        courses = Module.objects.all()
        myFilter = ModuleFilter(self.request.GET, queryset=courses)
        data['all_courses'] = myFilter.qs
        data['my_filter'] = myFilter

        return data
