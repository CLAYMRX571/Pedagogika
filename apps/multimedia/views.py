from django.shortcuts import render, redirect
from .models import Multimedia

def Multimediaviews(request):
    multimedia = Multimedia.objects.all()

    context = {
        'multimedia': multimedia,
    }

    return render(request, 'multimedia.html', context)

def lan_switch_multimedia(request, lan):
    return redirect(f'/{lan}/multimedia/')