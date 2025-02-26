import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Evento

def index(request):
    return render(request, "indexE.html")

def query_a(request):
    query_a = Evento.objects.order_by('data_inizio');
    context = {
        'query_a': query_a,
    }
    return render(request,'view_a.html',context)

def query_b(request):
    eventi = Evento.objects.all()
    context = {"eventi": eventi}
    print(context)
    return render(request, "view_b.html", context)
