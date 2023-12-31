from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponseRedirect
from BAapp.models import *
# Create your views here.

# 數據平台頁面
def index_view(request):
    latest_game = GAME.objects.latest('GID')

    if latest_game is not None:
        latest_gid = latest_game.GID
    else:
        latest_gid = None
    player = players.objects.filter( GID = latest_gid )

    return render(request, 'index.html', locals())

# 兩分球沒進
def two_cant_hit(request):
    if request.method == 'POST':
        get_pid = request.POST.get('pid', '')
        player = players.objects.get( PID = get_pid )
        player.update_fg_percentage(0, 1)  # 更新2分球的數據
        
        # 或者計算2分球的命中率
        fg_percentage = player.calculate_fg_percentage()
        print(fg_percentage)
    return redirect('/index/')

# 兩分球進
def two_hit(request):
    get_pid = request.POST.get('pid', '')
    # 假設您要更新球員編號為1的球員的2分球數據
    player = players.objects.get( PID = get_pid )
    player.update_fg_percentage(1, 1)  # 更新2分球的數據
    pts = player.PTS 
    player.PTS = pts + 2
    print(pts)
    player.save()
    # 或者計算2分球的命中率
    fg_percentage = player.calculate_fg_percentage()
    print(fg_percentage)
    return redirect('/index/')

# 三分球沒進
def three_cant_hit(request):
    if request.method == 'POST':
        get_pid = request.POST.get('pid', '')
        player = players.objects.get( PID = get_pid )
        player.update_tp_percentage(0, 1)  # 更新3分球的數據
        player.update_fg_percentage(0, 1)
        # 或者計算2分球的命中率
        tp_percentage = player.calculate_tp_percentage()
        print(tp_percentage)
    return redirect('/index/')

# 三分球進
def three_hit(request):
    get_pid = request.POST.get('pid', '')
    # 假設您要更新球員編號為1的球員的2分球數據
    player = players.objects.get( PID = get_pid )
    player.update_tp_percentage(1, 1)  # 更新3分球的數據
    player.update_fg_percentage(1, 1)
    pts = player.PTS 
    player.PTS = pts + 3
    print(pts)
    player.save()
    # 或者計算2分球的命中率
    tp_percentage = player.calculate_tp_percentage()
    print(tp_percentage)
    return redirect('/index/')

# 罰球沒進
def free_cant_hit(request):
    if request.method == 'POST':
        get_pid = request.POST.get('pid', '')
        player = players.objects.get( PID = get_pid )
        player.update_ft_percentage(0, 1)  # 更新3分球的數據
        
        # 或者計算2分球的命中率
        ft_percentage = player.calculate_ft_percentage()
        print(ft_percentage)
    return redirect('/index/')

# 罰球進
def free_hit(request):
    get_pid = request.POST.get('pid', '')
    # 假設您要更新球員編號為1的球員的2分球數據
    player = players.objects.get( PID = get_pid )
    player.update_ft_percentage(1, 1)  # 更新3分球的數據
    pts = player.PTS 
    player.PTS = pts + 1
    print(pts)
    player.save()
    # 或者計算2分球的命中率
    ft_percentage = player.calculate_ft_percentage()
    print(ft_percentage)
    return redirect('/index/')

# 數據更新
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

# 建立比賽頁面
def gameset_view(request):
    latest_game = GAME.objects.latest('GID')
    if latest_game is not None:
        latest_gid = latest_game.GID
    else:
        latest_gid = None

    if 'gid' in request.POST:
        latest_gid = request.POST.get('gid', '')
    
    player = players.objects.filter( GID = latest_gid )
    return render(request, 'gameset.html', locals())

# 新增比賽ID
def add_game(request):
    get_gid = request.POST.get('gid', '')
    get_gname = request.POST.get('gname', '')
    GAME.objects.create(
        GID = get_gid,
        GName = get_gname 
    )
    return redirect('/gameset/')


