from django.shortcuts import render, get_object_or_404
from .models import Bars, News

title = "Бары Челябинска"


def index(request):
    bar = Bars.objects.all()
    return render(request, 'bars/index.html', {'bar': bar})


def news(request):
    news = News.objects.all()
    return render(request, 'bars/news.html', {'news': news})
    # news = News.objects.all()
    # return request(request, 'bars/index.html', {'news': news})


def selectnew(request, new_id):

    new = get_object_or_404(News, pk=new_id)
    return render(request, 'bars/new.html', {'new': new})
