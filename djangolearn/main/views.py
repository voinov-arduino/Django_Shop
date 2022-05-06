from django.shortcuts import render
from .models import Task, News
from django.contrib.auth.models import User
from django import forms
from .models import UserRegistrationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import LoginForm

def index(request):
    Newss = News.objects.order_by('-id')
    return render(request, 'main/index.html', {'NewsTitle':'Новости', 'Newss':Newss })


def about(request):
    return render(request, 'main/about.html')


def product(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/product.html', {'title':'Продукты', 'tasks': tasks})


def price(request):
    return render(request, 'main/price.html')


def support(request):
    return render(request, 'main/support.html')


def cart(request):
    return render(request, 'main/basket.html')


def login(request):
    return render(request, 'main/login.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'main/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Успешный вход')
                else:
                    return HttpResponse('Аккаунт выключен администратором')
            else:
                return HttpResponse('Неверные данные')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})




