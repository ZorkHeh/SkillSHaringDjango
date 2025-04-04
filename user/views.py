from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate

from user.forms import UserForm

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')

        if form.is_valid():
            User.objects.create_user(username=username, password=password)

            return redirect('index')

    if request.method == 'GET':
        form = UserForm()

        return render(request, 'register.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if form.is_valid():
            login(request, user=user)
            return redirect('index')

    if request.method == 'GET':
        form = UserForm()

        return render(request, 'login.html', {'form': form})

def log_out(request):
    logout(request)

    return redirect('index')
