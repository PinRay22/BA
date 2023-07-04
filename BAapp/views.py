from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponseRedirect
from BAapp.models import *
# Create your views here.


def index_view(request):
    latest_game = GAME.objects.latest('GID')

    if latest_game is not None:
        latest_gid = latest_game.GID
    else:
        latest_gid = None
    player = players.objects.filter( GID = latest_gid )

    return render(request, 'index.html', locals())

def renew(request):
    get_pid = request.POST.get('pid', '')
    get_name = request.POST.get('name', '')
    get_number = request.POST.get('number', '')
    get_min = request.POST.get('min', '')
    get_pts = request.POST.get('pts', '')
    get_reb = request.POST.get('reb', '')
    get_or = request.POST.get('or', '')
    get_br = request.POST.get('br', '')
    get_ast = request.POST.get('ast', '')
    get_stl = request.POST.get('stl', '')
    get_blk = request.POST.get('blk', '')
    get_to = request.POST.get('to', '')
    get_fg = request.POST.get('fg', '')
    get_3p = request.POST.get('3p', '')
    get_ft = request.POST.get('ft', '')
    player = players.objects.get(PID=get_pid)
    player.PName = get_name
    player.NUM = get_number
    player.MIN = get_min
    player.PTS = get_pts
    player.REB = get_reb
    player.OR = get_or
    player.BR = get_br
    player.AST = get_ast
    player.STL = get_stl
    player.BLK = get_blk
    player.TO = get_to
    player.FG = get_fg
    player.TP = get_3p
    player.FT = get_ft
    player.save()
    return redirect('/index/')


def gameset_view(request):
    latest_game = GAME.objects.latest('GID')

    if latest_game is not None:
        latest_gid = latest_game.GID
    else:
        latest_gid = None
    player = players.objects.filter( GID = latest_gid )
    return render(request, 'gameset.html', locals())

def add_game(request):
    get_gid = request.POST.get('gid', '')
    get_gname = request.POST.get('gname', '')
    GAME.objects.create(
        GID = get_gid,
        GName = get_gname 
    )
    return redirect('/gameset/')


def login(request):
    get_number = request.POST.get('number', '')
    get_status = request.POST.get('status', '')
    get_gid = request.POST.get('gid', '')
    players.objects.create(
        NUM = get_number,
        PName = 'None',
        GID = get_gid,
        GS = get_status,
        MIN = None,
        PTS = None,
        REB = None,
        OR = None,
        BR = None,
        AST = None,
        STL = None,
        BLK = None,
        TO = None,
        FG = None,
        TP = None,
        FT = None
    )
    return redirect('/gameset/')

def strategy_view(request):

    return render(request, 'strategy.html', locals())