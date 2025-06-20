from django.shortcuts import render

def home(request):
    return render(request, 'view_once/index.html')

def features(request):
    return render(request, 'view_once/features.html')

def pricing(request):
    return render(request, 'view_once/pricing.html')
