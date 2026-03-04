from django.shortcuts import render, redirect
from .models import Home

def Homeviews(request):
    home = Home.objects.first()

    context = {
        'home': home,
    }

    return render(request, 'index.html', context)

def lan_switch_home(request, lan):
    return redirect(f'/home/{lan}/')