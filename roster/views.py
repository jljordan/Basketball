# Create your views here.

from django.shortcuts import render
from roster.models import Team, Player


def home(request):
    context = {
        'team_count': Team.objects.count(),
        'player_count': Player.objects.count(),
    }
    
    return render(request,"base.html", context)

def team(request):
    team = Team.objects.order_by('?')
    return render(request, "roster/team.html", {'team':team})

def player(request):
    player = Player.objects.order_by('?')
    return render(request, "roster/player.html", {'player':player})
