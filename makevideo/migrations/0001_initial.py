# Generated by Django 3.2.9 on 2022-01-19 20:42

from django.contrib.postgres.fields import ArrayField
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id_v', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name_video', models.CharField(max_length=100)),
                ('commands', ArrayField(models.TextField(), blank=True)),
                ('video_link', models.TextField(serialize=False))
            ],
            options={
                'db_table': 'video',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VideoCommands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('command', models.TextField()),
                ('num', models.DecimalField(decimal_places=0, max_digits=5)),
            ],
            options={
                'db_table': 'video_commands',
                'managed': False,
            },
        ),
    ]
