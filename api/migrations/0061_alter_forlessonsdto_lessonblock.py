# Generated by Django 3.2.9 on 2022-05-04 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0060_deletedto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forlessonsdto',
            name='lessonblock',
            field=models.IntegerField(),
        ),
    ]
