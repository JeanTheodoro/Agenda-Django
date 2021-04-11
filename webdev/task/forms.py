from django.forms import ModelForm
from webdev.task.models import Task    


class TaskNewForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name']
    
