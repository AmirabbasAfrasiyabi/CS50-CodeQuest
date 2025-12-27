from django.shortcuts import render
import datetime
# Create your views here.

def index(request):
    n = datetime.datetime.now()
    return render(request, 'newyears/index.html' , {
        "newyears" : n.month == 1 and n.day == 1,
    })
