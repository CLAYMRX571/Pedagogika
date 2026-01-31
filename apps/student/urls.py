from django.urls import path
from . import views

urlpatterns = [
    path('', views.Studentviews, name='student'),
]