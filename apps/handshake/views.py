from django.shortcuts import render, redirect
from .models import Handshake

def Handshakeviews(request):
    handshake = Handshake.objects.all()

    context = {
        'handshake': handshake,
    }

    return render(request, 'handshake.html', context)

def lan_switch_handshake(request, lan):
    return redirect(f'/{lan}/handshake/')