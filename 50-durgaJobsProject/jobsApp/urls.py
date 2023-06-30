from . import views
from django.urls import path

urlpatterns = [
	path('job/hyd/', views.hydJobs, name='hydjob'),
	path('job/pune/', views.puneJobs, name='punejob'),
	path('job/chennai/', views.chennaiJobs, name='chennaijob'),
	path('job/mumbai/', views.mumbaiJobs, name='mumbaijob'),
]