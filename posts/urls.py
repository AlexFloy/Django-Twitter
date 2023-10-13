from django.urls import path

from posts.views import index, comments_menu

urlpatterns = [
    path('posts/', index, name="index"),
    path('comments/', comments_menu, name="comment_menu")
]