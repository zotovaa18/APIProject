# Generated by Django 3.2.9 on 2022-04-29 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_auto_20220429_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='dialogdto',
            name='forlesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='dialog_dto', to='api.forlessonsdto'),
        ),
    ]