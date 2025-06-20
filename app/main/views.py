from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    # return render(request, "index.html")
    return HttpResponse("Hello world index")


def about(request) -> HttpResponse:
    # return render(request, "about.html")
    return HttpResponse("Hello world about")
