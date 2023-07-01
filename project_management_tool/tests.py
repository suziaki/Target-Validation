from django.test import TestCase
from .models import Project, Task, User

class ProjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='testuser', password='testpassword')
        Project.objects.create(name='Test Project', description='This is a test project', owner=User.objects.get(id=1))

    def test_project_content(self):
        project = Project.objects.get(id=1)
        expected_object_name = f'{project.name}'
        self.assertEquals(expected_object_name, 'Test Project')

class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='testuser', password='testpassword')
        Project.objects.create(name='Test Project', description='This is a test project', owner=User.objects.get(id=1))
        Task.objects.create(title='Test Task', description='This is a test task', project=Project.objects.get(id=1), assignee=User.objects.get(id=1))

    def test_task_content(self):
        task = Task.objects.get(id=1)
        expected_object_name = f'{task.title}'
        self.assertEquals(expected_object_name, 'Test Task')