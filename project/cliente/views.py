from django.shortcuts import render, redirect
from . import models
from . import forms
# Create your views here.

def index(request):
    return render(request, "core/index.html")

def profesor_list(request):
    consulta = models.Profesor.objects.all()
    contexto = {"profesores": consulta}
    return render(request, "core/Profesor_list.html" , contexto)
    
def profesor_creat(request):
    if request.method == "POST":
        form = forms.ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profesor-list")  # Ajusta el nombre según tu configuración de URL
    else:
        form = forms.ProfesorForm()

    return render(request, "core/Profesor_creat.html", {"form": form})

def agregar_estudiante(request):
    if request.method == 'POST':
        form = forms.EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver-estudiante')  # Ajusta 'lista_estudiantes' con el nombre de tu vista de lista de estudiantes
    else:
        form = forms.EstudianteForm()

    return render(request, 'core/agregar_estudiante.html', {'form': form})

def ver_estudiante(request):
    consulta = models.Estudiante.objects.all()
    contexto = {"Estudiantes": consulta}
    return render(request, "core/ver_estudiante.html" , contexto)

    