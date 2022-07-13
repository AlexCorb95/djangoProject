from django.shortcuts import render
from django.http import HttpResponse

def show_name(request):
    return HttpResponse('hello,world')

def show_my_text(request):
    return HttpResponse('Hello, are you how?')