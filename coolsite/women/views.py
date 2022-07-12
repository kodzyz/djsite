from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    return HttpResponse("Страница приложения women.")


def categories(request, cat):
    if request.GET:
        print(request.GET)
    # http://127.0.0.1:8000/cats/music/?name=Gagarina&type=pop ->
    # -> QueryDict: {'name': ['Gagarina'], 'type': ['pop']}

    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{cat}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def archive(request, year):
    if int(year) > 2020:
        return redirect('/')  # временное перенаправление на главную Django
        # "GET /archive/2030/ HTTP/1.1" 302 0

    return HttpResponse(f'<h1>Архив по годам</h1>{year}</p>')
