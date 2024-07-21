'''
En este archivo creo las vistas que tendrá el crud
para crear o leer información
'''
from rest_framework import viewsets
from .serializer import ProjectSerializer
from .models import Project

# Crea el crud completo
class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


