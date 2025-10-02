from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Evento(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo_evento = models.CharField(max_length=50)
    privado = models.BooleanField(default=False)
    fecha = models.DateTimeField()
    organizador = models.ForeignKey(User, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

