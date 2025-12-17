from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

days_of_week = {
     'lunes': 'nunca dejes de aprender',
    'martes': 'lee diario',
    'miercoles': 'lucha por tus sueños',
    'jueves': 'no tengas niedo a cometer errores es normal cometerlos',
    'viernes': 'un ganador es un perdedor que no dejo de intentarlo',
    'sabado': 'se 1% mejor cada dia',
    'domingo': 'eres grandioso'
}

def index(request):
    days = list(days_of_week.keys())
    return render(request,"quotes/quotes.html", {
        "days": days
    })



def days_week_with_number(request, day):
    days = list(days_of_week.keys())
    if day > len(days):
        return HttpResponseNotFound('<h1>El dia no existe</h1>')
    redirect_day = days[day-1]
    redirect_path = reverse('day-quote', args=[redirect_day])
    return HttpResponseRedirect(redirect_path)

def days_week(request, day):
    try:
        quote_text = days_of_week[day]
        return HttpResponse(quote_text)
    except Exception:
        return HttpResponseNotFound('Este dia no existe')
