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
                'is_olympic': True,
                'year_of_birth': 1990,
            },
            {
                'first_name': 'Simona',
                'last_name': 'Leuca',
                'is_olympic': False,
                'year_of_birth': 1988,
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


def all_books(request):
    context = {
        "books": [
            {
                "first_name": "Jules",
                "last_name": "Verne",
                "title": "Insula Misterioasa",
                "is_read": True,
            },
            {
                "first_name": "Jules",
                "last_name": "Verne",
                "title": "O mie de leghe sub mari",
                "is_read": True
            },
            {
                "first_name": "Jules",
                "last_name": "Verne",
                "title": "Journey to the moon",
                "is_read": True
            }
        ]
    }
    return render(request, "intro/list_of_books.html", context)
