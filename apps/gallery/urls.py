from django.urls import path
from . import views

urlpatterns = [
    path('', views.Galleryviews, name='gallery'),
]