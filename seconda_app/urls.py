from django.contrib import admin
from django.urls import path, include
from seconda_app.views import es_if, if_esle_elif, es_for

app_name="seconda_app"

urlpatterns = [
     path('es_if',es_if,name='es_if'),
     path('if_esle_elif',if_esle_elif,name='if_esle_elif'),
     path('es_for', es_for,name='es_for')
]