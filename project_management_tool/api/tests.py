```python
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.views import status
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer

# initialize the APIClient app
client = APIClient()

class BaseViewTest(TestCase):
    def setUp(self):
        # add test data
        self.first_project = Project.objects.create(name="First project", description="This is the first project")
        self.second_project = Project.objects.create(name="Second project", description="This is the second project")
        self.first_task = Task.objects.create(name="First task", description="This is the first task", project=self.first_project)
        self.second_task = Task.objects.create(name="Second task", description="This is the second task", project=self.second_project)

class GetAllProjectsTest(BaseViewTest):

    def test_get_all_projects(self):
        """
        This test ensures that all projects added in the setUp method
        exist when we make a GET request to the projects/ endpoint
        """
        # hit the API endpoint
        response = client.get(
            reverse("projects-all")
        )
        # fetch the data from db
        expected = Project.objects.all()
        serialized = ProjectSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetAllTasksTest(BaseViewTest):

    def test_get_all_tasks(self):
        """
        This test ensures that all tasks added in the setUp method
        exist when we make a GET request to the tasks/ endpoint
        """
        # hit the API endpoint
        response = client.get(
            reverse("tasks-all")
        )
        # fetch the data from db
        expected = Task.objects.all()
        serialized = TaskSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
```