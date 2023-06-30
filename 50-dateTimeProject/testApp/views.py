from . import views 
from datetime import datetime 
from django.shortcuts import render, HttpResponse


def dateTime(request):
	current_time = datetime.now()
	current_hour = int(datetime.time(current_time).strftime("%H"))

	if current_hour < 12:
		message = 'Good Morning'
	elif current_hour < 16:
		message = 'Good Afternoon'
	elif current_hour < 21:
		message = 'Good Evening'
	else:
		message = 'Good Night'

	greeting = (f'Hello Guys! very {message}. '
	f'Current time is {current_time.strftime("%H:%M:%S %p")}')

	return HttpResponse(f'<h2 style="text-align:center;">{greeting}</h2>')
