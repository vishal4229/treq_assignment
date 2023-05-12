from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

# Models: Create a Django model named "Task" with the following fields: title (CharField),
# description (TextField), and status (CharField with choices). 
# The status field should have the following choices: 'TO_DO', 'IN_PROGRESS', 'DONE'.
task_choices = [('TO_DO','TO_DO'),
                ('IN_PROGRESS','IN_PROGRESS'),
                ('DONE','DONE')]

class Task(models.Model):
    title = models.TextField(blank=False,null=False)
    status = models.CharField(max_length=50,choices=task_choices,default=task_choices[0])
    

state_transition = { 
    'TO_DO':'IN_PROGRESS',
    'IN_PROGRESS':"DONE",
}

def validate_state(current_state,previous_state):
    is_valid = True
    if state_transition.get(previous_state,None) != current_state:
        is_valid = False
    return is_valid

@receiver(pre_save,sender=Task)
def state_checker(sender,instance,**kwargs):
    if instance.id is None:
        pass
    else:
        previous_state = Task.objects.get(pk=instance.pk).status
        if validate_state(instance.status,previous_state):
            pass
        else:
            raise Exception("state not valid")