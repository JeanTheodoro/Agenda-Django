from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from webdev.task.forms import TaskNewForm
from webdev.task.forms import TaskForm
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
            task_done = Task.objects.filter(done=True).all()
            return render(
                request, 'task/home.html', 
                {
                    'form':form, 
                    'task_bagger': task_bagger,
                    'task_done': task_done,
                    }, 
                    status=400)
    task_bagger = Task.objects.filter(done=False).all()  
    task_done = Task.objects.filter(done=True).all()
    return render(request, 'task/home.html',
                    {
                        'task_bagger': task_bagger,
                        'task_done':task_done,
                    })

def detail(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect(reverse('task:home'))

def delete(request, task_id):
    if request.method =='POST':
        Task.objects.filter(id=task_id).delete()
    return HttpResponseRedirect(reverse('task:home'))

