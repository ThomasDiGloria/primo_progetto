"""
URL configuration for primo_progetto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("prima_app.urls", namespace="prima_app")),
    path('admin/', admin.site.urls),
    path('', include("seconda_app.urls", namespace="seconda_app")),
    path('admin/', admin.site.urls),
    path('', include("news.urls", namespace="news")),
    path('admin/', admin.site.urls),
    path('', include("eventi_culturali.urls", namespace="eventi_culturali")),
    path('admin/', admin.site.urls),
    path('', include("forms_app.urls", namespace="forms_app")),
    path('admin/', admin.site.urls),
    path('', include("api.urls", namespace="api")),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]