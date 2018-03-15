# Generated by Django 2.0.2 on 2018-03-14 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_api', '0007_course_simple_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='term',
            field=models.CharField(db_index=True, default='201810', max_length=32, verbose_name='Term'),
        ),
        migrations.AddField(
            model_name='subjectclass',
            name='term',
            field=models.CharField(db_index=True, default='201810', max_length=32, verbose_name='Term'),
        ),
    ]