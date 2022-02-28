# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 22:20:50 2021

@author: zotov
"""

from rest_framework import serializers

from .models import Countries, PeopleGroups, People, TypesLex, TypesMed, LessonBlocks, Lessons
from .models import Lexemes, Medias, Ik, Replicas, LecFilling, Rules, RulesLexemes, TypesEx, ShowInfoAboutWordsLetters
from .models import Exercises, Progress, Tasks, Variants, Favorites, Status, VowelSound, ShowInfoAboutRules
#from .models import Newletters, Newwords, Newphrases, Matchsyllablessound, Collectwordsletters, Missingletter
#from .models import Pronunciationwords, Recoverphrases, Selectwords, Wordpicturematch, Wordpictureselect, Writewords
from .models import ShowInfoAboutWordsLetters, ShowInfoAboutPhrase

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

class LexemesWriteSerializer(serializers.ModelSerializer):
    cons = serializers.PrimaryKeyRelatedField(many=True, queryset=Lexemes.objects.all())

    class Meta:
        model = Lexemes
        fields = ('id_lex', 'mean_lex', 'transcr', 'stress', 'type', 'lesson', 'cons')


class LexemesReadSerializer(serializers.ModelSerializer):
   class Meta(LexemesWriteSerializer.Meta):
        depth = 0

class VariantsWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = Variants
       fields = ('id', 'task', 'lexeme', 'num_miss')


class VariantsReadSerializer(serializers.ModelSerializer):
   class Meta(VariantsWriteSerializer.Meta):
       depth = 3

class TasksWriteSerializer(serializers.ModelSerializer):
   variants = VariantsWriteSerializer(many=True)
   class Meta:
       model = Tasks
       fields = ('id_task', 'exercise', 'num_task', 'lex_right', 'type', 'num_lex', 'count_miss', 'picture', 'sound',
                 'replic', 'pronunciation', 'variants')
       depth = 1


class TasksReadSerializer(serializers.ModelSerializer):
   class Meta(TasksWriteSerializer.Meta):
       depth = 1


class ExercisesWriteSerializer(serializers.ModelSerializer):
   task = TasksWriteSerializer(many=True)
   class Meta:
       model = Exercises
       fields = ('id_ex', 'type', 'lesson', 'num_ex', 'task')
       depth = 5


class ExercisesReadSerializer(serializers.ModelSerializer):
   class Meta(ExercisesWriteSerializer.Meta):
       depth = 5


class LessonsWriteSerializer(serializers.ModelSerializer):
   exercises_info = ExercisesWriteSerializer(many=True)
   class Meta:
       model = Lessons
       fields = ('id_les', 'name_les', 'lessonblock', 'video', 'video_st', 'lex_st', 'phr_st', 'dialog_st', 'rules_st', 'exercises_info')
       read_only_fields = ('lessonblock',)
       depth = 6

       def create(self, validated_data):
           exercises_info = validated_data.pop('exercises_info')
           lesson = Lessons.objects.create(**validated_data)
           for exercise in exercises_info:
               Exercises.objects.create(**exercise, lesson=lesson)
           return lesson


class LessonsReadSerializer(serializers.ModelSerializer):
    class Meta(LessonsWriteSerializer.Meta):
        depth = 6


class LessonBlocksWriteSerializer(serializers.ModelSerializer):
    lesson_info = LessonsWriteSerializer(many=True)
    class Meta:
        model = LessonBlocks
        fields = ["id_lb", "lesson_info"]

    def create(self, validated_data):
        lesson_info = validated_data.pop('lesson_info')
        lessonblock = LessonBlocks.objects.create(**validated_data)
        for lesson in lesson_info:
            Lessons.objects.create(**lesson, lessonblock=lessonblock)
        return lessonblock

    # def update(self, instance, validated_data):
    #     lessons_data = validated_data.pop('lesson')
    #     less = (instance.lesson).all()
    #     less = list(less)
    #     instance.id_lb = validated_data.get('id_lb', instance.id_lb)
    #     instance.save()
    #
    #     for lesson_data in lessons_data:
    #         lesson = less.pop(0)
    #         lesson.name_les = lesson_data.get('name_les', lesson.name_les)
    #         lesson.video = lesson_data.get('video', lesson.video)
    #         lesson.video_st = lesson_data.get('video_st', lesson.video_st)
    #         lesson.lex_st = lesson_data.get('lex_st', lesson.lex_st)
    #         lesson.phr_st = lesson_data.get('phr_st', lesson.phr_st)
    #         lesson.dialog_st = lesson_data.get('dialog_st', lesson.dialog_st)
    #         lesson.rules_st = lesson_data.get('rules_st', lesson.rules_st)
    #
    #         lesson.save()
    #     return instance


class LessonBlocksReadSerializer(serializers.ModelSerializer):
   class Meta(LessonBlocksWriteSerializer.Meta):
       depth = 1



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
       fields = ('id_rep', 'time_start', 'time_finish', 'lexeme', 'media', 'ik', 'med_ik', 'symbol')


class ReplicasReadSerializer(serializers.ModelSerializer):
   class Meta(ReplicasWriteSerializer.Meta):
       depth = 2


class TypesExSerializer(serializers.ModelSerializer):
   class Meta:
       model = TypesEx
       fields = '__all__'


class ProgressSerializer(serializers.ModelSerializer):
   class Meta:
       model = Progress
       fields = '__all__'
       depth = 2


class VowelSoundWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = VowelSound
       fields = ('id', 'lexeme', 'transcr1', 'transcr2', 'sound1', 'sound2')


class VowelSoundReadSerializer(serializers.ModelSerializer):
   class Meta(VowelSoundWriteSerializer.Meta):
       depth = 1


class FavoritesWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = Favorites
       fields = ('id', 'exercise', 'lexeme', 'media', 'person')


class FavoritesReadSerializer(serializers.ModelSerializer):
   class Meta(VariantsWriteSerializer.Meta):
       depth = 2



class ShowInfoAboutRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowInfoAboutRules
        fields = ('name_les', 'id_ex', 'id_r', 'id_task', 'picture', 'sound_rule', 'side', 'mean_lex', 'var_lex',
                   'var_transcr', 'var_sound', 'var_pic', 'mean_type_ex')


class ShowInfoAboutWordsLettersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowInfoAboutWordsLetters
        fields = ('name_les', 'id_ex', 'id_task', 'num_task', 'mean_lex1', 'sound1', 'mean_lex2', 'transcr1',
                   'transcr2', 'sound2', 'stress', 'pic', 'mean_type_ex', 'variant', 'miss')


class ShowInfoAboutPhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowInfoAboutPhrase
        fields = ('name_les', 'id_ex', 'id_task', 'num_task', 'replica', 'ik', 'pic_video', 'sound2', 'variant', 'miss',
                  'mean_type_ex')


# class NewlettersSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Newletters
#        fields = '__all__'
#
#
# class NewwordsSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Newwords
#        fields = '__all__'
#
#
# class NewphrasesSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Newphrases
#        fields = '__all__'
#
#
# class MatchsyllablessoundSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Matchsyllablessound
#        fields = '__all__'
#
#
# class CollectwordslettersSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Collectwordsletters
#        fields = '__all__'
#
#
# class MissingletterSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Missingletter
#        fields = '__all__'
#
#
# class PronunciationwordsSerializer(serializers.ModelSerializer):
#    class Meta:
#         model = Pronunciationwords
#         fields = '__all__'
#
#
# class RecoverphrasesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Recoverphrases
#         fields = '__all__'
#
#
# class SelectwordsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Selectwords
#         fields = '__all__'
#
#
# class WordpicturematchSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Wordpicturematch
#         fields = '__all__'
#
#
# class WordpictureselectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Wordpictureselect
#         fields = '__all__'
#
#
# class WritewordsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Writewords
#         fields = '__all__'
