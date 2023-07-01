```python
from rest_framework import viewsets
from .serializers import ProjectSerializer, TaskSerializer
from project_management_tool.models import Project, Task

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
```