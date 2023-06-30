from . import views 
from django.urls import path 


urlpatterns = [
	path('', views.secondWish, name='second-wish'),
]