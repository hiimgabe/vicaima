# Generated by Django 5.0.6 on 2024-05-15 15:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_rename_beginning_event_begin_event_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='evaluator',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evaluator_events', to='database.colaborator'),
        ),
    ]