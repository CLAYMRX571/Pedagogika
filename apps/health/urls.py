from django.urls import path
from . import views

urlpatterns = [
    path('', views.HealthViews, name='health'),
]