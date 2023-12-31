# Generated by Django 4.0 on 2023-07-03 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BAapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SID', models.CharField(max_length=50, verbose_name='戰術表編號')),
                ('SName', models.CharField(max_length=50, verbose_name='戰術名稱')),
                ('SPlayer', models.CharField(max_length=50, verbose_name='場上球員')),
                ('SStPlayer', models.CharField(max_length=50, verbose_name='發動者')),
                ('EndPlayer', models.CharField(max_length=50, verbose_name='終結者')),
                ('Clean', models.CharField(max_length=50, verbose_name='空檔')),
            ],
        ),
    ]
