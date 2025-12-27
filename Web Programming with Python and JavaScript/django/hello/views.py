from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def brain(request , name):
    return HttpResponse(f"hello, {name.capitalize()}!")

def hello(request):
    return JsonResponse({'hello': 'world'})

def four_view(request):
    return render(request, 'four.html')

def greeting(request):
    return render(request, 'greeting.html' , {
        'name' : 'Greek',


    })

