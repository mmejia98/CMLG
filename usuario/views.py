from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

import usuario

# Create your views here.

def registrar(request):
    form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

def guardarregistro(request):
    form = UserCreationForm(request.POST)
    if(form.is_valid()):
        usuario = form.save()
        login(request, usuario)
        return redirect('inicio')
    else:
        for msg in form.error_messages:
            messages.error(request, form.error_messages[msg])
        
        return render(request, 'registration/registro.html', {'form': form})

