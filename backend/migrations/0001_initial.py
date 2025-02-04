# Generated by Django 5.0.6 on 2024-07-08 20:52

import backend.models.base
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImagePath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', backend.models.base.AutoDateTimeField(default=django.utils.timezone.now)),
                ('path', models.CharField(max_length=300, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', backend.models.base.AutoDateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'indexes': [models.Index(fields=['name'], name='backend_gam_name_2bfe89_idx'), models.Index(fields=['created_at'], name='backend_gam_created_7d29c9_idx'), models.Index(fields=['updated_at'], name='backend_gam_updated_bc2b74_idx')],
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', backend.models.base.AutoDateTimeField(default=django.utils.timezone.now)),
                ('victory', models.BooleanField()),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('kill', models.IntegerField(default=-1)),
                ('assist', models.IntegerField(default=-1)),
                ('death', models.IntegerField(default=-1)),
                ('point', models.IntegerField(default=-1)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.game')),
            ],
            options={
                'indexes': [models.Index(fields=['name'], name='backend_rec_name_8479ce_idx'), models.Index(fields=['date'], name='backend_rec_date_c48a8e_idx'), models.Index(fields=['name', 'game_id'], name='backend_rec_name_9e723f_idx'), models.Index(fields=['created_at'], name='backend_rec_created_31c23a_idx'), models.Index(fields=['updated_at'], name='backend_rec_updated_0dd2b4_idx')],
            },
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', backend.models.base.AutoDateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('total_played', models.IntegerField(default=0)),
                ('total_won', models.IntegerField(default=0)),
                ('total_lost', models.IntegerField(default=0)),
                ('total_assist', models.IntegerField(default=0)),
                ('total_death', models.IntegerField(default=0)),
                ('total_kill', models.IntegerField(default=0)),
                ('total_point', models.IntegerField(default=0)),
                ('valid_assist_match', models.IntegerField(default=0)),
                ('valid_death_match', models.IntegerField(default=0)),
                ('valid_kill_match', models.IntegerField(default=0)),
                ('valid_point_match', models.IntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.game')),
            ],
            options={
                'indexes': [models.Index(fields=['name'], name='backend_sta_name_157564_idx'), models.Index(fields=['date'], name='backend_sta_date_a34539_idx'), models.Index(fields=['name', 'game_id'], name='backend_sta_name_5824cf_idx'), models.Index(fields=['created_at'], name='backend_sta_created_d7f460_idx'), models.Index(fields=['updated_at'], name='backend_sta_updated_6a8fdc_idx')],
            },
        ),
    ]
