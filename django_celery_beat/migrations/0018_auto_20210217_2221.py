# Generated by Django 3.1.6 on 2021-02-17 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0017_auto_20201229_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodictask',
            name='name',
            field=models.CharField(help_text='Short Description For This Task', max_length=200, verbose_name='Name'),
        ),
    ]