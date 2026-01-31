from django.shortcuts import render, redirect
from .models import Brain

def Brainviews(request):
    brain = Brain.objects.all()

    context = {
        'brain': brain,
    }

    return render(request, 'brain.html', context)

def lan_switch_brain(request, lan):
    return redirect(f'/{lan}/brain/')