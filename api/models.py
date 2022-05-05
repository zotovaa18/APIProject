from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
from makevideo.models import Video


class WeakPoints(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    name_les = models.TextField()
    id_les = models.ForeignKey('Lessons', models.DO_NOTHING, db_column='id_les')
    login = models.ForeignKey('People', models.DO_NOTHING, db_column='login')
    total = models.IntegerField()
    completed = models.IntegerField()
    count = models.IntegerField()
    type = models.TextField()

    class Meta:
        managed = False
        db_table = 'for_weak_points_dto'


class Weaks(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    name_les = models.TextField()
    id_les = models.ForeignKey('Lessons', models.DO_NOTHING, db_column='id_les')
    login = models.ForeignKey('People', models.DO_NOTHING, db_column='login')
    total = models.IntegerField()
    completed = models.IntegerField()
    data = ArrayField(models.TextField())

    class Meta:
        managed = False
        db_table = 'for_weak_dto'


class DeleteDTO(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    id_les = models.ForeignKey('Lessons', models.DO_NOTHING, db_column='id_les')
    id_ex = ArrayField(models.IntegerField())
    login = models.ForeignKey('People', models.DO_NOTHING, db_column='login')

    class Meta:
        managed = False
        db_table = 'delete_dto'


# class WeakExerciseDTO:
#     id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
#     count = models.IntegerField()
#     type = models.TextField()
#     forweak = models.ForeignKey("WeakPointDTO", models.DO_NOTHING, related_name='data', blank=True, null=True)
#
#
# class WeakPointDTO(models.Model):
#     id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
#     name_les = models.TextField()
#     #login = models.ForeignKey('People', models.DO_NOTHING, db_column='login')
#     id_les = models.ForeignKey('Lessons', models.DO_NOTHING, db_column='id_les')
#     total = models.IntegerField()
#     complited = models.IntegerField()


class NumberOfWeakPoints(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    name_les = models.TextField()
    login = models.ForeignKey('People', models.DO_NOTHING, db_column='login')
    count = models.IntegerField()
    type = models.TextField()

    class Meta:
        managed = False
        db_table = 'number_of_weak_points'


class Rating(models.Model):
    login = models.CharField(primary_key=True, max_length=200, serialize=False)
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    photo = models.TextField(default='Пусто')
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rating'


# class WeakPoints(models.Model):
#     login = models.CharField(primary_key=True, max_length=200, serialize=False)
#     weak = ArrayField(models.IntegerField())
#
#     class Meta:
#         managed = False
#         db_table = 'weak_points'


class TimeSpent(models.Model):
    login = models.CharField(primary_key=True, max_length=200, serialize=False)
    time_spent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_time_spent'


class NumStop(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    block = models.TextField()
    name_les = models.TextField()
    login = models.ForeignKey('People', models.DO_NOTHING, db_column='login')
    stop = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'num_stop'


class ProgressBlocks(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    name_les = models.TextField()
    login = models.ForeignKey('People', models.DO_NOTHING, db_column='login')
    sum = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'progress_blocks'

        
class Countries(models.Model):
    id_country = models.CharField(primary_key=True, max_length=3)
    country_name = models.CharField(unique=True, max_length=40)
    flag_link = models.ImageField(unique=True, upload_to="images/")

    class Meta:
        managed = False
        db_table = 'countries'

    def __str__(self):
        return self.country_name


class Status(models.Model):
    id_status = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'status'

    def __str__(self):
        return self.id_status


class LessonInfoDTO(models.Model):
    video_st = models.ForeignKey(Status, models.DO_NOTHING, db_column='video_st',
                                 related_name='ForLessonsDTO_status_video_st', default='Пусто')
    lex_st = models.ForeignKey(Status, models.DO_NOTHING, db_column='lex_st',
                               related_name='ForLessonsDTO_status_lex_st', default='Пусто')
    phr_st = models.ForeignKey(Status, models.DO_NOTHING, db_column='phr_st',
                               related_name='ForLessonsDTO_status_phr_st', default='Пусто')
    dialog_st = models.ForeignKey(Status, models.DO_NOTHING, db_column='dialog_st',
                                  related_name='ForLessonsDTO_status_dialog_st', default='Пусто')
    rules_st = models.ForeignKey(Status, models.DO_NOTHING, db_column='rules_st',
                                 related_name='ForLessonsDTO_status_rules_st', default='Пусто')
    forlesson = models.OneToOneField("ForLessonsDTO", related_name='lesson_info', on_delete=models.CASCADE)


class RulesDTO(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    type_ex = models.ForeignKey('TypesEx', models.DO_NOTHING, db_column='type_ex', related_name='ForLessonsDTO_type')
    num_ex = models.DecimalField(max_digits=2, decimal_places=0)
    id_lex = models.ManyToManyField('Lexemes', blank=True, null=True, related_name='RulesDTO_lex_id_lex')
    id_var = models.ManyToManyField('Lexemes', blank=True, null=True)
    side = models.CharField(max_length=5, blank=True, null=True)
    sound_rule = models.TextField(blank=True, null=True)
    picture = models.TextField()
    forlesson = models.ForeignKey("ForLessonsDTO",  models.DO_NOTHING, related_name='rules', blank=True, null=True,)


class LexDTO(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    type_ex = models.ForeignKey('TypesEx', models.DO_NOTHING, db_column='type_ex')
    num_ex = models.DecimalField(max_digits=2, decimal_places=0)
    id_lex = models.ManyToManyField('Lexemes', blank=True, null=True, related_name='LexDTO_lex_id_lex')
    id_miss = ArrayField(models.IntegerField(), blank=True, null=True)
    id_var = models.ManyToManyField('Lexemes', blank=True, null=True, related_name='LexDTO_lex_id_variant')
    forlesson = models.ForeignKey("ForLessonsDTO", models.DO_NOTHING, related_name='lex', blank=True, null=True)


class DialogDTO(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    type_ex = models.ForeignKey('TypesEx', models.DO_NOTHING, db_column='type_ex')
    num_ex = models.DecimalField(max_digits=2, decimal_places=0)
    id_rep = ArrayField(models.IntegerField(), blank=True, null=True)
    id_miss = ArrayField(models.IntegerField(), blank=True, null=True)
    forlesson = models.ForeignKey("ForLessonsDTO", models.DO_NOTHING, related_name='dialogs', blank=True, null=True)


class PhrasesDTO(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    type_ex = models.ForeignKey('TypesEx', models.DO_NOTHING, db_column='type_ex')
    num_ex = models.DecimalField(max_digits=2, decimal_places=0)
    id_rep = models.ManyToManyField('Replicas', blank=True, null=True, related_name='PhrasesDTO_rep_id_rep')
    id_miss = ArrayField(models.IntegerField(), blank=True, null=True)
    id_var = models.ManyToManyField('Lexemes', blank=True, null=True, related_name='PhrasesDTO_lex_id_variant')
    forlesson = models.ForeignKey("ForLessonsDTO", models.DO_NOTHING, related_name='phrases', blank=True, null=True)


class ForLessonsDTO(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    name_les = models.CharField(max_length=100,  null=True)
    lessonblock = models.IntegerField( null=True)
    video = models.ForeignKey(Video, models.DO_NOTHING, db_column='id_v', related_name='ForLessonsDTO_video',
                              blank=True, null=True)
    description = models.TextField(blank=True, null=True)


class Exercises(models.Model):
    id_ex = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    type = models.ForeignKey('TypesEx', models.DO_NOTHING, db_column='type_ex')
    lesson = models.ForeignKey('Lessons', models.DO_NOTHING, db_column='id_les')
    num_ex = models.DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'exercises'
        unique_together = (('lesson', 'num_ex'),)

    def __str__(self):
        return '%s %s %s' % (str(self.lesson), str(self.num_ex), self.type)


class Favorites(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    exercise = models.ForeignKey('Exercises', models.DO_NOTHING, db_column='id_ex', blank=True, null=True)
    lexeme = models.ForeignKey('Lexemes', models.DO_NOTHING, db_column='id_lex', blank=True, null=True)
    media = models.ForeignKey('Medias', models.DO_NOTHING, db_column='id_med', blank=True, null=True)
    person = models.ForeignKey('People', models.DO_NOTHING, db_column='login')

    class Meta:
        managed = False
        db_table = 'favorites'
        unique_together = (('person', 'exercise'), ('person', 'lexeme'), ('person', 'media'),)

    def __str__(self):
        return self.id


class Ik(models.Model):
    id_ik = models.CharField(primary_key=True, max_length=4)

    class Meta:
        managed = False
        db_table = 'ik'

    def __str__(self):
        return self.id_ik


class LessonBlocks(models.Model):
    id_lb = models.AutoField(auto_created=True, primary_key=True, serialize=False)

    class Meta:
        managed = False
        db_table = 'lesson_blocks'

    def __str__(self):
        return str(self.id_lb)

    @property
    def lesson(self):
        return self.lesson_set.all()


class Lessons(models.Model):
    id_les = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    name_les = models.CharField(max_length=100)
    lessonblock = models.ForeignKey(LessonBlocks, models.DO_NOTHING, db_column='id_lb', related_name='lesson_info',
                                    null=True)
    video = models.ForeignKey(Video, models.DO_NOTHING, db_column='id_v', related_name='video', blank=True, null=True)
    video_st = models.ForeignKey(Status, models.DO_NOTHING, db_column='video_st', related_name='status_video_st',
                                 default='Пусто')
    lex_st = models.ForeignKey(Status, models.DO_NOTHING, db_column='lex_st', related_name='status_lex_st',
                               default='Пусто')
    phr_st = models.ForeignKey(Status, models.DO_NOTHING, db_column='phr_st', related_name='status_phr_st',
                               default='Пусто')
    dialog_st = models.ForeignKey(Status, models.DO_NOTHING, db_column='dialog_st', related_name='status_dialog_st',
                                  default='Пусто')
    rules_st = models.ForeignKey(Status, models.DO_NOTHING, db_column='rules_st', related_name='status_rules_st',
                                 default='Пусто')

    class Meta:
        managed = False
        db_table = 'lessons'
        unique_together = (('name_les', 'lessonblock'),)

    def __str__(self):
        return '%s %s' % (self.name_les, str(self.lessonblock))


class TypesLex(models.Model):
    type_lex = models.CharField(primary_key=True, max_length=6)

    class Meta:
        managed = False
        db_table = 'types_lex'

    def __str__(self):
        return self.type_lex


class Lexemes(models.Model):
    id_lex = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    mean_lex = models.CharField(max_length=100)
    transcr = models.CharField(max_length=100, blank=True, null=True, default=True)
    stress = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    type = models.ForeignKey(TypesLex, models.DO_NOTHING, db_column='type_lex')
    lesson = models.ForeignKey(Lessons, models.DO_NOTHING, db_column='id_les', related_name='lexeme')
    cons = models.ManyToManyField('Lexemes', through='LecFilling', related_name='Lex_cons')

    class Meta:
        managed = False
        db_table = 'lexemes'

    # def __str__(self):
    #     return '%s %s %s' % (self.id_lex, self.mean_lex, self.type)
    def __str__(self):
        return '%s' % (self.id_lex)


class LecFilling(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    lexeme = models.ForeignKey('Lexemes', models.DO_NOTHING, db_column='id_lex', related_name='Lexemes_lex')
    cons = models.ForeignKey('Lexemes', models.DO_NOTHING, db_column='id_lex_cons', related_name='Lexemes_cons')

    class Meta:
        managed = False
        db_table = 'lec_filling'

    def __str__(self):
        return '%s %s' % (self.lexeme, self.cons)


class Medias(models.Model):
    id_med = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    link_med = models.FileField(upload_to='media/')
    lexeme = models.ForeignKey(Lexemes, models.DO_NOTHING, db_column='id_lex', null=True)
    type = models.ForeignKey('TypesMed', models.DO_NOTHING, db_column='med_type')

    class Meta:
        managed = False
        db_table = 'media'
        unique_together = (('lexeme', 'type'),)

    def __str__(self):
        return '%s %s %s' % (str(self.id_med), self.lexeme, self.type)


class People(models.Model):
    login = models.CharField(primary_key=True, max_length=200)
    surname = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    group_user = models.ForeignKey('PeopleGroups', models.DO_NOTHING, db_column='group_user', default='Пользователь')
    email = models.EmailField(max_length=40, unique=True)
    #id_country = models.ForeignKey(Countries, models.DO_NOTHING, db_column='id_country')
    password = models.CharField(max_length=20, blank=True, null=True)
    password_admin = models.CharField(max_length=20, blank=True, null=True)
    photo = models.TextField(default='Пусто')

    class Meta:
        managed = False
        db_table = 'people'

    def __str__(self):
        return self.login


class PeopleGroups(models.Model):
    group_user = models.CharField(primary_key=True, max_length=13)

    class Meta:
        managed = False
        db_table = 'people_groups'

    def __str__(self):
        return self.group_user


class Progress(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    id_ex = models.ForeignKey(Exercises, models.DO_NOTHING, db_column='id_ex')
    login = models.ForeignKey(People, models.DO_NOTHING, db_column='login')
    mean_pr = models.BooleanField()
    count_attempt = models.DecimalField(max_digits=3, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'progress'

    def __str__(self):
        return self.id


class Rules(models.Model):
    id_r = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    picture = models.TextField()
    side = models.CharField(max_length=5)
    sound_rule = models.TextField(blank=True, null=True)
    lesson = models.ForeignKey(Lessons, models.DO_NOTHING, db_column='id_les', related_name='rule')
    lexeme = models.ManyToManyField(Lexemes, through='RulesLexemes', related_name='rules')

    class Meta:
        managed = False
        db_table = 'rules'

    def __str__(self):
        return str(self.id_r)


class RulesLexemes(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    rule = models.ForeignKey(Rules, models.DO_NOTHING, db_column='id_r')
    lexeme = models.ForeignKey(Lexemes, models.DO_NOTHING, db_column='id_lex')

    class Meta:
        managed = False
        db_table = 'rules_lexemes'

    def __str__(self):
        return self.id


class Replicas(models.Model):
    id_rep = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    time_start = models.TimeField()
    time_finish = models.TimeField()
    lexeme = models.ForeignKey(Lexemes, models.DO_NOTHING, db_column='id_lex')
    media = models.ForeignKey(Medias, models.DO_NOTHING, db_column='id_med')
    ik = models.ForeignKey(Ik, models.DO_NOTHING, db_column='id_ik')
    med_ik = models.TextField()
    symbol = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'replicas'

    def __str__(self):
        return '%s %s %s' % (str(self.id_rep), self.lexeme, self.symbol)


class Tasks(models.Model):
    id_task = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    exercise = models.ForeignKey(Exercises, models.DO_NOTHING, db_column='id_ex', related_name='task')
    num_task = models.DecimalField(max_digits=2, decimal_places=0)
    lex_right = models.ForeignKey(Lexemes, models.DO_NOTHING, db_column='id_lex_right', blank=True, null=True)
    type = models.ForeignKey('TypesMed', models.DO_NOTHING, db_column='type_med', blank=True, null=True)
    num_lex = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    count_miss = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    picture = models.TextField(blank=True, null=True)
    sound = models.TextField(blank=True, null=True)
    replic = models.ForeignKey('Replicas', models.DO_NOTHING, db_column='id_rep',  blank=True, null=True)
    pronunciation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasks'

    def __int__(self):
        return self.id_task


class TypesEx(models.Model):
    type_ex = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    mean_type_ex = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'types_ex'

    # def __str__(self):
    #     return self.mean_type_ex


class TypesMed(models.Model):
    type_med = models.CharField(primary_key=True, max_length=11)

    class Meta:
        managed = False
        db_table = 'types_med'

    def __str__(self):
        return self.type_med


class Variants(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    task = models.ForeignKey(Tasks, models.DO_NOTHING, db_column='id_task', related_name='variants')
    lexeme = models.ForeignKey(Lexemes, models.DO_NOTHING, db_column='id_lex', blank=True, null=True)
    num_miss = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'variants'
        unique_together = (('num_miss', 'task'),)

    def __str__(self):
        return self.id


class VowelSound(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    lexeme = models.OneToOneField(Lexemes, models.DO_NOTHING, db_column='id_lex')
    transcr1 = models.CharField(max_length=2)
    transcr2 = models.CharField(max_length=2)
    sound1 = models.TextField()
    sound2 = models.TextField()

    class Meta:
        managed = False
        db_table = 'vowel_sound'


class ShowInfoAboutRules(models.Model):
    id_les = models.IntegerField()
    name_les = models.CharField(max_length=100)
    id_ex = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    num_ex = models.IntegerField()
    id_r = models.DecimalField(max_digits=5, decimal_places=0)
    id_task = models.TextField()
    picture = models.TextField()
    sound_rule = models.TextField()
    side = models.CharField(max_length=5)
    mean_lex = models.TextField()
    var_lex = models.TextField()
    var_transcr = models.TextField()
    var_sound = models.TextField()
    var_pic = models.TextField()
    mean_type_ex = models.TextField()

    class Meta:
        managed = False
        db_table = 'show_info_about_rules'


class ShowInfoAboutWordsLetters(models.Model):
    id_les = models.IntegerField()
    name_les = models.CharField(max_length=100)
    id_ex = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    num_ex = models.IntegerField()
    id_task = models.TextField()
    num_task = models.TextField()
    mean_lex1 = models.TextField()
    sound1 = models.TextField()
    mean_lex2 = models.TextField()
    transcr1 = models.TextField()
    transcr2 = models.TextField()
    sound2 = models.TextField()
    stress = models.DecimalField(max_digits=2, decimal_places=0)
    pic = models.TextField()
    mean_type_ex = models.TextField()
    variant = models.TextField()
    miss = models.TextField()

    class Meta:
        managed = False
        db_table = 'show_info_about_words_letters'


class ShowInfoAboutPhrase(models.Model):
    id_les = models.IntegerField()
    name_les = models.CharField(max_length=100)
    id_ex = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_les = models.IntegerField()
    id_task = models.TextField()
    num_task = models.TextField()
    replica = models.TextField()
    ik = models.TextField()
    pic_video = models.TextField(db_column='pic/video')
    sound2 = models.TextField()
    variant = models.TextField()
    miss = models.TextField()
    mean_type_ex = models.TextField()

    class Meta:
        managed = False
        db_table = 'show_info_about_phrase'


# class Newletters(models.Model):
#     id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
#     id_ex = models.DecimalField(max_digits=5, decimal_places=0)
#     num_task = models.DecimalField(max_digits=2, decimal_places=0)
#     mean_lex = models.CharField(max_length=100)
#     med_type = models.CharField(max_length=11)
#     link_med = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'new_letters'
#
#
# class Newwords(models.Model):
#     id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
#     id_ex = models.DecimalField(max_digits=5, decimal_places=0)
#     num_task = models.DecimalField(max_digits=2, decimal_places=0)
#     mean_lex = models.CharField(max_length=100)
#     med_type = models.CharField(max_length=11)
#     link_med = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'new_words'
#
#
# class Newphrases(models.Model):
#     id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
#     id_ex = models.DecimalField(max_digits=5, decimal_places=0)
#     num_task = models.DecimalField(max_digits=2, decimal_places=0)
#     mean_lex = models.CharField(max_length=100)
#     med_type = models.CharField(max_length=11)
#     link_med = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'new_phrases'
#
#
# class Matchsyllablessound(models.Model):
#     id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
#     id_ex = models.DecimalField(max_digits=5, decimal_places=0)
#     num_task = models.DecimalField(max_digits=2, decimal_places=0)
#     mean_lex = models.CharField(max_length=100)
#     right_sound = models.TextField()
#     wrong_sound = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'match_syllables_sound'
#
#
# class Collectwordsletters(models.Model):
#     id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
#     id_ex = models.DecimalField(max_digits=5, decimal_places=0)
#     num_task = models.DecimalField(max_digits=2, decimal_places=0)
#     word = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'collect_words_letters'
#
#
# class Missingletter(models.Model):
#     id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
#     id_ex = models.DecimalField(max_digits=5, decimal_places=0)
#     num_task = models.DecimalField(max_digits=2, decimal_places=0)
#     word = models.CharField(max_length=100)
#     num_lex = models.DecimalField(max_digits=1, decimal_places=0)
#     count_miss = models.DecimalField(max_digits=50, decimal_places=0)
#     num_miss = models.DecimalField(max_digits=101, decimal_places=0)
#     letter = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'missing_letter'
#
#
# class Pronunciationwords(models.Model):
#     id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
#     id_ex = models.DecimalField(max_digits=5, decimal_places=0)
#     num_task = models.DecimalField(max_digits=2, decimal_places=0)
#     mean_lex = models.CharField(max_length=100)
#     right_sound = models.TextField()
#     wrong_sound = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'pronunciation_words'
#
#
# class Recoverphrases(models.Model):
#     id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
#     id_ex = models.DecimalField(max_digits=5, decimal_places=0)
#     num_task = models.DecimalField(max_digits=2, decimal_places=0)
#     word = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'recover_phrases'
#
#
# class Selectwords(models.Model):
#     id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
#     id_ex = models.DecimalField(max_digits=5, decimal_places=0)
#     num_task = models.DecimalField(max_digits=2, decimal_places=0)
#     phrase = models.CharField(max_length=100)
#     num_lex = models.DecimalField(max_digits=1, decimal_places=0)
#     count_miss = models.DecimalField(max_digits=50, decimal_places=0)
#     num_miss = models.DecimalField(max_digits=101, decimal_places=0)
#     word = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'select_words'
#
#
# class Wordpicturematch(models.Model):
#     id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
#     id_ex = models.DecimalField(max_digits=5, decimal_places=0)
#     num_task = models.DecimalField(max_digits=2, decimal_places=0)
#     var1_lex = models.CharField(max_length=100)
#     var1_pic = models.TextField()
#     var_lex = models.CharField(max_length=100)
#     var_pic = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'word_picture_match'
#
#
# class Wordpictureselect(models.Model):
#     id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
#     id_ex = models.DecimalField(max_digits=5, decimal_places=0)
#     num_task = models.DecimalField(max_digits=2, decimal_places=0)
#     right_lex = models.CharField(max_length=100)
#     right_pic = models.TextField()
#     wrong_lex = models.CharField(max_length=100)
#     wrong_pic = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'word_picture_select'
#
#
# class Writewords(models.Model):
#     id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
#     id_ex = models.DecimalField(max_digits=5, decimal_places=0)
#     num_task = models.DecimalField(max_digits=2, decimal_places=0)
#     phrase = models.CharField(max_length=100)
#     num_lex = models.DecimalField(max_digits=1, decimal_places=0)
#     count_miss = models.DecimalField(max_digits=50, decimal_places=0)
#     word = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'write_words'
