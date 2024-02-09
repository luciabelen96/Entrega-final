from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import *


def index(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")


class CustomLoginView(LoginView):
    template_name = 'core/login.html'  # Ajusta la ruta según tu estructura de carpetas
    success_url = reverse_lazy('index') 


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "core/index.html")
    else:
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form": form})