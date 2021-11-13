from django.db import models
from dbview.models import DbView


# Create your models here.

class Countries(models.Model):
    id_country = models.CharField(primary_key=True, max_length=3)
    country_name = models.CharField(unique=True, max_length=40)
    flag_link = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'countries'



class Exercises(models.Model):
    id_ex = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    type_ex = models.ForeignKey('TypesEx', models.DO_NOTHING, db_column='type_ex')
    id_les = models.ForeignKey('Lessons', models.DO_NOTHING, db_column='id_les')
    num_ex = models.DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'exercises'
        unique_together = (('id_les', 'num_ex'),)


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


class Ik(models.Model):
    id_ik = models.CharField(primary_key=True, max_length=4)

    class Meta:
        managed = False
        db_table = 'ik'

class LecFilling(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_lex = models.ForeignKey('Lexemes', models.DO_NOTHING, db_column='id_lex', related_name='Lexemes_id_lex')
    id_lex_cons = models.ForeignKey('Lexemes', models.DO_NOTHING, db_column='id_lex_cons', related_name='Lexemes_id_lex_cons')

    class Meta:
        managed = False
        db_table = 'lec_filling'


class LessonBlocks(models.Model):
    id_lb = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'lesson_blocks'


class Lessons(models.Model):
    id_les = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    name_les = models.CharField(unique=True, max_length=100)
    id_lb = models.ForeignKey(LessonBlocks, models.DO_NOTHING, db_column='id_lb')

    class Meta:
        managed = False
        db_table = 'lessons'


class Lexemes(models.Model):
    id_lex = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    mean_lex = models.CharField(max_length=100)
    transcr = models.CharField(max_length=100, blank=True, null=True)
    stress = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    type_lex = models.ForeignKey('TypesLex', models.DO_NOTHING, db_column='type_lex')
    id_les = models.ForeignKey(Lessons, models.DO_NOTHING, db_column='id_les')

    class Meta:
        managed = False
        db_table = 'lexemes'


class Media(models.Model):
    id_med = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    link_med = models.TextField()
    id_lex = models.ForeignKey(Lexemes, models.DO_NOTHING, db_column='id_lex')
    med_type = models.ForeignKey('TypesMed', models.DO_NOTHING, db_column='med_type')

    class Meta:
        managed = False
        db_table = 'media'
        unique_together = (('id_lex', 'med_type'),)


class People(models.Model):
    login = models.CharField(primary_key=True, max_length=20)
    surname = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    group_user = models.ForeignKey('PeopleGroups', models.DO_NOTHING, db_column='group_user', blank=True, null=True)
    email = models.EmailField(max_length=40, unique=True)
    id_country = models.ForeignKey(Countries, models.DO_NOTHING, db_column='id_country')

    class Meta:
        managed = False
        db_table = 'people'


class PeopleGroups(models.Model):
    group_user = models.CharField(primary_key=True, max_length=13)

    class Meta:
        managed = False
        db_table = 'people_groups'


class Progress(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_ex = models.ForeignKey(Exercises, models.DO_NOTHING, db_column='id_ex')
    login = models.ForeignKey(People, models.DO_NOTHING, db_column='login')
    mean_pr = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'progress'


class Reduction(models.Model):
    id_red = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    mean_red = models.TextField()
    id_lex = models.ManyToManyField(Lexemes, related_name='lex')
    
    class Meta:
        managed = False
        db_table = 'reduction'


class ReductionLexemes(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_red = models.ForeignKey(Reduction, models.DO_NOTHING, db_column='id_red')
    id_lex = models.ForeignKey(Lexemes, models.DO_NOTHING, db_column='id_lex')

    class Meta:
        managed = False
        db_table = 'reduction_lexemes'


class Replicas(models.Model):
    id_rep = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    time_start = models.TimeField()
    time_finish = models.TimeField()
    id_lex = models.ForeignKey(Lexemes, models.DO_NOTHING, db_column='id_lex')
    id_med = models.ForeignKey(Media, models.DO_NOTHING, db_column='id_med')
    id_ik = models.ForeignKey(Ik, models.DO_NOTHING, db_column='id_ik')
    med_ik = models.TextField()

    class Meta:
        managed = False
        db_table = 'replicas'


class Tasks(models.Model):
    id_task = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_ex = models.ForeignKey(Exercises, models.DO_NOTHING, db_column='id_ex')
    num_task = models.DecimalField(max_digits=2, decimal_places=0)
    id_lex_right = models.ForeignKey(Lexemes, models.DO_NOTHING, db_column='id_lex_right')
    type_med = models.ForeignKey('TypesMed', models.DO_NOTHING, db_column='type_med', blank=True, null=True)
    num_lex = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    count_miss = models.DecimalField(max_digits=50, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasks'


class TypesEx(models.Model):
    type_ex = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    mean_type_ex = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'types_ex'


class TypesLex(models.Model):
    type_lex = models.CharField(primary_key=True, max_length=5)

    class Meta:
        managed = False
        db_table = 'types_lex'


class TypesMed(models.Model):
    type_med = models.CharField(primary_key=True, max_length=11)

    class Meta:
        managed = False
        db_table = 'types_med'


class Variants(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_task = models.ForeignKey(Tasks, models.DO_NOTHING, db_column='id_task')
    id_lex = models.ForeignKey(Lexemes, models.DO_NOTHING, db_column='id_lex', blank=True, null=True)
    num_miss = models.DecimalField(max_digits=101, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'variants'
        unique_together = (('num_miss', 'id_task'),)

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