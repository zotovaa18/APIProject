# Generated by Django 3.2.9 on 2022-04-28 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_rulesdto_side'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rulesdto',
            name='vl_var',
        ),
    ]