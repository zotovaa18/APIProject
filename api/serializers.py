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
from .models import ShowInfoAboutWordsLetters, ShowInfoAboutPhrase, ForLessonsDTO
from .models import *


class TimeSpentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSpent
        fields = '__all__'


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
   #variants = VariantsWriteSerializer(many=True)
   class Meta:
       model = Tasks
       fields = ('id_task', 'exercise', 'num_task', 'lex_right', 'type', 'num_lex', 'count_miss', 'picture', 'sound',
                 'replic', 'pronunciation', )



class TasksReadSerializer(serializers.ModelSerializer):
   class Meta(TasksWriteSerializer.Meta):
       depth = 2


class ExercisesWriteSerializer(serializers.ModelSerializer):
   #task = TasksWriteSerializer(many=True)
   #lesson = serializers.PrimaryKeyRelatedField(queryset=Lessons.objects.all())
   #type = serializers.PrimaryKeyRelatedField(queryset=TypesEx.objects.all())
   class Meta:
       model = Exercises
       fields = ('id_ex', 'type', 'lesson', 'num_ex', )


class ExercisesReadSerializer(serializers.ModelSerializer):
   class Meta(ExercisesWriteSerializer.Meta):
       depth = 5


class LessonInfoDTOWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = LessonInfoDTO
       #fields = "__all__"
       #read_only_fields = ('lesson')
       exclude = ('forlesson',)


class RulesDTOWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = RulesDTO
       fields = ["type", "num_ex", "id_lex", "id_var", "vl_var", "side", "sound_rule", "picture"]


class LexDTOWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = LexDTO
       fields = "__all__"
       depth = 5


class DialogDTOWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = DialogDTO
       fields = "__all__"
       depth = 5


class PhrasesDTOWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = PhrasesDTO
       fields = "__all__"
       depth = 5


class ForLessonsDTOWriteSerializer(serializers.ModelSerializer):
    lesson_info = LessonInfoDTOWriteSerializer(many=True)
    rules_dto = RulesDTOWriteSerializer(many=True)
    # lex_dto = LexDTOWriteSerializer(many=True)
    # dialog_dto = DialogDTOWriteSerializer(many=True)
    # phrase_dto = PhrasesDTOWriteSerializer(many=True)
    # {
    #     "lesson_info": [
    #         {
    #             "video_st": "Пусто     ",
    #             "lex_st": "Пусто     ",
    #             "phr_st": "Пусто     ",
    #             "dialog_st": "Пусто     ",
    #             "rules_st": "Пусто     "
    #         }
    #     ],
    #     "rules_dto": [
    #         {
    #             "type": 23,
    #             "num_ex": 0,
    #             "id_lex": null,
    #             "id_var": [61, 62],
    #             "vl_var": [],
    #             "side": "лево",
    #             "sound_rule": "прол",
    #             "picture": "лдолд"
    #         }
    #     ],
    #     "name_les": "Тест 26.04_5",
    #     "lessonblock": 1,
    #     "video": 1
    # }

    class Meta:
        model = ForLessonsDTO
        fields = '__all__'

    # def create(self, validated_data):
    #     lessons_info_data = validated_data.pop('lesson_info')
    #     rules_data = validated_data.pop('rules_dto')
    #     forlessonsdto = ForLessonsDTO.objects.create(**validated_data)
    #     for lesson_info_data in lessons_info_data:
    #
    #         les = Lessons.objects.create(name_les=forlessonsdto.name_les, lessonblock=forlessonsdto.lessonblock,
    #                                      video=forlessonsdto.video, **lesson_info_data)
    #         les.save()
    #         LessonInfoDTO.objects.create(forlesson=forlessonsdto, id=les.id_les, **lesson_info_data)
    #
    #     for rule_data in rules_data:
    #         print(rule_data.get('id_var')[0])
    #         print(len(rule_data.get('id_var')))
    #
    #         if rule_data.get('type').type_ex == 23:
    #             rule = Rules.objects.create(lesson=les,
    #                                         picture=rule_data.get('picture'), side=rule_data.get('side'),
    #                                         sound_rule=rule_data.get('sound_rule'))
    #             for i in rule_data.get('id_var'):
    #                 print(i)
    #                 rule.lexeme.add(i)
    #             rule.save()
    #         else:
    #             ex = Exercises.object.create(type_ex=forlessonsdto.type, lesson=les.id_les, num_ex=forlessonsdto.rule_data.num_ex)
    #             ex.save()
    #             task = Tasks.object.create(exercise=ex.id_ex, num_task=1, lex_right=forlessonsdto.rule_data.id_lex,
    #                                        type=None, num_lex=None, count_miss=None,
    #                                        picture=forlessonsdto.rule_data.picture, sount_rule=forlessonsdto.rule_data.sound_rule,
    #                                        replic=None, pronunciation=None)
    #             task.save()
    #             variant = Variants.object.create(task=task.id_task, lexemes=forlessonsdto.rule_data.id_var, num_miss=None)
    #             variant.save()
    #
    #         RulesDTO.objects.create(forlesson=forlessonsdto, id=rule.id_r, **rule_data)
    #
    #     return forlessonsdto


