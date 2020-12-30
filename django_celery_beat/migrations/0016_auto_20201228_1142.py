# Generated by Django 3.0.5 on 2020-12-28 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0015_edit_solarschedule_events_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='crontabschedule',
            name='name',
            field=models.CharField(default='', help_text='Short Name For This Crontab', max_length=200, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='intervalschedule',
            name='name',
            field=models.CharField(default='', help_text='Short Name For This IntervalSchedule', max_length=200, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
