# Generated by Django 2.0.3 on 2018-08-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_api', '0026_waitlist_expired'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='user_events',
            field=models.TextField(default='[]', verbose_name='User Events'),
        ),
    ]
