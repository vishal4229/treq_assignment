from django.test import TestCase
from django.core.exceptions import ValidationError
from task.models import Task

class TaskTestCase(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title='abc',status='TO_DO')

    def test_task_in_progress(self):
        self.task.status = "IN_PROGRESS"
        self.assertIsNone(self.task.save())
    
    def test_task_done(self):
        self.task.status = "DONE"
        self.assertIsNone(self.task.save())
    
    def test_task_done_error(self):
        self.task.status = "TO_DO"
        self.assertEqual(ValidationError,self.task.save())
    
    def test_task_done_again(self):
        self.task.status = "DONE"
        self.assertIsNone(self.task.save())
        