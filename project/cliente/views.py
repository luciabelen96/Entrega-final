from django.shortcuts import render, redirect
from . import models
from . import forms
# Create your views here.

def index(request):
    return render(request, "cliente/index.html")

def profesor_list(request):
    consulta = models.Profesor.objects.all()
    contexto = {"profesores": consulta}
    return render(request, "cliente/Profesor_list.html" , contexto)
    
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect

from django.shortcuts import render, redirect

def profesor_creat(request):
    if request.method == "POST":
        form = forms.ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:index")
    else:
        form = forms.ProfesorForm()

    return render(request, "cliente/Profesor_creat.html", {"form": form})


def agregar_estudiante(request):
    if request.method == "POST":
        form = forms.EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:index")
    else:
        form = forms.EstudianteForm()

    return render(request, 'cliente/agregar_estudiante.html', {'form': form})

def ver_estudiante(request):
    consulta = models.Estudiante.objects.all()
    contexto = {"Estudiantes": consulta}
    print(contexto)  # Agrega esta línea para imprimir el contexto en la consola
    return render(request, "cliente/ver_estudiante.html" , contexto)


    