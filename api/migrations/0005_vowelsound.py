# Generated by Django 3.2.9 on 2022-02-11 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_status_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='VowelSound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('transcr1', models.CharField(max_length=2)),
                ('transcr2', models.CharField(max_length=2)),
                ('sound1', models.TextField()),
                ('sound2', models.TextField()),
            ],
            options={
                'db_table': 'vowel_sound',
                'managed': False,
            },
        ),
    ]