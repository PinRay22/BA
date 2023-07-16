# Generated by Django 4.0 on 2023-07-16 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BAapp', '0004_alter_players_ft_alter_players_tp'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefensiveStats',
            fields=[
                ('OSID', models.AutoField(primary_key=True, serialize=False, verbose_name='防守端戰術統計表編號')),
                ('P1', models.CharField(max_length=50, verbose_name='背號')),
                ('P2', models.CharField(max_length=50, verbose_name='背號')),
                ('P3', models.CharField(max_length=50, verbose_name='背號')),
                ('P4', models.CharField(max_length=50, verbose_name='背號')),
                ('P5', models.CharField(max_length=50, verbose_name='背號')),
                ('DefensiveSystem', models.CharField(max_length=100, verbose_name='我方防守系統')),
                ('Opponent_Remarks', models.TextField(blank=True, verbose_name='備註')),
                ('O1', models.CharField(max_length=50, verbose_name='背號')),
                ('O2', models.CharField(max_length=50, verbose_name='背號')),
                ('O3', models.CharField(max_length=50, verbose_name='背號')),
                ('O4', models.CharField(max_length=50, verbose_name='背號')),
                ('O5', models.CharField(max_length=50, verbose_name='背號')),
                ('OffensiveSystem', models.CharField(max_length=100, verbose_name='對方進攻系統')),
                ('Shooter', models.CharField(max_length=50, verbose_name='出手者')),
                ('IsVacant', models.BooleanField(default=False, verbose_name='是否空檔')),
                ('IsScored', models.BooleanField(default=False, verbose_name='是否得分')),
                ('Remarks', models.TextField(blank=True, verbose_name='備註')),
            ],
        ),
        migrations.CreateModel(
            name='Intelligence_p',
            fields=[
                ('IID', models.AutoField(primary_key=True, serialize=False, verbose_name='情蒐表(球員)編號')),
                ('IName', models.CharField(max_length=50, verbose_name='球員名稱')),
                ('Iteam', models.CharField(max_length=50, verbose_name='球隊名稱')),
                ('INum', models.CharField(max_length=50, verbose_name='球員背號')),
                ('Height', models.IntegerField(null=True, verbose_name='身高')),
                ('Weight', models.IntegerField(null=True, verbose_name='體重')),
                ('U_strat', models.CharField(max_length=50, verbose_name='常用戰術')),
                ('Position', models.CharField(max_length=50, verbose_name='位置')),
                ('Habit', models.CharField(max_length=100, verbose_name='球員習慣')),
                ('Dhand', models.CharField(max_length=50, verbose_name='慣用手')),
            ],
        ),
        migrations.CreateModel(
            name='Intelligence_T',
            fields=[
                ('TID', models.AutoField(primary_key=True, serialize=False, verbose_name='情蒐表(球隊)編號')),
                ('Tteam', models.CharField(max_length=50, verbose_name='球隊名稱')),
                ('c_player', models.CharField(max_length=50, verbose_name='主力球員')),
                ('U_Strate', models.CharField(max_length=100, verbose_name='常用戰術')),
                ('Defence', models.CharField(max_length=200, verbose_name='防守模式')),
            ],
        ),
        migrations.CreateModel(
            name='OffensiveStats',
            fields=[
                ('OSID', models.AutoField(primary_key=True, serialize=False, verbose_name='進攻端戰術統計表編號')),
                ('P1', models.CharField(max_length=50, verbose_name='背號')),
                ('P2', models.CharField(max_length=50, verbose_name='背號')),
                ('P3', models.CharField(max_length=50, verbose_name='背號')),
                ('P4', models.CharField(max_length=50, verbose_name='背號')),
                ('P5', models.CharField(max_length=50, verbose_name='背號')),
                ('OffensiveSystem', models.CharField(max_length=100, verbose_name='我方進攻系統')),
                ('Shooter', models.CharField(max_length=50, verbose_name='出手者')),
                ('IsVacant', models.BooleanField(default=False, verbose_name='是否空檔')),
                ('IsScored', models.BooleanField(default=False, verbose_name='是否得分')),
                ('Remarks', models.TextField(blank=True, verbose_name='備註')),
                ('O1', models.CharField(max_length=50, verbose_name='背號')),
                ('O2', models.CharField(max_length=50, verbose_name='背號')),
                ('O3', models.CharField(max_length=50, verbose_name='背號')),
                ('O4', models.CharField(max_length=50, verbose_name='背號')),
                ('O5', models.CharField(max_length=50, verbose_name='背號')),
                ('DefensiveSystem', models.CharField(max_length=100, verbose_name='對方防守系統')),
                ('Opponent_Remarks', models.TextField(blank=True, verbose_name='對方備註')),
            ],
        ),
    ]
