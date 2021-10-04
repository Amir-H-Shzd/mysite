from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone


def blog_view(request):
    # posts = Post.objects.filter(status=1)
    posts = Post.objects.filter(published_date__lte=timezone.now())
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def single_view(request, pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post, id=pid)
    post.views = post.views + 1
    post.save()
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)


def test(request, pid):
    #post = Post.objects.get(id=pid)
    post = get_object_or_404(Post, id=pid)
    context = {'post': post}
    return render(request, 'test.html', context)
