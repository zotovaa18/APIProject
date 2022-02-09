# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 22:20:50 2021

@author: zotov
"""

from rest_framework import serializers

from .models import Countries, PeopleGroups, People, TypesLex, TypesMed, LessonBlocks, Lessons
from .models import Lexemes, Medias, Ik, Replicas, LecFilling, Rules, RulesLexemes, TypesEx
from .models import Exercises, Progress, Tasks, Variants, Favorites, Status
from .models import Newletters, Newwords, Newphrases, Matchsyllablessound, Collectwordsletters, Missingletter
from .models import Pronunciationwords, Recoverphrases, Selectwords, Wordpicturematch, Wordpictureselect, Writewords


class PeopleGroupsSerializer(serializers.ModelSerializer):
   class Meta:
       model = PeopleGroups
       fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
   class Meta:
       model = Status
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
       fields = ('type_lex',)


class TypesMedSerializer(serializers.ModelSerializer):
   class Meta:
       model = TypesMed
       fields = '__all__'


class LessonsWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = Lessons
       fields = ['id_les', 'name_les', 'lessonblock', 'video', 'video_st', 'lex_st', 'phr_st', 'dialog_st', 'rules_st']


class LessonsReadSerializer(serializers.ModelSerializer):
    class Meta(LessonsWriteSerializer.Meta):
        depth = 1


class LessonBlocksWriteSerializer(serializers.ModelSerializer):
    lesson = LessonsWriteSerializer(many=True, read_only=True)
    class Meta:
        model = LessonBlocks
        fields = ('id_lb', 'lesson')


class LessonBlocksReadSerializer(serializers.ModelSerializer):
   class Meta(LessonBlocksWriteSerializer.Meta):
       depth = 1


class LexemesWriteSerializer(serializers.ModelSerializer):
    cons = serializers.PrimaryKeyRelatedField(many=True, queryset=Lexemes.objects.all())

    class Meta:
        model = Lexemes
        fields = ('id_lex', 'mean_lex', 'transcr', 'stress', 'type', 'lesson', 'cons')


class LexemesReadSerializer(serializers.ModelSerializer):
   class Meta(LexemesWriteSerializer.Meta):
        depth = 0


class LecFillingWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = LecFilling
       fields = ('id', 'lexeme', 'cons')


class LecFillingReadSerializer(serializers.ModelSerializer):
    class Meta(LecFillingWriteSerializer.Meta):
        depth = 1


class RulesLexemesSerializer(serializers.ModelSerializer):
    #lexeme = serializers.ReadOnlyField(source='lexemes.id_lex')

    class Meta:
        model = RulesLexemes
        fields = ('id', 'rule', 'lexeme')


class RulesSerializer(serializers.ModelSerializer):
    lexeme = serializers.PrimaryKeyRelatedField(many=True, queryset=Lexemes.objects.all())
    lesson = serializers.PrimaryKeyRelatedField(queryset=Lessons.objects.all())

    class Meta:
        model = Rules
        fields = '__all__'

    # def create(self, validated_data):
    #     lexemes = Lexemes.objects.get(pk=validated_data.pop("id_lex"))
    #     instance = Rules.objects.create(**validated_data)
    #     RulesLexemes.objects.create(Lexemes=lexemes, Rules=instance)
    #     return instance
    #
    # def to_representation(self, instance):
    #     representation = super(RulesSerializer, self).to_representation(instance)
    #     representation["ruleslexemes"] = RulesLexemesSerializer(instance.ruleslexemes_set.all(), many=True).data
    #     return representation


class RulesReadSerializer(serializers.ModelSerializer):
    class Meta(RulesSerializer.Meta):
        depth = 1


class MediaWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = Medias
       fields = ('id_med', 'link_med', 'lexeme', 'type')


class MediaReadSerializer(serializers.ModelSerializer):
   class Meta(MediaWriteSerializer.Meta):
       depth = 1


class IkSerializer(serializers.ModelSerializer):
   class Meta:
       model = Ik
       fields = '__all__'


class ReplicasWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = Replicas
       fields = ('id_rep', 'time_start', 'time_finish', 'id_lex', 'id_med', 'id_ik', 'med_ik')


class ReplicasReadSerializer(serializers.ModelSerializer):
   class Meta(ReplicasWriteSerializer.Meta):
       depth = 2


class TypesExSerializer(serializers.ModelSerializer):
   class Meta:
       model = TypesEx
       fields = '__all__'


class ExercisesWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = Exercises
       fields = '__all__'


class ExercisesReadSerializer(serializers.ModelSerializer):
   class Meta(ExercisesWriteSerializer.Meta):
       depth = 2


class ProgressSerializer(serializers.ModelSerializer):
   class Meta:
       model = Progress
       fields = '__all__'
       depth = 2



class TasksWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = Tasks
       fields = ('id_task', 'id_ex', 'num_task', 'id_lex_right', 'type_med', 'num_lex', 'count_miss')


class TasksReadSerializer(serializers.ModelSerializer):
   class Meta(TasksWriteSerializer.Meta):
       depth = 2


class VariantsWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = Variants
       fields = ('id', 'id_task', 'id_lex', 'num_miss')


class VariantsReadSerializer(serializers.ModelSerializer):
   class Meta(VariantsWriteSerializer.Meta):
       depth = 2


class FavoritesWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = Favorites
       fields = ('id', 'exercise', 'lexeme', 'media', 'person')


class FavoritesReadSerializer(serializers.ModelSerializer):
   class Meta(VariantsWriteSerializer.Meta):
       depth = 2


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
