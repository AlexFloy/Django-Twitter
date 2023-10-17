from django.shortcuts import render
from django.http import HttpResponse

from posts.models import Post, Comments


def posts_menu(request):
    post = Post.objects.all()
    context = {'post': post}
    return render(request, 'posts/posts_list.html', context)


def comments_menu(request):
    comment = Comments.objects.all()
    context = {'comments': comment}
    return render(request, 'posts/comments_menu.html', context)
