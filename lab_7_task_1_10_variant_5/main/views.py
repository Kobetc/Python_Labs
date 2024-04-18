from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('<h1>Главная страница</h1>')


def about(request):
    return HttpResponse('<h1>Страница о нас</h1>')
