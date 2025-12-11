from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from datetime import date

def home(request):
    today = date.today()
    stack = [
        {'id': 'python', 'name': 'Python'},
        {'id': 'django', 'name': 'Django'},
        {'id': 'php', 'name': 'Php'},
        {'id': 'js', 'name': 'Js'}
    ]
    return render(request,'landing/landing.html',{
        'name': 'Gerardo',
        'dia': today,
        'edad': '44',
        'stack': stack
    })

def stack_detail(request, tool):
    return HttpResponse(f'Tecnologia: {tool}')