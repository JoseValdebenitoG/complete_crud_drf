
'''
Aqui se selecciona los campos en que los datos serán
pasados a JSON
'''
from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

