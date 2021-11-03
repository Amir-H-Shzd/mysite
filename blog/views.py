from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone


def blog_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def single_view(request, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, id=pid)

    nextPost = Post.objects.filter(
        published_date__gt=post.published_date).order_by('published_date').first()
    prevPost = Post.objects.filter(
        published_date__lt=post.published_date).order_by('published_date').last()

    # context = {'post': post}

    
    # count viewer by reloading (first not compelete model)
    # post.views = post.views + 1
    #     post.save()

    # count each specific user but cant view new post only read one post
    # if not request.session.get('counted'):
    #     post.views = post.views + 1
    #     post.save()
    #     context = {'post': post}
    #     request.session['counted'] = True

    # this views structure count specific viewer of each post
    if (request.session.get(str(post.id), False) == False):
        request.session[str(post.id)] = True
        post.views += 1
        post.save()
    return render(request, 'blog/blog-single.html',  {'post': post, 'nextpost': nextPost, 'prevpost': prevPost})


def test(request, pid):
    # post = Post.objects.get(status=1)
    post = get_object_or_404(Post, id=pid)
    context = {'post': post}
    return render(request, 'test.html', context)
