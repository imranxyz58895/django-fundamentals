from django.shortcuts import render, HttpResponse

# Create your views here.
def hydJobs(request):
	return HttpResponse(
		"<h1 style='text-align: center; font-family: operator mono;'>Hello, Jobs Board from Hyderbad </h1>"
	)

def puneJobs(request):
	return HttpResponse(
		"<h1 style='text-align: center; font-family: operator mono;'>Hello, Jobs Board from Pune </h1>"
	)

def chennaiJobs(request):
	return HttpResponse(
		"<h1 style='text-align: center; font-family: operator mono;'>Hello, Jobs Board from Chennai </h1>"
	)

def mumbaiJobs(request):
	return HttpResponse(
		"<h1 style='text-align: center; font-family: operator mono;'>Hello, Jobs Board from Mumbai </h1>"
	)