class LessonsWriteSerializer(serializers.ModelSerializer):
   #exercises_info = ExercisesWriteSerializer(many=True)
   #lessonblock = serializers.PrimaryKeyRelatedField(queryset=LessonBlocks.objects.all())
   #lessonblock = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
   class Meta:
       model = Lessons
       fields = ('id_les', 'name_les', 'lessonblock', 'video', 'video_st', 'lex_st', 'phr_st', 'dialog_st', 'rules_st',)
       #'exercises_info'
       # read_only_fields = ('lessonblock',)
       # depth = 6
       # #'exercises_info'
       # def create(self, validated_data):
       #     exercises_info = validated_data.pop('exercises_info')
       #     lesson = Lessons.objects.create(**validated_data)
       #     for exercise in exercises_info:
       #         Exercises.objects.create(**exercise, lesson=lesson)
       #     return lesson


class LessonsReadSerializer(serializers.ModelSerializer):
    class Meta(LessonsWriteSerializer.Meta):
        depth = 6


class LessonBlocksWriteSerializer(serializers.ModelSerializer):
    #lesson_info = LessonsWriteSerializer(many=True,  read_only=True)
    class Meta:
        model = LessonBlocks
        fields = ["id_lb"]

    # #"lesson_info"
    # def create(self, validated_data):
    #     lessons_info = validated_data.pop('lesson_info')
    #     lessonblock = LessonBlocks.objects.create(**validated_data)
    #     for lesson in lessons_info:
    #         ex_info = lesson.pop('exercises_info')
    #         les = Lessons.objects.create(**lesson, lessonblock=lessonblock)
    #         for exercise in ex_info:
    #             Exercises.objects.create(**exercise, lesson=les)
    #     return lessonblock
    #
    # def update(self, instance, validated_data):
    #     lesson_info = validated_data.pop('lesson_info')
    #     instance.save()
    #     keep_lessons = []
    #     #existing_ids = [lesson.id_les for lesson in instance.lesson_info]
    #     for lesson_data in lesson_info:
    #         les_id = lesson_data.get('id_les', None)
    #         #if "id_les" in lesson_data.keys():
    #         if les_id:
    #             if Lessons.objects.filter(id_les=lesson_data["id_les"]).exists():
    #                 lesson = Lessons.objects.get(id_les=lesson_data["id_les"])
    #                 lesson.name_les = lesson_data.get('name_les', lesson.name_les)
    #                 #lesson.lessonblock = lesson_data('lessonblock', instance.id_lb)
    #                 lesson.video = lesson_data.get('video', lesson.video)
    #                 lesson.video_st = lesson_data.get('video_st', lesson.video_st)
    #                 lesson.lex_st = lesson_data.get('lex_st', lesson.lex_st)
    #                 lesson.phr_st = lesson_data.get('phr_st', lesson.phr_st)
    #                 lesson.dialog_st = lesson_data.get('dialog_st', lesson.dialog_st)
    #                 lesson.rules_st = lesson_data.get('rules_st', lesson.rules_st)
    #                 lesson.save()
    #                 keep_lessons.append(lesson.id_les)
    #                 exercises_info = validated_data.pop('exercises_info')
    #                 keep_exercises = []
    #                 for exercise_data in exercises_info:
    #                     les_ex = exercise_data.get('id_ex', None)
    #                     # if "id_les" in lesson_data.keys(): 'id_ex', 'type', 'lesson', 'num_ex',
    #                     print("tyt")
    #                     if les_ex:
    #                         if Exercises.objects.filter(id_ex=exercise_data["id_ex"]).exists():
    #                             exercise = Exercises.objects.get(id_les=exercise_data["id_ex"])
    #                             exercise.type = lesson_data.get('type', exercise.type)
    #                             # lesson.lessonblock = lesson_data('lessonblock', instance.id_lb)
    #                             exercise.num_ex = lesson_data.get('num_ex', exercise.num_ex)
    #                             exercise.save()
    #                             keep_exercises.append(exercise.id_ex)
    #
    #                         else:
    #                             continue
    #                     else:
    #                         exercise = Exercises.objects.create(**exercise_data, lesson=lesson)
    #                         keep_exercises.append(exercise.id_ex)
    #                 for exercise_data in lesson.exercises_info:
    #                     if exercise_data.id_ex not in keep_exercises:
    #                         exercise_data.delete()
    #             else:
    #                 continue
    #         else:
    #             lesson = Lessons.objects.create(**lesson_data, lessonblock=instance)
    #             keep_lessons.append(lesson.id_les)
    #     for lesson_data in instance.lesson_info:
    #         if lesson_data.id_les not in keep_lessons:
    #             lesson_data.delete()
    #     return instance
# def update(self, instance, validated_data):
    #     lessons_data = validated_data.get('lesson_info')
    #     instance.save()
    #
    #     for lesson_data in lessons_data:
    #         les_id = lesson_data.get('id_les', None)
    #         if les_id:
    #             print("yes")
    #             lesson = Lessons.objects.get(id_les=les_id)
    #             lesson.name_les = lesson_data.get('name_les', lesson.name_les)
    #             lesson.lessonblock = lesson_data('lessonblock', instance.id_lb)
    #             lesson.video = lesson_data.get('video', lesson.video)
    #             lesson.video_st = lesson_data.get('video_st', lesson.video_st)
    #             lesson.lex_st = lesson_data.get('lex_st', lesson.lex_st)
    #             lesson.phr_st = lesson_data.get('phr_st', lesson.phr_st)
    #             lesson.dialog_st = lesson_data.get('dialog_st', lesson.dialog_st)
    #             lesson.rules_st = lesson_data.get('rules_st', lesson.rules_st)
    #             lesson.save()
    #         else:
    #             print("no")
    #             Lessons.objects.create(**lesson_data, lessonblock=instance)
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
