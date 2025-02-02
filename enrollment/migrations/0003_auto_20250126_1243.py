# Generated by Django 5.1.4 on 2025-01-26 12:43

from django.db import migrations

def add_sleep_durations(apps, schema_editor):
    SleepDuration = apps.get_model('enrollment', 'SleepDuration')
    durations = [
        "5-6 hours",
        "7-8 hours",
        "Less than 5 hours",
        "More than 8 hours",
        "Others",
    ]
    for duration in durations:
        SleepDuration.objects.create(name=duration)


def remove_sleep_durations(apps, schema_editor):
    SleepDuration = apps.get_model('enrollment', 'SleepDuration')
    durations = [
        "5-6 hours",
        "7-8 hours",
        "Less than 5 hours",
        "More than 8 hours",
        "Others",
    ]
    for duration in durations:
        SleepDuration.objects.filter(name=duration).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0002_auto_20250126_1240'),
    ]

    operations = [
        migrations.RunPython(add_sleep_durations, remove_sleep_durations),
    ]
