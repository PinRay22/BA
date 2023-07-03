from django.db import models


class players(models.Model):
    PID = models.AutoField('球員編號', primary_key=True)
    GID = models.CharField('比賽編號', max_length=20)
    PName = models.CharField('會員姓名', max_length=20)
    NUM = models.IntegerField('球衣號', null=True)
    MIN = models.IntegerField('上場時間', null=True)
    PTS = models.IntegerField('分數', null=True)
    REB = models.IntegerField('籃板', null=True)
    OR = models.IntegerField('攻籃', null=True)
    BR = models.IntegerField('守籃', null=True)
    AST = models.IntegerField('助攻', null=True)
    STL = models.IntegerField('抄截', null=True)
    BLK = models.IntegerField('阻攻', null=True)
    TO = models.IntegerField('失誤', null=True)
    FG = models.IntegerField('2分球', null=True)
    TP = models.IntegerField('3分球', null=True)
    FT = models.IntegerField('罰球', null=True)
    GS_CHOICES = [
        ('GS', '首發'),
        ('BENCH', '替補'),
        ('DNP', '未上場'),
    ]
    GS = models.CharField('狀態',max_length=5, choices=GS_CHOICES, default='DNP')

class GAME(models.Model):
    GID = models.CharField('比賽編號', max_length=50, null = False)
    GName = models.CharField('比賽名稱', max_length=50)

