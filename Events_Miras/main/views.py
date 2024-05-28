from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

# Create your views here.

def index(request):
    return render(request, 'main/index.html')