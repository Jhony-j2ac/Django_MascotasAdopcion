from django.db import models

# Create your models here.
class Persona(models.Model):

    nombre = models.CharField(max_length = 50);
    apellido = models.CharField(max_length = 50);
    edad = models.IntegerField();
    telefono = models.BigIntegerField();
    email = models.TextField();
    domicilio = models.TextField(max_length = 50);

    def __str__(self):
        return '{}'.format(self.nombre);

class solicitud(models.Model):

    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE);
    numero_mascotas = models.IntegerField();
    razones = models.TextField();
    
    