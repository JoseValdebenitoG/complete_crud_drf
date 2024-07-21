from django.contrib.auth.models import Group, User
# importa los modulos para generar los viewsets
from rest_framework import permissions, viewsets
# importa los serializers
from .serializer import GroupSerializer, UserSerializer

'''
crea los viewsets, que son endpoints que permite que los datos de la base
sean vistos y editados
'''
class UserViewSet(viewsets.ModelViewSet):
    # consulta a la base de datos por todos los usuarios
    queryset = User.objects.all().order_by('-date_joined')
    # clase de serializers a utilizar
    serializer_class = UserSerializer
    # clase de permisos a utilizar
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
