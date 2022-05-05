# Generated by Django 3.2.9 on 2022-02-11 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_showinfoaboutrules'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowInfoAboutWordsLetters',
            fields=[
                ('id_les', models.IntegerField()),
                ('name_les', models.CharField(max_length=100)),
                ('id_ex', models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False)),
                ('num_ex', models.IntegerField()),
                ('id_task', models.TextField()),
                ('num_task', models.TextField()),
                ('mean_lex1', models.TextField()),
                ('sound1', models.TextField()),
                ('mean_lex2', models.TextField()),
                ('transcr1', models.TextField()),
                ('transcr2', models.TextField()),
                ('sound2', models.TextField()),
                ('stress', models.DecimalField(decimal_places=0, max_digits=2)),
                ('pic', models.TextField()),
                ('mean_type_ex', models.TextField()),
                ('var', models.TextField()),
                ('miss', models.TextField()),
            ],
            options={
                'db_table': 'show_info_about_words_letters',
                'managed': False,
            },
        ),
    ]
