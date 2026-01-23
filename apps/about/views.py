from django.shortcuts import render, redirect
from .models import About

def Aboutviews(request):
    about = list(About.objects.all())

    context = {
        'about': about,
    }

    return render(request, 'about.html', context)

def lan_switch_about(request, lan):
    return redirect(f'/{lan}/about/')