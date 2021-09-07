from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def test(request):
    return HttpResponse('<h1>Hi Amir Hossein</h1>')


def json(request):
    return JsonResponse({'name': 'Amir Hossein'})
