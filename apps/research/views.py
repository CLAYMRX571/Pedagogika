from django.shortcuts import render, redirect
from .models import Research

def Researchviews(request):
    research = Research.objects.all()

    context = {
        'research': research,
    }

    return render(request, 'research.html', context)

def lan_switch_research(request, lan):
    return redirect(f'/{lan}/research/')