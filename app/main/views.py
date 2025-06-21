from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        "title": "Главная страница сайта DPITSTUDIO",
        "content": "Добро пожаловать на главную страницу нашего сайта. Здесь вы можете найти информацию о нашем проекте и наших услугах. Если у вас есть какие-либо вопросы или пожелания, пожалуйста, свяжитесь с нами. Мы будем рады помочь вам.",
        "list": ["first", "second"],
        "dict": {"first": 1},
        "is_aut": False,
    }
    return render(request, "main/index.html", context=context)


def about(request) -> HttpResponse:
    return render(request, "about.html")
