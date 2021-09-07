from django.shortcuts import render
from django.http import HttpResponse


def Home_view(request):
    return HttpResponse('<h1>Home</h1>')


def Contact_view(request):
    return HttpResponse('<h1>Contact</h1>')


def About_us_view(request):
    return HttpResponse('<h1>About us</h1>')
