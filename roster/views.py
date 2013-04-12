# Create your views  
from roster.models import Team, Player
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    context = {
        'team_count': Team.objects.count(),
        'player_count': Player.objects.count(),
    }
    
    return render(request,"base.html", context)



def player(request, pk):
    player = get_object_or_404(Player, id=pk)
    
    return render(request, "roster/player.html", {'player':player})

def team(request):
    player_list = Player.objects.all()
    paginator = Paginator(player_list, 25)
    page = request.GET.get('page')
    
    try:
        players = paginator.page(page)
    
    except PageNotAnInteger:
        players = paginator.page(1)
    
    except EmptyPage:
        players = paginator.page(paginator.num_pages)
    
    return render(request, 'roster/team.html', {"players": players})
