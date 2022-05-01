# Generated by Django 3.2.9 on 2022-05-01 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0050_auto_20220501_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumStop',
            fields=[
                ('login', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('count', models.IntegerField()),
            ],
            options={
                'db_table': 'num_stop',
                'managed': False,
            },
        ),
    ]
