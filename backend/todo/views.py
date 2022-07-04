from rest_framework.viewsets import ModelViewSet
from .serializers import ToDoSerializer
from .models import ToDo


class TodoViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()