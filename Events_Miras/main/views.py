from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.shortcuts import render, redirect
import requests

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def login_to_account(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return render(request, 'main/index.html')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form":form})

def register_to_account(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request)
            messages.success(request, 'маладес')
            return render(request, 'main/registration_successful.html')
        else:
            messages.error(request, 'Регистрация не получилось')
            return render(request, 'main/registration.html', {'register_form': form})
    form = NewUserForm()
    return render(request, 'main/registration.html', {'register_form': form})