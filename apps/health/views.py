from django.shortcuts import render, redirect
from .models import Health

def Healthviews(request):
    health = Health.objects.all()

    context = {
        'health': health,
    }

    return render(request, 'health.html', context)

def lan_switch_health(request, lan):
    return redirect(f'/{lan}/health/')