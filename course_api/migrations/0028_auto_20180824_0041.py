# Generated by Django 2.0.3 on 2018-08-24 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_api', '0027_schedule_user_events'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='final_dates_2',
        ),
        migrations.RemoveField(
            model_name='course',
            name='final_days_2',
        ),
        migrations.RemoveField(
            model_name='course',
            name='final_hours_2',
        ),
        migrations.RemoveField(
            model_name='course',
            name='final_room_2',
        ),
        migrations.RemoveField(
            model_name='course',
            name='final_type_2',
        ),
    ]
