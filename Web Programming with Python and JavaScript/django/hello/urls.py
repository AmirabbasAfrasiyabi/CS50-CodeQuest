from django.urls import path
from . import  views
urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.hello, name='hello'),
    path('hello/<str:name>', views.brain, name='brain'),
    path('hello/four', views.four_view, name='hello'),
    path('hello/greeting', views.greeting, name='greeting'),
]