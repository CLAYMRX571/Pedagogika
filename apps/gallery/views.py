from django.shortcuts import render, redirect
from .models import Gallery

def Galleryviews(request):
    gallery = list(Gallery.objects.all())

    context = {
        'gallery': gallery,
    }

    return render(request, 'gallery.html', context)

def lan_switch_gallery(request, lan):
    return redirect(f'/{lan}/gallery/')