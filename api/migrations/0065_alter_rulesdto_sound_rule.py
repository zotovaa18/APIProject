# Generated by Django 3.2.9 on 2022-05-06 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0064_alter_rulesdto_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rulesdto',
            name='sound_rule',
            field=models.TextField(),
        ),
    ]
