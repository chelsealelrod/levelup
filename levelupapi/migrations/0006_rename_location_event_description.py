# Generated by Django 3.2.9 on 2022-01-12 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0005_auto_20220112_0305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='location',
            new_name='description',
        ),
    ]