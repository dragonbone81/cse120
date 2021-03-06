# Generated by Django 2.0.2 on 2018-03-14 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_api', '0008_auto_20180314_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(db_index=True, max_length=256, verbose_name='Course Name')),
                ('term', models.CharField(db_index=True, default='201810', max_length=32, verbose_name='Term')),
            ],
            options={
                'verbose_name': 'Subject Class',
                'verbose_name_plural': 'Subject Classes',
            },
        ),
        migrations.AlterUniqueTogether(
            name='subjectcourse',
            unique_together={('course_name', 'term')},
        ),
    ]
