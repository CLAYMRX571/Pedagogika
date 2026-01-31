from django.shortcuts import render, redirect
from .models import Pedagogical

def Pedagogicalviews(request):
    pedagogical = Pedagogical.objects.all()

    context = {
        'pedagogical': pedagogical,
    }

    return render(request, 'pedagogical.html', context)

def lan_switch_pedagogical(request, lan):
    return redirect(f'/{lan}/pedagogical/')