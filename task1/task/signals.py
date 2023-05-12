"""
Signal handler for model Task with state validation
"""

from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver
from task.models import Task

STATE_TRANSITION = {
    'TO_DO': 'IN_PROGRESS',
    'IN_PROGRESS': 'DONE',
    'DONE': 'DONE'
}

def validate_state(current_state, previous_state):
    """
    State checker based on previous and current state
    """
    return STATE_TRANSITION.get(previous_state) == current_state

@receiver(pre_save,sender=Task)
def state_checker(sender,instance,**kwargs):
    """
    Checking for state validation before saving and returning error for invalid state
    """
    if instance.id is None:
        pass
    else:
        previous_state = Task.objects.get(pk=instance.pk).status
        if validate_state(instance.status,previous_state):
            pass
        else:
            raise ValidationError("state not valid")
