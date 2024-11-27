from django.contrib import admin
from django.urls import path, include
from seconda_app.views import es_if

app_name="seconda_app"

urlpatterns = [
     path('es_if',es_if,name='es_if'),
]