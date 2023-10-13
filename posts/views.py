from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello post")


def comments_menu(request):
    return HttpResponse("Hello comments")
