from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

# Crea las tablas.
class Task(models.Model):
    # Cada elemento es una columna de la tabla
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # CASCADE nos sirva para eliminar las tareas asociadas a un proyecto si lo eliminamos.
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' > ' + self.project.name + ' > ' + self.user.username
