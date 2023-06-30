from django.shortcuts import render, HttpResponse

def secondWish(request):
	return HttpResponse('Message from secondApp')