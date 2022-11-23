from django.db import connections
from django.db import models

class Persona(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cedula = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    tel_usuario = models.CharField(max_length=10)
    nombre_usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    id_rol = models.CharField(max_length=20)
    class Meta:
        db_table='persona'