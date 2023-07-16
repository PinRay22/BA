from django.contrib import admin
from BAapp.models import *
# Register your models here.

class playersAdmin(admin.ModelAdmin):
    list_display = ('PID', 'GID', 'PName', 'NUM')

class GAMEAdmin(admin.ModelAdmin):
    list_display = ('GID', 'GName')

class StrategyAdmin(admin.ModelAdmin):
    list_display = ('SID', 'SName')

class OffensiveStatsAdmin(admin.ModelAdmin):
    list_display = ('OSID', 'OffensiveSystem', 'DefensiveSystem')

class DefensiveStatsAdmin(admin.ModelAdmin):
    list_display = ('DSID', 'DefensiveSystem', 'OffensiveSystem')

admin.site.register(players, playersAdmin)
admin.site.register(GAME, GAMEAdmin)
admin.site.register(Strategy, StrategyAdmin)
admin.site.register(OffensiveStats, OffensiveStatsAdmin)
admin.site.register(DefensiveStats, DefensiveStatsAdmin)