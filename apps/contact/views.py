from django.shortcuts import render, redirect
from .models import Contact

def Contactviews(request):
    contact = list(Contact.objects.all())

    context = {
        'contact': contact,
    }

    return render(request, 'contact.html', context)

def lan_switch_contact(request, lan):
    return redirect(f'/{lan}/contact/')