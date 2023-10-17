from django.urls import path

from posts.views import posts_menu, comments_menu

urlpatterns = [
    path('', posts_menu, name="posts"),
    path('comments/', comments_menu, name="comment_menu")
]