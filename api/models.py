from django.db import models


# Create your models here.
from makevideo.models import Video


class Countries(models.Model):
    id_country = models.CharField(primary_key=True, max_length=3)
    country_name = models.CharField(unique=True, max_length=40)
    flag_link = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'countries'

    def __str__(self):
        return self.country_name


class Exercises(models.Model):
    id_ex = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    type_ex = models.ForeignKey('TypesEx', models.DO_NOTHING, db_column='type_ex')
    id_les = models.ForeignKey('Lessons', models.DO_NOTHING, db_column='id_les')
    num_ex = models.DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'exercises'
        unique_together = (('id_les', 'num_ex'),)

    def __str__(self):
        return '%s %s %s' % (str(self.id_les), str(self.num_ex), self.type_ex)


class Favorites(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_ex = models.ForeignKey('Exercises', models.DO_NOTHING, db_column='id_ex', blank=True, null=True)
    id_lex = models.ForeignKey('Lexemes', models.DO_NOTHING, db_column='id_lex', blank=True, null=True)
    id_med = models.ForeignKey('Media', models.DO_NOTHING, db_column='id_med', blank=True, null=True)
    login = models.ForeignKey('People', models.DO_NOTHING, db_column='login')

    class Meta:
        managed = False
        db_table = 'favorites'
        unique_together = (('login', 'id_ex'), ('login', 'id_lex'), ('login', 'id_med'),)

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


class Status(models.Model):
    id_status = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'status'

    def __str__(self):
        return self.id_status


class Lessons(models.Model):
    id_les = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    name_les = models.CharField(max_length=100)
    id_lb = models.ForeignKey(LessonBlocks, models.DO_NOTHING, db_column='id_lb', related_name='lesson')
    id_v = models.ForeignKey(Video, models.DO_NOTHING, db_column='id_v', related_name='video')
    video_st = models.ForeignKey(Status, models.DO_NOTHING, db_column='video_st', related_name='status_video_st', default='Пусто', editable=False)
    lex_st = models.ForeignKey(Status, models.DO_NOTHING, db_column='lex_st', related_name='status_lex_st', default='Пусто', editable=False)
    phr_st = models.ForeignKey(Status, models.DO_NOTHING, db_column='phr_st', related_name='status_phr_st', default='Пусто', editable=False)
    dialog_st = models.ForeignKey(Status, models.DO_NOTHING, db_column='dialog_st', related_name='status_dialog_st', default='Пусто', editable=False)
    rules_st = models.ForeignKey(Status, models.DO_NOTHING, db_column='rules_st', related_name='status_rules_st', default='Пусто', editable=False)

    class Meta:
        managed = False
        db_table = 'lessons'
        unique_together = (('name_les', 'id_lb'),)

    def __str__(self):
        return '%s %s' % (self.name_les, str(self.id_lb))


class TypesLex(models.Model):
    type_lex = models.CharField(primary_key=True, max_length=5)

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
    type_lex = models.ForeignKey(TypesLex, models.DO_NOTHING, db_column='type_lex')
    id_les = models.ForeignKey(Lessons, models.DO_NOTHING, db_column='id_les')
    id_lex_cons = models.ManyToManyField('Lexemes', through='LecFilling', related_name='Lex_cons')

    class Meta:
        managed = False
        db_table = 'lexemes'

    def __str__(self):
        return '%s %s %s' % (self.id_lex, self.mean_lex, self.type_lex)


class LecFilling(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    id_lex = models.ForeignKey('Lexemes', models.DO_NOTHING, db_column='id_lex', related_name='Lexemes_id_lex')
    id_lex_cons = models.ForeignKey('Lexemes', models.DO_NOTHING, db_column='id_lex_cons',
                                    related_name='Lexemes_id_lex_cons')

    class Meta:
        managed = False
        db_table = 'lec_filling'

    def __str__(self):
        return '%s %s' % (self.id_lex, self.id_lex_cons)


class Media(models.Model):
    id_med = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    link_med = models.TextField()
    id_lex = models.ForeignKey(Lexemes, models.DO_NOTHING, db_column='id_lex', null=True)
    med_type = models.ForeignKey('TypesMed', models.DO_NOTHING, db_column='med_type')

    class Meta:
        managed = False
        db_table = 'media'
        unique_together = (('id_lex', 'med_type'),)

    def __str__(self):
        return '%s %s' % (self.id_lex, self.med_type)


class People(models.Model):
    login = models.CharField(primary_key=True, max_length=20)
    surname = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    group_user = models.ForeignKey('PeopleGroups', models.DO_NOTHING, db_column='group_user', blank=True, null=True)
    email = models.EmailField(max_length=40, unique=True)
    #id_country = models.ForeignKey(Countries, models.DO_NOTHING, db_column='id_country')
    password = models.CharField(max_length=20, blank=True, null=True)
    password_admin = models.CharField(max_length=20, blank=True, null=True)

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
    id_les = models.ForeignKey(Lessons, models.DO_NOTHING, db_column='id_les')
    id_lex = models.ManyToManyField(Lexemes, through='RulesLexemes', related_name='rules')

    class Meta:
        managed = False
        db_table = 'rules'

    def __str__(self):
        return self.id_r


class RulesLexemes(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    id_r = models.ForeignKey(Rules, models.DO_NOTHING, db_column='id_r')
    id_lex = models.ForeignKey(Lexemes, models.DO_NOTHING, db_column='id_lex')

    class Meta:
        managed = False
        db_table = 'rules_lexemes'

    def __str__(self):
        return self.id


class Replicas(models.Model):
    id_rep = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    time_start = models.TimeField()
    time_finish = models.TimeField()
    id_lex = models.ForeignKey(Lexemes, models.DO_NOTHING, db_column='id_lex')
    id_med = models.ForeignKey(Media, models.DO_NOTHING, db_column='id_med')
    id_ik = models.ForeignKey(Ik, models.DO_NOTHING, db_column='id_ik')
    med_ik = models.TextField()

    class Meta:
        managed = False
        db_table = 'replicas'

    def __str__(self):
        return self.id_rep


class Tasks(models.Model):
    id_task = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    id_ex = models.ForeignKey(Exercises, models.DO_NOTHING, db_column='id_ex')
    num_task = models.DecimalField(max_digits=2, decimal_places=0)
    id_lex_right = models.ForeignKey(Lexemes, models.DO_NOTHING, db_column='id_lex_right')
    type_med = models.ForeignKey('TypesMed', models.DO_NOTHING, db_column='type_med', blank=True, null=True)
    num_lex = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    count_miss = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

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

    def __str__(self):
        return self.mean_type_ex


class TypesMed(models.Model):
    type_med = models.CharField(primary_key=True, max_length=11)

    class Meta:
        managed = False
        db_table = 'types_med'

    def __str__(self):
        return self.type_med


class Variants(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    id_task = models.ForeignKey(Tasks, models.DO_NOTHING, db_column='id_task')
    id_lex = models.ForeignKey(Lexemes, models.DO_NOTHING, db_column='id_lex', blank=True, null=True)
    num_miss = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'variants'
        unique_together = (('num_miss', 'id_task'),)

    def __str__(self):
        return self.id


class Newletters(models.Model):
    id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_ex = models.DecimalField(max_digits=5, decimal_places=0)
    num_task = models.DecimalField(max_digits=2, decimal_places=0)
    mean_lex = models.CharField(max_length=100)
    med_type = models.CharField(max_length=11)
    link_med = models.TextField()
    
    class Meta:
        managed = False
        db_table = 'new_letters'


class Newwords(models.Model):
    id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_ex = models.DecimalField(max_digits=5, decimal_places=0)
    num_task = models.DecimalField(max_digits=2, decimal_places=0)
    mean_lex = models.CharField(max_length=100)
    med_type = models.CharField(max_length=11)
    link_med = models.TextField()
    
    class Meta:
        managed = False
        db_table = 'new_words'    


class Newphrases(models.Model):
    id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_ex = models.DecimalField(max_digits=5, decimal_places=0)
    num_task = models.DecimalField(max_digits=2, decimal_places=0)
    mean_lex = models.CharField(max_length=100)
    med_type = models.CharField(max_length=11)
    link_med = models.TextField()
    
    class Meta:
        managed = False
        db_table = 'new_phrases'  


class Matchsyllablessound(models.Model):
    id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_ex = models.DecimalField(max_digits=5, decimal_places=0)
    num_task = models.DecimalField(max_digits=2, decimal_places=0)
    mean_lex = models.CharField(max_length=100)
    right_sound = models.TextField()
    wrong_sound = models.TextField()
    
    class Meta:
        managed = False
        db_table = 'match_syllables_sound'  


class Collectwordsletters(models.Model):
    id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_ex = models.DecimalField(max_digits=5, decimal_places=0)
    num_task = models.DecimalField(max_digits=2, decimal_places=0)
    word = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'collect_words_letters'          
        

class Missingletter(models.Model):
    id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_ex = models.DecimalField(max_digits=5, decimal_places=0)
    num_task = models.DecimalField(max_digits=2, decimal_places=0)
    word = models.CharField(max_length=100)
    num_lex = models.DecimalField(max_digits=1, decimal_places=0)
    count_miss = models.DecimalField(max_digits=50, decimal_places=0)
    num_miss = models.DecimalField(max_digits=101, decimal_places=0)
    letter = models.CharField(max_length=100)
    
    class Meta:
        managed = False
        db_table = 'missing_letter'  


class Pronunciationwords(models.Model):
    id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_ex = models.DecimalField(max_digits=5, decimal_places=0)
    num_task = models.DecimalField(max_digits=2, decimal_places=0)
    mean_lex = models.CharField(max_length=100)
    right_sound = models.TextField()
    wrong_sound = models.TextField()
    
    class Meta:
        managed = False
        db_table = 'pronunciation_words'          


class Recoverphrases(models.Model):
    id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_ex = models.DecimalField(max_digits=5, decimal_places=0)
    num_task = models.DecimalField(max_digits=2, decimal_places=0)
    word = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'recover_phrases'  


class Selectwords(models.Model):
    id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_ex = models.DecimalField(max_digits=5, decimal_places=0)
    num_task = models.DecimalField(max_digits=2, decimal_places=0)
    phrase = models.CharField(max_length=100)
    num_lex = models.DecimalField(max_digits=1, decimal_places=0)
    count_miss = models.DecimalField(max_digits=50, decimal_places=0)
    num_miss = models.DecimalField(max_digits=101, decimal_places=0)
    word = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'select_words'  


class Wordpicturematch(models.Model):
    id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_ex = models.DecimalField(max_digits=5, decimal_places=0)
    num_task = models.DecimalField(max_digits=2, decimal_places=0)
    var1_lex = models.CharField(max_length=100)
    var1_pic = models.TextField()
    var_lex = models.CharField(max_length=100)
    var_pic = models.TextField()    
    
    class Meta:
        managed = False
        db_table = 'word_picture_match'          


class Wordpictureselect(models.Model):
    id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_ex = models.DecimalField(max_digits=5, decimal_places=0)
    num_task = models.DecimalField(max_digits=2, decimal_places=0)
    right_lex = models.CharField(max_length=100)
    right_pic = models.TextField()
    wrong_lex = models.CharField(max_length=100)
    wrong_pic = models.TextField()    
    
    class Meta:
        managed = False
        db_table = 'word_picture_select'          


class Writewords(models.Model):
    id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_ex = models.DecimalField(max_digits=5, decimal_places=0)
    num_task = models.DecimalField(max_digits=2, decimal_places=0)
    phrase = models.CharField(max_length=100)
    num_lex = models.DecimalField(max_digits=1, decimal_places=0)
    count_miss = models.DecimalField(max_digits=50, decimal_places=0)
    word = models.CharField(max_length=100)   
    
    class Meta:
        managed = False
        db_table = 'write_words'
