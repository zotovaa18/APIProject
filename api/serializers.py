# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 22:20:50 2021

@author: zotov
"""

from rest_framework import serializers

from .models import Countries, PeopleGroups, People, TypesLex, TypesMed, LessonBlocks, Lessons
from .models import Lexemes, Media, Ik, Replicas, LecFilling, Reduction, ReductionLexemes, TypesEx
from .models import Exercises, Progress, Tasks, Variants, Favorites
from .models import Newletters, Newwords, Newphrases, Matchsyllablessound, Collectwordsletters, Missingletter
from .models import Pronunciationwords, Recoverphrases, Selectwords, Wordpicturematch, Wordpictureselect, Writewords


class PeopleGroupsSerializer(serializers.ModelSerializer):
   class Meta:
       model = PeopleGroups
       fields = '__all__'

class CountriesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Countries
       fields = '__all__'

class PeopleSerializer(serializers.ModelSerializer):
   class Meta:
       model = People
       fields = '__all__'

class TypesLexSerializer(serializers.ModelSerializer):
   class Meta:
       model = TypesLex
       fields = '__all__'

class TypesMedSerializer(serializers.ModelSerializer):
   class Meta:
       model = TypesMed
       fields = '__all__'

class LessonBlocksSerializer(serializers.ModelSerializer):
   class Meta:
       model = LessonBlocks
       fields = '__all__'

class LessonsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Lessons
       fields = '__all__'

class LexemesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Lexemes
       fields = '__all__'
class MediaSerializer(serializers.ModelSerializer):
   class Meta:
       model = Media
       fields = '__all__'

class IkSerializer(serializers.ModelSerializer):
   class Meta:
       model = Ik
       fields = '__all__'

class ReplicasSerializer(serializers.ModelSerializer):
   class Meta:
       model = Replicas
       fields = '__all__'

class LecFillingSerializer(serializers.ModelSerializer):
   class Meta:
       model = LecFilling
       fields = '__all__'

class ReductionSerializer(serializers.ModelSerializer):
   class Meta:
       model = Reduction
       fields = '__all__'
              
class ReductionLexemesSerializer(serializers.ModelSerializer):
   class Meta:
       model = ReductionLexemes
       fields = '__all__'

class TypesExSerializer(serializers.ModelSerializer):
   class Meta:
       model = TypesEx
       fields = '__all__'

class ExercisesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Exercises
       fields = '__all__'

class ProgressSerializer(serializers.ModelSerializer):
   class Meta:
       model = Progress
       fields = '__all__'

class TasksSerializer(serializers.ModelSerializer):
   class Meta:
       model = Tasks
       fields = '__all__'
       
class VariantsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Variants
       fields = '__all__'

class FavoritesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Favorites
       fields = '__all__'

class NewlettersSerializer(serializers.ModelSerializer):
   class Meta:
       model = Newletters 
       fields = '__all__'

class NewwordsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Newwords 
       fields = '__all__'       

class NewphrasesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Newphrases 
       fields = '__all__'

class MatchsyllablessoundSerializer(serializers.ModelSerializer):
   class Meta:
       model = Matchsyllablessound
       fields = '__all__'        
       
class CollectwordslettersSerializer(serializers.ModelSerializer):
   class Meta:
       model = Collectwordsletters
       fields = '__all__'            
       
class MissingletterSerializer(serializers.ModelSerializer):
   class Meta:
       model = Missingletter
       fields = '__all__'  

class PronunciationwordsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Pronunciationwords
       fields = '__all__'     

class RecoverphrasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recoverphrases
        fields = '__all__'  

class SelectwordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selectwords
        fields = '__all__'  

class WordpicturematchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wordpicturematch
        fields = '__all__'              

class WordpictureselectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wordpictureselect
        fields = '__all__'     

class WritewordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writewords
        fields = '__all__'            