# Generated by Django 3.2.9 on 2022-01-11 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0003_auto_20211222_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(null=True, related_name='myevents', to='levelupapi.Gamer'),
        ),
    ]
