from django.urls import path
from .views import homeNews, articoloDetailView, listaArticoli, queryBase, giornalistaDetailView
#query_base

app_name = 'news'

urlpatterns = [
    path('homeNews/', homeNews, name = "homeview1"),
    path("articolo_detail/<int:pk>/", articoloDetailView, name="articolo_detail"),
    path("lista_articoli/<int:pk>/", listaArticoli, name="lista_articoli"),
    path("lista_articoli/", listaArticoli, name="lista_articoli"),
    path("query/", queryBase, name="query"),
    path("giornalistaDetail/<int:pk>/", giornalistaDetailView, name="giornalista_detail")
    
]