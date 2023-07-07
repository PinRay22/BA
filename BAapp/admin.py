from django.contrib import admin
from BAapp.models import *
# Register your models here.

class playersAdmin(admin.ModelAdmin):
    list_display = ('PID', 'GID', 'PName', 'NUM')

class GAMEAdmin(admin.ModelAdmin):
    list_display = ('GID', 'GName')

class StrategyAdmin(admin.ModelAdmin):
    list_display = ('SID', 'SName')

admin.site.register(players, playersAdmin)
admin.site.register(GAME, GAMEAdmin)
admin.site.register(Strategy, StrategyAdmin)