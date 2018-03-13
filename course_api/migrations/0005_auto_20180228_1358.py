# Generated by Django 2.0.2 on 2018-02-28 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_api', '0004_subjectclass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectclass',
            name='id',
        ),
        migrations.AlterField(
            model_name='subjectclass',
            name='course_name',
            field=models.CharField(db_index=True, max_length=256, primary_key=True, serialize=False, verbose_name='Course Name'),
        ),
    ]