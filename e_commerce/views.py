from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {
        "title": "Home Page",
        "content": "Bem-vindo a pagina principal"
    }
    return render(request, "home_page.html", context)


def about(request):
    context = {
        "title": "About Page",
        "content": "Bem-vindo a pagina Sobre"
    }
    return render(request, "about/view.html", context)


def contato(request):
    context = {
        "title": "Pagina de contato",
        "content": "Bem-vindo a pagina Contato"
    }
    return render(request, "contato/view.html", context)
