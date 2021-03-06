# Generated by Django 3.2.9 on 2022-04-26 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('makevideo', '0002_delete_videocommands'),
        ('api', '0010_alter_forlessonsdto_video'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dialog',
            new_name='DialogDTO',
        ),
        migrations.RenameModel(
            old_name='LessonInfo',
            new_name='LessonInfoDTO',
        ),
        migrations.RenameModel(
            old_name='Lex',
            new_name='LexDTO',
        ),
        migrations.RenameModel(
            old_name='Phrases',
            new_name='PhrasesDTO',
        ),
        migrations.AlterField(
            model_name='forlessonsdto',
            name='video',
            field=models.ForeignKey(blank=True, db_column='id_v', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ForLessonsDTO_video', to='makevideo.video'),
        ),
        migrations.CreateModel(
            name='RulesDTO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('num_ex', models.DecimalField(decimal_places=0, max_digits=2)),
                ('side', models.CharField(max_length=5)),
                ('sound_rule', models.FileField(unique=True, upload_to="images/sound/")),
                ('picture', models.ImageField(unique=True, upload_to="images/")),
                ('id_var', models.ManyToManyField(to='api.Lexemes')),
                ('type', models.ForeignKey(db_column='type_ex', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ForLessonsDTO_type', to='api.typesex')),
            ],
        ),
    ]
