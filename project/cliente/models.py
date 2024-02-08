from django.db import models

# Create your models here.

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"


class Curso(models.Model):
    curso = models.CharField(max_length=50)
    comision = models.PositiveBigIntegerField()
    id_profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.curso} {self.comision} - {self.id_profesor}"


class CursoEstudiantes(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.curso} {self.estudiante}"
