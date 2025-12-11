from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:day>', views.days_week_with_number, name='day-quotenumber'),
    path('<str:day>', views.days_week, name='day-quote')
]
