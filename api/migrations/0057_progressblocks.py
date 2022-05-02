# Generated by Django 3.2.9 on 2022-05-02 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0056_numstop'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgressBlocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name_les', models.TextField()),
                ('sum', models.IntegerField()),
            ],
            options={
                'db_table': 'progress_blocks',
                'managed': False,
            },
        ),
    ]
