from django.shortcuts import render

def es_if(request):
    context = {
        'var1' : 200,
        'var2' : 200,
        'var3' : 300,
    }
    return render(request, "es_if.html", context)

def if_esle_elif(request):
    context = {
        'var1' : 100,
        'var2' : 100.0,
        'var3' : 100.50,
    }
    return render(request, "if_esle_elif.html", context)
