"""BA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BAapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index_view),
    path('gameset/', views.gameset_view),
    path('strategy/', views.strategy_view),
    path('save_offensive_stats/', views.save_offensive_stats),
    path('save_defensive_stats/', views.save_defensive_stats),
    path('strategyde/', views.strategy2_view),
    path('intell/', views.intell_view),
    path('addgame/', views.add_game),
    path('login/', views.login),
    path('renew/', views.renew),
    path('two_cant_hit/', views.two_cant_hit),
    path('two_hit/', views.two_hit),
    path('three_cant_hit/', views.three_cant_hit),
    path('three_hit/', views.three_hit),
    path('free_cant_hit/', views.free_cant_hit),
    path('free_hit/', views.free_hit),

]
