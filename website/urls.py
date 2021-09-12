from django.urls import path
from website.views import Elements_view, Home_view, Contact_view, About_us_view

app_name = 'website'

urlpatterns = [
    path('', Home_view, name='home'),
    path('contact/', Contact_view, name='contact'),
    path('about/', About_us_view, name='about'),
    path('element/', Elements_view, name='element')
]
