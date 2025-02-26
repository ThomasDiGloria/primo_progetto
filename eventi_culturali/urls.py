from django.urls import path
from .views import index, query_a, query_b, query_c, query_d

app_name = 'corsi_formazione'

urlpatterns = [
    path('index', index, name = "index_eventi"),
    path('query_a', query_a, name = "query_a"),
    path('query_b', query_b, name = "query_b"),
    path('query_c', query_c, name = "query_c"),
    path('query_d', query_d, name = "query_d"),
    
]