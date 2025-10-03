from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class CustomUser(AbstractUser):
    class Meta:
        permissions = [
            ("view_eventos", "Puede ver la sección de eventos"),
            ("crear_evento", "Puede crear un evento"),
            ("editar_evento", "Puede editar un evento"),
            ("eliminar_evento", "Puede eliminar un evento"),
            ("asistir_evento", "Puede asistir a un evento"),
            ("ver_eventos_privados", "Puede ver eventos privados"),
        ]

class Evento(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo_evento = models.CharField(max_length=50)
    privado = models.BooleanField(default=False)
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


