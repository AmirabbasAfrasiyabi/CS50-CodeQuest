from django.http import HttpResponse

from django import forms
from django.shortcuts import render

from django.urls import reverse

# Create your views here.
tasks = []

class TaskForm(forms.Form):
    task = forms.CharField(label = "NewTask")
    priority = forms.IntegerField(label = "NewPriority" , min_value=1 , max_value=10)

def index (request):
    return render(request, 'task/index.html' , {
        "tasks" : tasks,
    })

def add(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            tasks.append(task)
        else:
            return render(request, 'task/index.html' , {
                "form" : form,
            })
    return render(request, 'task/add.html' , {
        "form": TaskForm(),
    })

