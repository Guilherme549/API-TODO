from rest_framework import viewsets

from app.models import Todo
from app.serializers import TodoSerializers


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
