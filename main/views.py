from django.shortcuts import render, HttpResponse
from main.models import *

def landing(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
    return render(request, "landing.html")
