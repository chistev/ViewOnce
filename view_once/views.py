from django.shortcuts import render

def home(request):
    return render(request, 'view_once/index.html')

def features(request):
    return render(request, 'view_once/features.html')

def pricing(request):
    return render(request, 'view_once/pricing.html')

def support(request):
    return render(request, 'view_once/support.html')

def login_view(request):
    return render(request, 'view_once/login.html')

def dashboard(request):
    return render(request, 'view_once/dashboard.html')

def terms(request):
    return render(request, 'view_once/terms.html')

def privacy(request):
    return render(request, 'view_once/privacy.html')

def links(request):
    return render(request, 'view_once/links.html')

def analytics(request):
    return render(request, 'view_once/analytics.html')