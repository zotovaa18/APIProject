# Generated by Django 3.2.9 on 2022-05-01 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0046_auto_20220501_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dialogdto',
            name='pic_video',
        ),
    ]