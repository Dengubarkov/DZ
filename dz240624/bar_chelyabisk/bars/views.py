from django.shortcuts import render, get_object_or_404, redirect
from .models import Bars, News
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

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

def signupuser(request):
    if request.method == "GET":
        return render(request, 'bars/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'bars/signupuser.html',
                              {'form': UserCreationForm(),
                               'error': 'Такое имя пользователя существует-укажите другое!'})
        else:
            return render(request, 'bars/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Пароли не совпадают!'})

def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')

def loginuser(request):
    if request.method == "GET":
        return render(request, 'bars/loginuser.html', {'form':AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'bars/loginuser.html', {'form': AuthenticationForm, 'error':'Логин или пароль не верны!'})
        else:
            login(request, user)
            return redirect('index')