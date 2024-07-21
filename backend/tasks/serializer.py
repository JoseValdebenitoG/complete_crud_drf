from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        # señalar el modelo a utilizar
        model = Task
        # Señalar los campos a leer dentro de una tupla
        #  fields = ('id', 'title', 'description', 'done')
        # tambien se pueden señalar todos los campos
        fields = '__all__'
