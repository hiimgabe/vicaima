# Generated by Django 5.0.6 on 2024-05-15 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='beginning',
            new_name='begin_event',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='end',
            new_name='end_event',
        ),
    ]