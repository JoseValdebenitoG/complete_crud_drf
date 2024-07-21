'''
En este archivo creamos los modelos de la base de datos,
cada class que creamos será una tabla de la base de datos
'''
from django.db import models
from django.contrib.auth.models import User

# Creamos las tablas


class Project(models.Model):
    # Con los campos de las tablas
    name = models.CharField(max_length=200)
    #  user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Podemos devolver el nombre del proyecto para mostrarlo en el front
    def __str__(self):
        return self.name


