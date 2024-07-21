from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializer import TaskSerializer
from .models import Task

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    #  permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
