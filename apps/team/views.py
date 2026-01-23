from django.shortcuts import render, redirect
from .models import Team

def Teamviews(request):
    team = list(Team.objects.all())

    context = {
        'team': team,
    }

    return render(request, 'team.html', context)

def lan_switch_team(request, lan):
    return redirect(f'/{lan}/team/')