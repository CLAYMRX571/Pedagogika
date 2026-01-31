from django.shortcuts import render, redirect
from .models import Model

def Modelviews(request):
    model = Model.objects.all()

    context = {
        'model': model,
    }

    return render(request, 'model.html', context)

def lan_switch_model(request, lan):
    return redirect(f'/{lan}/model/')