from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('features/', views.features, name='features'),
    path('pricing/', views.pricing, name='pricing'),
    path('support/', views.support, name='support'),
]
