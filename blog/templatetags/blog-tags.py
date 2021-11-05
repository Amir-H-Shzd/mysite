from django import template
from blog.models import Post
register = template.Library()


@register.simple_tag
def function():
    posts = Post.objects.filter()
    return posts
