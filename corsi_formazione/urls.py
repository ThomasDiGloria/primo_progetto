from django.urls import path
from .views import index, query_a

app_name = 'corsi_formazione'

urlpatterns = [
    path('index', index, name = "index_corsi"),
    path('query_a', query_a, name = "query_a"),
    
]