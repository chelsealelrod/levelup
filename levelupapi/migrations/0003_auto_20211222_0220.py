# Generated by Django 3.2.9 on 2021-12-22 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_event_game_gametype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='type',
            new_name='game_type',
        ),
        migrations.AddField(
            model_name='game',
            name='gamer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gamer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='maker',
            field=models.CharField(default='Milton Bradley', max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='number_of_players',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='skill_level',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='gamer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gamer'),
        ),
    ]
