from django.shortcuts import render

def home(request):
    return render(request, 'view_once/index.html')
