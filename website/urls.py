from django.urls import path
from website.views import test, json

urlpatterns = [
    path('test/', test),
    path('json/', json)
]
