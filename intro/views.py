from django.shortcuts import render
from django.http import HttpResponse


def show_name(request):
    return HttpResponse('hello,world')


def show_my_text(request):
    return HttpResponse('Hello, are you how?')


def all_students(request):
    context = {
        'students': [
            {
                'first_name': 'Alex',
                'last_name': 'Corb',
                'is_olympic': False,
                'year_of_birth': 1995,
            },
            {
                'first_name': 'Marius',
                'last_name': 'Ciufu',
                'is_olympic': True,
                'year_of_birth': 1975,
            },
            {
                'first_name': 'Ionel',
                'last_name': 'Leuca',
                'is_olympic': False,
                'year_of_birth': 1988,
            },
            {
                'first_name': 'Catalina',
                'last_name': 'Corb',
                'is_olympic': False,
                'year_of_birth': 2001,
            },
            {
                'first_name': 'Paula',
                'last_name': 'Vacuta',
                'is_olympic': True,
                'year_of_birth': 2005,
            },

        ]
    }
    return render(request, 'intro/list_of_students.html', context)
