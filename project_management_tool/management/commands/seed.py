```python
from django.core.management.base import BaseCommand
from project_management_tool.models import Project, Task, User
import random
import faker

class Command(BaseCommand):
    help = 'Seed the database with random data'

    def handle(self, *args, **options):
        fake = faker.Faker()

        # Create some users
        for _ in range(10):
            User.objects.create(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password()
            )

        # Create some projects
        for _ in range(5):
            Project.objects.create(
                name=fake.bs(),
                description=fake.text(),
                owner=random.choice(User.objects.all())
            )

        # Create some tasks
        for _ in range(20):
            Task.objects.create(
                name=fake.bs(),
                description=fake.text(),
                assignee=random.choice(User.objects.all()),
                project=random.choice(Project.objects.all()),
                status=random.choice(['TO DO', 'IN PROGRESS', 'DONE'])
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))
```