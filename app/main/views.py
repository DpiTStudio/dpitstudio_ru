from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    con_text = {
        "title": "Главная страница сайта DPITSTUDIO",
        "content": "Добро пожаловать на главную страницу нашего сайта. Здесь вы можете найти информацию о нашем проекте и наших услугах. Если у вас есть какие-либо вопросы или пожелания, пожалуйста, свяжитесь с нами. Мы будем рады помочь вам.",
        "is_aut": True,
    }
    return render(request, "main/index.html", context=con_text)


def about(request) -> HttpResponse:
    con_text = {
        "title": "Страница о нас DPITSTUDIO",
        "content": "История нас и наши услуги",
        "is_aut": True,
    }
    return render(request, "main/about.html", context=con_text)
