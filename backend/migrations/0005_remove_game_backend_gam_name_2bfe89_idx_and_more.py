# Generated by Django 5.0.6 on 2024-07-06 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_game_name_game_backend_gam_name_2bfe89_idx_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='game',
            name='backend_gam_name_2bfe89_idx',
        ),
        migrations.RemoveIndex(
            model_name='record',
            name='backend_rec_game_id_bd68b0_idx',
        ),
        migrations.AddIndex(
            model_name='game',
            index=models.Index(fields=['name', 'created_at', 'updated_at'], name='backend_gam_name_d2bf4e_idx'),
        ),
        migrations.AddIndex(
            model_name='record',
            index=models.Index(fields=['game', 'name', 'created_at', 'updated_at'], name='backend_rec_game_id_853dc0_idx'),
        ),
    ]
