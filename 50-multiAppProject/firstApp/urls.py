from . import views 
from django.urls import path 


urlpatterns = [
	path('', views.firstWish, name='second-wish'),
]