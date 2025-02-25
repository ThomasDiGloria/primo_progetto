import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Corso

def index(request):
    return render(request, "indexC.html")

def query_a(request):
    query_a = Corso.objects.order_by('data_inizio');
     

    context = {
        'query_a': query_a,
    }
    
    return render(request,'view_a.html',context)
