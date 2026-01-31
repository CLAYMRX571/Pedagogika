from django.shortcuts import render, redirect
from .models import Monitor

def Monitorviews(request):
    monitor = Monitor.objects.all()

    context = {
        'monitor': monitor,
    }

    return render(request, 'monitor.html', context)

def lan_switch_monitor(request, lan):
    return redirect(f'/{lan}/monitor/')