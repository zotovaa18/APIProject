# Generated by Django 3.2.9 on 2022-04-29 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_alter_vl_id_r'),
    ]

    operations = [
        migrations.AddField(
            model_name='forlessonsdto',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
