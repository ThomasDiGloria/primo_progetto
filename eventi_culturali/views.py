import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Evento

def index(request):
    return render(request, "indexE.html")
