from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='blog'),
    path('single/', single_view, name='single'),
    path('post-<int:pid>', test, name='test'),
]
