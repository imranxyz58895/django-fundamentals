from django.shortcuts import render


def home(request):
    return render(request=request, template_name='testApp/index.html', context={'title': 'Home Page'})


def profile(request):
    return render(request=request, template_name='testApp/profile.html', context={'title': 'Profile Page'})