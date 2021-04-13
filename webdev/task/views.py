from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from webdev.task.forms import TaskNewForm
from django.urls import reverse
from webdev.task.models import Task

def home(request):
    if request.method == 'POST':
        form = TaskNewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task:home'))
        else:
            task_bagger = Task.objects.filter(done=False).all()
            return render(request, 'task/home.html', {'form':form, 'task_bagger': task_bagger}, status=400)
    task_bagger = Task.objects.filter(done=False).all()  
    return render(request, 'task/home.html', {'task_bagger': task_bagger})
