# Generated by Django 3.2.9 on 2022-05-01 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0048_auto_20220501_1745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phrasesdto',
            old_name='id_variant',
            new_name='id_var',
        ),
    ]
