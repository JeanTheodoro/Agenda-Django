from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from webdev.task.forms import TaskNewForm
from django.urls import reverse

def home(request):
    if request.method == 'POST':
        form = TaskNewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task:home'))
        else:
          return render(request, 'task/home.html', {'form':form}, status=400)  
    return render(request, 'task/home.html')
