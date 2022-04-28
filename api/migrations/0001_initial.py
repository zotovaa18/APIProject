# Generated by Django 3.2.9 on 2021-11-30 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collectwordsletters',
            fields=[
                ('id_task', models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False)),
                ('id_ex', models.DecimalField(decimal_places=0, max_digits=5)),
                ('num_task', models.DecimalField(decimal_places=0, max_digits=2)),
                ('word', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'collect_words_letters',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id_country', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=40, unique=True)),
                ('flag_link', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'countries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id_ex', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('num_ex', models.DecimalField(decimal_places=0, max_digits=2)),
            ],
            options={
                'db_table': 'exercises',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'favorites',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ik',
            fields=[
                ('id_ik', models.CharField(max_length=4, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'ik',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LecFilling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'lec_filling',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LessonBlocks',
            fields=[
                ('id_lb', models.AutoField(auto_created = True, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'lesson_blocks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id_les', models.AutoField(auto_created = True, primary_key=True, serialize=False)),
                ('name_les', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'lessons',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lexemes',
            fields=[
                ('id_lex', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('mean_lex', models.CharField(max_length=100)),
                ('transcr', models.CharField(blank=True, max_length=100, null=True, default=True)),
                ('stress', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True)),
            ],
            options={
                'db_table': 'lexemes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Matchsyllablessound',
            fields=[
                ('id_task', models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False)),
                ('id_ex', models.DecimalField(decimal_places=0, max_digits=5)),
                ('num_task', models.DecimalField(decimal_places=0, max_digits=2)),
                ('mean_lex', models.CharField(max_length=100)),
                ('right_sound', models.TextField()),
                ('wrong_sound', models.TextField()),
            ],
            options={
                'db_table': 'match_syllables_sound',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medias',
            fields=[
                ('id_med', models.AutoField(auto_created = True, primary_key=True, serialize=False)),
                ('link_med', models.TextField()),
            ],
            options={
                'db_table': 'media',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Missingletter',
            fields=[
                ('id_task', models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False)),
                ('id_ex', models.DecimalField(decimal_places=0, max_digits=5)),
                ('num_task', models.DecimalField(decimal_places=0, max_digits=2)),
                ('word', models.CharField(max_length=100)),
                ('num_lex', models.DecimalField(decimal_places=0, max_digits=1)),
                ('count_miss', models.DecimalField(decimal_places=0, max_digits=3)),
                ('num_miss', models.DecimalField(decimal_places=0, max_digits=3)),
                ('letter', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'missing_letter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Newletters',
            fields=[
                ('id_task', models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False)),
                ('id_ex', models.DecimalField(decimal_places=0, max_digits=5)),
                ('num_task', models.DecimalField(decimal_places=0, max_digits=2)),
                ('mean_lex', models.CharField(max_length=100)),
                ('med_type', models.CharField(max_length=11)),
                ('link_med', models.TextField()),
            ],
            options={
                'db_table': 'new_letters',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Newphrases',
            fields=[
                ('id_task', models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False)),
                ('id_ex', models.DecimalField(decimal_places=0, max_digits=5)),
                ('num_task', models.DecimalField(decimal_places=0, max_digits=2)),
                ('mean_lex', models.CharField(max_length=100)),
                ('med_type', models.CharField(max_length=11)),
                ('link_med', models.TextField()),
            ],
            options={
                'db_table': 'new_phrases',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Newwords',
            fields=[
                ('id_task', models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False)),
                ('id_ex', models.DecimalField(decimal_places=0, max_digits=5)),
                ('num_task', models.DecimalField(decimal_places=0, max_digits=2)),
                ('mean_lex', models.CharField(max_length=100)),
                ('med_type', models.CharField(max_length=11)),
                ('link_med', models.TextField()),
            ],
            options={
                'db_table': 'new_words',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('login', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('password_admin', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'people',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PeopleGroups',
            fields=[
                ('group_user', models.CharField(max_length=13, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'people_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('mean_pr', models.BooleanField()),
                ('count_attempt', models.DecimalField(max_digits=3, decimal_places=0))
            ],
            options={
                'db_table': 'progress',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pronunciationwords',
            fields=[
                ('id_task', models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False)),
                ('id_ex', models.DecimalField(decimal_places=0, max_digits=5)),
                ('num_task', models.DecimalField(decimal_places=0, max_digits=2)),
                ('mean_lex', models.CharField(max_length=100)),
                ('right_sound', models.TextField()),
                ('wrong_sound', models.TextField()),
            ],
            options={
                'db_table': 'pronunciation_words',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recoverphrases',
            fields=[
                ('id_task', models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False)),
                ('id_ex', models.DecimalField(decimal_places=0, max_digits=5)),
                ('num_task', models.DecimalField(decimal_places=0, max_digits=2)),
                ('word', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'recover_phrases',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id_r', models.AutoField(auto_created = True, primary_key=True, serialize=False)),
                ('picture', models.TextField()),
            ],
            options={
                'db_table': 'reduction',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RulesLexemes',
            fields=[
                ('id', models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'reduction_lexemes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Replicas',
            fields=[
                ('id_rep', models.AutoField(auto_created = True, primary_key=True, serialize=False)),
                ('time_start', models.TimeField()),
                ('time_finish', models.TimeField()),
                ('med_ik', models.TextField()),
                ('symbol', models.CharField(max_length=1))
            ],
            options={
                'db_table': 'replicas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Selectwords',
            fields=[
                ('id_task', models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False)),
                ('id_ex', models.DecimalField(decimal_places=0, max_digits=5)),
                ('num_task', models.DecimalField(decimal_places=0, max_digits=2)),
                ('phrase', models.CharField(max_length=100)),
                ('num_lex', models.DecimalField(decimal_places=0, max_digits=1)),
                ('count_miss', models.DecimalField(decimal_places=0, max_digits=3)),
                ('num_miss', models.DecimalField(decimal_places=0, max_digits=3)),
                ('word', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'select_words',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id_task', models.AutoField(auto_created = True, primary_key=True, serialize=False)),
                ('num_task', models.DecimalField(decimal_places=0, max_digits=2)),
                ('num_lex', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('count_miss', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('picture', models.TextField(blank=True, null=True)),
                ('sound', models.TextField(blank=True, null=True)),
                ('pronunciation', models.TextField(blank=True, null=True))
            ],
            options={
                'db_table': 'tasks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TypesEx',
            fields=[
                ('type_ex', models.AutoField(auto_created = True, primary_key=True, serialize=False)),
                ('mean_type_ex', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'types_ex',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TypesLex',
            fields=[
                ('type_lex', models.CharField(max_length=5, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'types_lex',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TypesMed',
            fields=[
                ('type_med', models.CharField(max_length=11, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'types_med',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Variants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('num_miss', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
            ],
            options={
                'db_table': 'variants',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wordpicturematch',
            fields=[
                ('id_task', models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False)),
                ('id_ex', models.DecimalField(decimal_places=0, max_digits=5)),
                ('num_task', models.DecimalField(decimal_places=0, max_digits=2)),
                ('var1_lex', models.CharField(max_length=100)),
                ('var1_pic', models.TextField()),
                ('var_lex', models.CharField(max_length=100)),
                ('var_pic', models.TextField()),
            ],
            options={
                'db_table': 'word_picture_match',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wordpictureselect',
            fields=[
                ('id_task', models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False)),
                ('id_ex', models.DecimalField(decimal_places=0, max_digits=5)),
                ('num_task', models.DecimalField(decimal_places=0, max_digits=2)),
                ('right_lex', models.CharField(max_length=100)),
                ('right_pic', models.TextField()),
                ('wrong_lex', models.CharField(max_length=100)),
                ('wrong_pic', models.TextField()),
            ],
            options={
                'db_table': 'word_picture_select',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Writewords',
            fields=[
                ('id_task', models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False)),
                ('id_ex', models.DecimalField(decimal_places=0, max_digits=5)),
                ('num_task', models.DecimalField(decimal_places=0, max_digits=2)),
                ('phrase', models.CharField(max_length=100)),
                ('num_lex', models.DecimalField(decimal_places=0, max_digits=3)),
                ('count_miss', models.DecimalField(decimal_places=0, max_digits=3)),
                ('word', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'write_words',
                'managed': False,
            },
        ),
    ]
