# Generated by Django 3.2.9 on 2022-05-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0055_delete_numstop'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumStop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('block', models.TextField()),
                ('stop', models.IntegerField()),
            ],
            options={
                'db_table': 'num_stop',
                'managed': False,
            },
        ),
    ]
