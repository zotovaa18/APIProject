# Generated by Django 3.2.9 on 2022-05-01 11:23

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0043_vlmissd_vlrep'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dialogdto',
            name='id_rep',
        ),
        migrations.AddField(
            model_name='dialogdto',
            name='id_rep',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None),
        ),
    ]
