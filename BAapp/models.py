from django.db import models

# 球員數據
class players(models.Model):
    PID = models.AutoField('球員編號', primary_key=True) # 不能重複
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
    FG = models.CharField('2分球', max_length=10, null=True)
    TP = models.CharField('3分球', max_length=10, null=True)
    FT = models.CharField('罰球', max_length=10, null=True)
    GS_CHOICES = [
        ('GS', '首發'),
        ('BENCH', '替補'),
        ('DNP', '未上場'),
    ]
    GS = models.CharField('狀態',max_length=5, choices=GS_CHOICES, default='DNP')

    def calculate_fg_percentage(self):
        if self.FG is not None:
            made, attempted = map(int, self.FG.split('/'))
            if attempted > 0:
                percentage = round(made / attempted, 2)
                return f"{made}/{attempted} ({percentage})"
        return None
    
    def calculate_tp_percentage(self):
        if self.TP is not None:
            made, attempted = map(int, self.TP.split('/'))
            if attempted > 0:
                percentage = round(made / attempted, 2)
                return f"{made}/{attempted} ({percentage})"
        return None
    
    def calculate_ft_percentage(self):
        if self.FT is not None:
            made, attempted = map(int, self.FT.split('/'))
            if attempted > 0:
                percentage = round(made / attempted, 2)
                return f"{made}/{attempted} ({percentage})"
        return None

    def update_fg_percentage(self, made, attempted):
        if self.FG is not None:
            old_made, old_attempted = map(int, self.FG.split('/'))
            new_made = old_made + made
            new_attempted = old_attempted + attempted
            self.FG = f"{new_made}/{new_attempted}"
        else:
            self.FG = f"{made}/{attempted}"
        self.save()

    def update_tp_percentage(self, made, attempted):
        if self.TP is not None:
            old_made, old_attempted = map(int, self.TP.split('/'))
            new_made = old_made + made
            new_attempted = old_attempted + attempted
            self.TP = f"{new_made}/{new_attempted}"
        else:
            self.TP = f"{made}/{attempted}"
        self.save()

    def update_ft_percentage(self, made, attempted):
        if self.FT is not None:
            old_made, old_attempted = map(int, self.FT.split('/'))
            new_made = old_made + made
            new_attempted = old_attempted + attempted
            self.FT = f"{new_made}/{new_attempted}"
        else:
            self.FT = f"{made}/{attempted}"
        self.save()
            

# 比賽
class GAME(models.Model):
    GID = models.CharField('比賽編號', max_length=50, null = False) # 不能重複
    GName = models.CharField('比賽名稱', max_length=50)


class Strategy(models.Model):
    SID = models.CharField('戰術表編號', max_length=50, null = False) # 不能重複
    SName = models.CharField('戰術名稱', max_length=50)    # 西班牙擋拆              # 西班牙擋拆
    SPlayer = models.CharField('場上球員', max_length=50)  # 0, 17, 5, 35, 96       # 0, 17, 15, 33, 96
    SStPlayer = models.CharField('發動者', max_length=50)  # 0                      # 15
    EndPlayer = models.CharField('終結者', max_length=50)  # 17                     # 17
    Clean = models.CharField('空檔', max_length=50)  # 0                            # 0

class Intelligence_p(models.Model):
    IID = models.AutoField('情蒐表(球員)編號', primary_key=True)
    IName = models.CharField('球員名稱', max_length=50) 
    Iteam = models.CharField('球隊名稱', max_length=50) 
    INum = models.CharField('球員背號', max_length=50) 
    Height = models.IntegerField('身高', null=True)
    Weight = models.IntegerField('體重', null=True)
    U_strat = models.CharField('常用戰術', max_length=50)
    Position = models.CharField('位置', max_length=50)
    Habit = models.CharField('球員習慣', max_length=100)
    Dhand = models.CharField('慣用手', max_length=50)

class Intelligence_T(models.Model):
    TID = models.AutoField('情蒐表(球隊)編號', primary_key=True )
    Tteam = models.CharField('球隊名稱', max_length=50 ) 
    c_player = models.CharField('主力球員', max_length=50 )
    U_Strate = models.CharField('常用戰術', max_length=100) 
    Defence = models.CharField('防守模式', max_length=200) 
