from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django_girls.blog.forms import PostForm
from django_girls.blog.models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    posts = Post.objects.filter(author=request.user).order_by('-published_date')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        return redirect('/post/new')
    else:
        form = PostForm()
    context = {
        'form': form,
        'posts': posts
    }
    return render(request, 'blog/post_new.html', context)


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    posts = Post.objects.filter(author=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect('/post/new/')
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
        'posts': posts
    }
    return render(request, 'blog/post_new.html', context)


def post_delete(request, pk):
    Post.objects.get(pk=pk).delete()
    return redirect('/post/new/')
