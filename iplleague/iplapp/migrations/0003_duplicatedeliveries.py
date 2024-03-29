# Generated by Django 2.2.2 on 2019-06-17 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iplapp', '0002_auto_20190617_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='DuplicateDeliveries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inning', models.IntegerField()),
                ('batting_team', models.CharField(max_length=40)),
                ('bowling_team', models.CharField(max_length=40)),
                ('over', models.IntegerField()),
                ('ball', models.IntegerField()),
                ('batsman', models.CharField(max_length=40)),
                ('non_striker', models.CharField(max_length=40)),
                ('bowler', models.CharField(max_length=40)),
                ('is_super_over', models.IntegerField()),
                ('wide_runs', models.IntegerField()),
                ('bye_runs', models.IntegerField()),
                ('legbye_runs', models.IntegerField()),
                ('noball_runs', models.IntegerField()),
                ('penalty_runs', models.IntegerField()),
                ('batsman_runs', models.IntegerField()),
                ('extra_runs', models.IntegerField()),
                ('total_runs', models.IntegerField()),
                ('player_dismissed', models.CharField(blank=True, max_length=40, null=True)),
                ('dismissal_kind', models.CharField(blank=True, max_length=40, null=True)),
                ('fielder', models.CharField(blank=True, max_length=40, null=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iplapp.Matches')),
            ],
        ),
    ]
