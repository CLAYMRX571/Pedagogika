from django.urls import path
from . import views

urlpatterns = [
    path('', views.Teamviews, name='team'),
]