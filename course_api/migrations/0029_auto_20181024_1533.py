# Generated by Django 2.1.2 on 2018-10-24 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_api', '0028_auto_20180824_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='important',
        ),
        migrations.AddField(
            model_name='schedule',
            name='enrolled',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Enrolled'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='finals_conflict',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Finals Conflict?'),
        ),
    ]
