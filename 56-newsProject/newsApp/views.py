from django.shortcuts import render

def Home(request):
    return render(request=request, template_name='index.html')

def News(request):
    return render(request=request, template_name='news.html')
