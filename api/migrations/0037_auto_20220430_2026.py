# Generated by Django 3.2.9 on 2022-04-30 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_alter_lessoninfodto_forlesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='lexdto',
            name='forlesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='lex', to='api.forlessonsdto'),
        ),
        migrations.AlterField(
            model_name='rulesdto',
            name='forlesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='rules', to='api.forlessonsdto'),
        ),
        migrations.CreateModel(
            name='VlVar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
                ('label', models.CharField(max_length=100)),
                ('id_lexdto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vl_variant', to='api.lexdto')),
            ],
        ),
        migrations.CreateModel(
            name='VlMiss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
                ('label', models.CharField(max_length=100)),
                ('id_lexdto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vl_miss', to='api.lexdto')),
            ],
        ),
        migrations.CreateModel(
            name='VlLex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
                ('label', models.CharField(max_length=100)),
                ('id_lexdto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vl_lex', to='api.lexdto')),
            ],
        ),
    ]