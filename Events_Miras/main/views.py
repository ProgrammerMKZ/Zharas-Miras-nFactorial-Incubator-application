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
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, Registration_on_event
from .forms import Registration_on_event_form

# Create your views here.


@login_required
def Profile(request):
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        registration = get_object_or_404(Registration_on_event, event_id=event_id, user=request.user)
        registration.delete()
        messages.success(request, 'You have successfully unregistered from the event.')

    user_registrations = Registration_on_event.objects.filter(user=request.user).select_related('event')
    return render(request, 'main/Profile.html', {'registrations': user_registrations})

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
                return redirect('profile')
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
            messages.success(request, 'маладес')
            return render(request, 'main/registration_successful.html')
        else:
            messages.error(request, 'Регистрация не получилось')
            return render(request, 'main/registration.html', {'register_form': form})
    form = NewUserForm()
    return render(request, 'main/registration.html', {'register_form': form})

def index(request):
    events = Event.objects.all() 
    return render(request, 'main/index.html', {'events': events})

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = Registration_on_event_form(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.user = request.user
            registration.event = event
            registration.save()
            return redirect('main_page')
    else:
        form = Registration_on_event_form(initial={'event': event})
    return render(request, 'main/event_detail.html', {'form':form, 'event': event})

def Logout(request):
    logout(request)
    return redirect('main_page')
