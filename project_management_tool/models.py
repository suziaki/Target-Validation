```python
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    users = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = (
        ('TO_DO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TO_DO')
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='tasks', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
```