from ast import Import
from django.contrib import admin
from django.urls import path
from . import views

# Ahora haremos que el usuario pueda acceder por medio del URL
# Para lograrlo agregar un path con los argumentos requeridos
# Path('tu_pagina/', tu_metodo_en_view.py)
# La URL sera la siguiente: http://127.0.0.1:8000/tu_pagina

urlpatterns = [
    path('registrarse/', views.registrar, name='registrarse'),
    path('guardarregistro/', views.guardarregistro, name='guardarregistro'),
]