# Generated by Django 3.2.9 on 2022-04-28 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_remove_rulesdto_forlesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='rulesdto',
            name='forlesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='rules_dto', to='api.forlessonsdto'),
        ),
    ]
