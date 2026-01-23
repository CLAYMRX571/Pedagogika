from django.shortcuts import render, redirect
from .models import Services

def Servicesviews(request):
    services = list(Services.objects.all())

    context = {
        'services': services,
    }

    return render(request, 'services.html', context)

def lan_switch_services(request, lan):
    return redirect(f'/{lan}/services/')