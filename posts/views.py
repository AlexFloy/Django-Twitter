from django.shortcuts import render
from django.http import HttpResponse

from posts.models import Post, Comments


def posts_menu(request, user_name=None):
    if user_name:
        posts = Post.objects.filter(user__user_name=user_name)
    else:
        posts = Post.objects.all()

    context = {'post': posts}

    return render(request, 'posts/posts_list.html', context)


def comments_menu(request):
    comment = Comments.objects.all()
    context = {'comments': comment}
    return render(request, 'posts/comments_menu.html', context)
