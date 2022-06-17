"""APP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from ast import Import
from django.contrib import admin
from django.urls import path
from APP.views import inicio

# Ahora haremos que el usuario pueda acceder por medio del URL
# Para lograrlo agregar un path con los argumentos requeridos
# Path('tu_pagina/', tu_metodo_en_view.py)
# La URL sera la siguiente: http://127.0.0.1:8000/tu_pagina

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
]
