from django.db import models
# Create your models here.

# Models: Create a Django model named "Task" with the following fields: title (CharField),
# description (TextField), and status (CharField with choices). 
# The status field should have the following choices: 'TO_DO', 'IN_PROGRESS', 'DONE'.


TASK_CHOICES = [('TO_DO','TO_DO'),
                ('IN_PROGRESS','IN_PROGRESS'),
                ('DONE','DONE')]

class Task(models.Model):
    title = models.TextField(blank=False,null=False)
    status = models.CharField(max_length=50,choices=TASK_CHOICES,default=TASK_CHOICES[0])
    
