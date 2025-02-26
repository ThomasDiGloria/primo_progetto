from django.urls import path
from .views import index, query_a, query_b

app_name = 'corsi_formazione'

urlpatterns = [
    path('index', index, name = "index_eventi"),
    path('query_a', query_a, name = "query_a"),
    path('query_b', query_b, name = "query_b"),
    
]