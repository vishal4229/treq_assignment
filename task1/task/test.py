from task.models import Task


t1 = Task(title='abc',status='TO_DO')
t1.save()

t1.status='IN_PROGRESS'
t1.save()

t1.status="DONE"
t1.save()

from django.test import TestCase

class TestTask(TestCase):
    def test_to_do(self):
        