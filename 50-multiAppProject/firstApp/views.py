from django.shortcuts import render, HttpResponse

def firstWish(request):
	return HttpResponse('Message from firstApp')
