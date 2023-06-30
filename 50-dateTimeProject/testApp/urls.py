from django.urls import path 
from . import views

urlpatterns = [
	path('', views.dateTime, name='date-time'),
]