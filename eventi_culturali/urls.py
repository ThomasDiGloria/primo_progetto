from django.urls import path
from .views import index, query_a, query_b, query_c, query_d, query_e, query_f

app_name = 'eventi_culturali'

urlpatterns = [
    path('index', index, name = "index_eventi"),
    path('query_a', query_a, name = "query_a"),
    path('query_b', query_b, name = "query_b"),
    path('query_c', query_c, name = "query_c"),
    path('query_d', query_d, name = "query_d"),
    path('query_e', query_e, name = "query_e"),
    path('query_f', query_f, name = "query_f"),
    
]