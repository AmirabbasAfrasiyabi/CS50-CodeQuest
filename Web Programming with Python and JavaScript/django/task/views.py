from django.shortcuts import render

# Create your views here.
tasks = ["foo" , "bar" , "baz"]
def task (request):
    return render(request, 'task/index.html' , {
        "tasks" : tasks,
    })

def add(request):
    return render(request, 'task/add.html' , {})