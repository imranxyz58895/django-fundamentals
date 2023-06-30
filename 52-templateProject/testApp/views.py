from django.shortcuts import render

def sayHi(request):
    return render(request=request, template_name='testApp/index.html')

# Create your views here.
