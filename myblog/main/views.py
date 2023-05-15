from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
# from .forms import LoginForm, RegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def index(request):
    data = {'title': 'Главная страница',
            'values': ['Some', 'Hello', '123']}
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session.set_expiry(0)
            return redirect('main_app:index')
        else:
            messages.error(request, 'Неправильное имя пользователя или пароль.')
    return render(request, 'registration/login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно. Вы можете войти.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
