from django.shortcuts import render
from django.http import HttpResponse


# def Home_view(request):
#     return HttpResponse('<h1>Home</h1>')


# def Home_view(request):
#     return render(request, 'home.html')


def Home_view(request):
    return render(request, 'website/home.html')
    # Note: if you added a folder in templates folder
    # you need to change the address from 'home.html' to 'foldername/home.html'


def Contact_view(request):
    return render(request, 'website/contact.html')


def About_us_view(request):
    return render(request, 'website/about.html')
