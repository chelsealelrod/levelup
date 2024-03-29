# Generated by Django 3.2.9 on 2022-01-12 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0004_alter_event_attendees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='levelupapi.game'),
        ),
        migrations.AlterField(
            model_name='event',
            name='gamer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='levelupapi.gamer'),
        ),
    ]
