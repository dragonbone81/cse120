# Generated by Django 2.0.2 on 2018-03-22 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_api', '0011_schedule_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created'),
        ),
    ]