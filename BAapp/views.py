from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponseRedirect
# Create your views here.


def index_view(request):
    return render(request, 'index.html', locals())


def gameset_view(request):
    return render(request, 'gameset.html', locals())

def login(request):
    get_pnum = request.POST.get('number', '')
    get_odid = request.POST.get('status', '')
    return redirect('/gameset/')


def creategame(request):
    return redirect('/gameset/')