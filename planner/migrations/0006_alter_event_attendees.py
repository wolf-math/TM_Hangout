# Generated by Django 5.0 on 2024-07-08 14:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_alter_event_max_attendees'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='attended_events', through='planner.Attendance', to=settings.AUTH_USER_MODEL),
        ),
    ]