# 登入球員
def login(request):
    get_number = request.POST.get('number', '')
    player = players.objects.filter(NUM=get_number).first()
    if player:
        name = player.PName
    else:
        name = None
    get_status = request.POST.get('status', '')
    get_gid = request.POST.get('gid', '')
    players.objects.create(
        NUM = get_number,
        PName = name,
        GID = get_gid,
        GS = get_status,
        MIN = 0,
        PTS = 0,
        REB = 0,
        OR = 0,
        BR = 0,
        AST = 0,
        STL = 0,
        BLK = 0,
        TO = 0,
        FG = '0/0',
        TP = '0/0',
        FT = '0/0'
    )
    return redirect('/gameset/')

# 戰術分析頁面
def strategy_view(request):
    return render(request, 'strategy.html', locals())

def save_offensive_stats(request):
    if request.method == 'POST':
        p1 = request.POST.get('p1')
        p2 = request.POST.get('p2')
        p3 = request.POST.get('p3')
        p4 = request.POST.get('p4')
        p5 = request.POST.get('p5')
        offensive_system = request.POST.get('offensive-system')
        if offensive_system == '其他':
            offensive_system = request.POST.get('other-option-value')
        shooter = request.POST.get('shooter')
        is_vacant = request.POST.get('is-vacant') == '是'
        is_scored = request.POST.get('is-scored') == '是'
        remarks = request.POST.get('remarks')
        o1 = request.POST.get('o1')
        o2 = request.POST.get('o2')
        o3 = request.POST.get('o3')
        o4 = request.POST.get('o4')
        o5 = request.POST.get('o5')

        defensive_system = request.POST.get('defensive-system')
        if defensive_system == '其他':
            defensive_system = request.POST.get('defense-other-option-value')
        opponent_remarks = request.POST.get('opponent-remarks')
        
        offensive_stats = OffensiveStats(
            P1=p1,
            P2=p2,
            P3=p3,
            P4=p4,
            P5=p5,
            OffensiveSystem=offensive_system,
            Shooter=shooter,
            IsVacant=is_vacant,
            IsScored=is_scored,
            Remarks=remarks,
            O1=o1,
            O2=o2,
            O3=o3,
            O4=o4,
            O5=o5,
            DefensiveSystem=defensive_system,
            Opponent_Remarks=opponent_remarks
        )
        offensive_stats.save()
        
    return redirect('/strategy/')


def strategy2_view(request):
    return render(request, 'strategy_de.html', locals())

def save_defensive_stats(request):
    if request.method == 'POST':
        p1 = request.POST.get('p1')
        p2 = request.POST.get('p2')
        p3 = request.POST.get('p3')
        p4 = request.POST.get('p4')
        p5 = request.POST.get('p5')
        defensive_system = request.POST.get('defensive_system')
        if defensive_system == '其他':
            defensive_system = request.POST.get('defense-other-option-value')
        remarks = request.POST.get('remarks')
        o1 = request.POST.get('o1')
        o2 = request.POST.get('o2')
        o3 = request.POST.get('o3')
        o4 = request.POST.get('o4')
        o5 = request.POST.get('o5')
        offensive_system = request.POST.get('offense-tactic')
        if offensive_system == '其他':
            offensive_system = request.POST.get('offense-other-option-value')
        shooter = request.POST.get('shooter')
        is_vacant = request.POST.get('is-vacant') == '是'
        is_scored = request.POST.get('is-score') == '是'
        opponent_remarks = request.POST.get('opponent-remarks')

        defensive_stats = DefensiveStats(
            P1=p1,
            P2=p2,
            P3=p3,
            P4=p4,
            P5=p5,
            DefensiveSystem=defensive_system,
            Remarks=remarks,            
            O1=o1,
            O2=o2,
            O3=o3,
            O4=o4,
            O5=o5,
            OffensiveSystem=offensive_system,
            Shooter=shooter,
            IsVacant=is_vacant,
            IsScored=is_scored,
            Opponent_Remarks=opponent_remarks
        )
        defensive_stats.save()

    return redirect('/strategyde/')

def intell_view(request):
    return render(request, 'intelligence.html', locals())