from django import template
from blog.models import Post
register = template.Library()


@register.simple_tag
def function():
    posts = Post.objects.filter()
    return posts


@register.simple_tag(name='plus')
def numfunction(a):
    return a + 2


@register.filter
def snippet(value):
    return value[:100]+'...'


@register.inclusion_tag('popularposts.html')
def popularposts():
    posts = Post.objects.filter(status=1).order_by('published_date')
    return {'posts': posts}
