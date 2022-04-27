# Generated by Django 3.2.9 on 2022-04-26 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_lessoninfodto_forlesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessoninfodto',
            name='forlesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_info', to='api.forlessonsdto'),
        ),
    ]
