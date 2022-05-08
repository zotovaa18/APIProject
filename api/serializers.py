# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 22:20:50 2021

@author: zotov
"""

from rest_framework import serializers
from django.db import transaction

from .models import Countries, PeopleGroups, People, TypesLex, TypesMed, LessonBlocks, Lessons
from .models import Lexemes, Medias, Ik, Replicas, LecFilling, Rules, RulesLexemes, TypesEx, ShowInfoAboutWordsLetters
from .models import Exercises, Progress, Tasks, Variants, Favorites, Status, VowelSound, ShowInfoAboutRules
# from .models import Newletters, Newwords, Newphrases, Matchsyllablessound, Collectwordsletters, Missingletter
# from .models import Pronunciationwords, Recoverphrases, Selectwords, Wordpicturematch, Wordpictureselect, Writewords
from .models import ShowInfoAboutWordsLetters, ShowInfoAboutPhrase, ForLessonsDTO
from .models import *


class RatingSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)
    class Meta:
        model = Rating
        fields = ['name', 'surname', 'photo', 'count']


class TimeSpentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSpent
        fields = '__all__'


class NumStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumStop
        fields = ['block', 'name_les', 'login', 'stop']


class WeakPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeakPoints
        fields = ['name_les', 'id_les', 'login', 'total', 'completed', 'count', 'type']


class WeaksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weaks
        fields = ['name_les', 'id_les', 'login', 'total', 'completed','data']


class DeleteDTOSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeleteDTO
        fields = ['id_les', 'id_ex', 'login']


class ProgressBlocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressBlocks
        fields = ['name_les', 'login', 'sum']


class NumberOfWeakPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberOfWeakPoints
        fields = ['name_les', 'login', 'count', 'type']


# class WeakPointsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WeakPoints
#         fields = ['login', 'weak']


class PeopleGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleGroups
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class CountriesSerializer(serializers.ModelSerializer):
    flag_link = serializers.ImageField(required=False)

    class Meta:
        model = Countries
        fields = '__all__'


class PeopleSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)

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
    #sound_rule = serializers.FileField(required=False)
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
    # variants = VariantsWriteSerializer(many=True)
    class Meta:
        model = Tasks
        fields = ('id_task', 'exercise', 'num_task', 'lex_right', 'type', 'num_lex', 'count_miss', 'picture', 'sound',
                  'replic', 'pronunciation',)


class TasksReadSerializer(serializers.ModelSerializer):
    class Meta(TasksWriteSerializer.Meta):
        depth = 2


class ExercisesWriteSerializer(serializers.ModelSerializer):
    # task = TasksWriteSerializer(many=True)
    # lesson = serializers.PrimaryKeyRelatedField(queryset=Lessons.objects.all())
    # type = serializers.PrimaryKeyRelatedField(queryset=TypesEx.objects.all())
    class Meta:
        model = Exercises
        fields = ('id_ex', 'type', 'lesson', 'num_ex',)


class ExercisesReadSerializer(serializers.ModelSerializer):
    class Meta(ExercisesWriteSerializer.Meta):
        depth = 5


class LessonInfoDTOWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonInfoDTO
        # fields = "__all__"
        # read_only_fields = ('lesson')
        exclude = ('forlesson',)


class RulesDTOWriteSerializer(serializers.ModelSerializer):
    # vl_var = VlWriteSerializer(many=True)
    # id_var = serializers.PrimaryKeyRelatedField(many=True, queryset=Lexemes.objects.all())
    #picture = serializers.ImageField(required=False)
    #sound_rule = serializers.FileField(required=False)
    id = serializers.IntegerField(required=False)
    id_lex = serializers.PrimaryKeyRelatedField(many=True, queryset=Lexemes.objects.all(), allow_null=True,
                                                required=False)

    class Meta:
        model = RulesDTO
        fields = '__all__'

    def create(self, validated_data):
        # vls_data = validated_data.pop('vl_var')
        print('near rulesdto')
        picture = validated_data.get('picture')
        sound_rule = validated_data.get('sound_rule')
        side = validated_data.get('side')
        type_ex = validated_data.get('type_ex')
        num_ex = validated_data.get('num_ex')
        rulesdto = RulesDTO.objects.create(type_ex=type_ex, num_ex=num_ex, side=side,
                                           sound_rule=sound_rule, picture=picture)
        rulesdto.id_var.set(validated_data.get('id_var'))
        rulesdto.id_lex.set(validated_data.get('id_lex'))
        rulesdto.save()
        # print('near for')
        # print(vls_data)
        # for vl_data in vls_data:
        #     v = Vl.objects.create(id_r=rulesdto, **vl_data)
        #     v.save()
        #     #rulesdto.vl_var.set(v.id)
        return rulesdto


class LexDTOWriteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    id_lex = serializers.PrimaryKeyRelatedField(many=True, queryset=Lexemes.objects.all())
    id_miss = serializers.ListField(child=serializers.IntegerField(), allow_null=True, required=False)
    id_var = serializers.PrimaryKeyRelatedField(many=True, queryset=Lexemes.objects.all(), allow_null=True,
                                                required=False)

    # vl_lex = VlLexWriteSerializer(many=True, allow_null=True, required=False)
    # vl_miss = VlMissWriteSerializer(many=True, allow_null=True, required=False)
    # vl_variant = VlVarWriteSerializer(many=True, allow_null=True, required=False)
    class Meta:
        model = LexDTO
        fields = ['id', 'type_ex', 'num_ex', 'id_lex', 'id_miss', 'id_var', 'forlesson']

    @transaction.atomic
    def create(self, validated_data):

        print('near lexdto')
        type_ex = validated_data.get('type_ex')
        num_ex = validated_data.get('num_ex')

        print(validated_data.get('type_ex').type_ex)
        if (validated_data.get('type_ex').type_ex == 2) or (validated_data.get('type_ex').type_ex == 7) or \
                (validated_data.get('type_ex').type_ex == 5) or (validated_data.get('type_ex').type_ex == 15) or \
                (validated_data.get('type_ex').type_ex == 6):
            if (validated_data.get('type_ex').type_ex == 2) or (validated_data.get('type_ex').type_ex == 7):
                lexdto = LexDTO.objects.create(type_ex=type_ex, num_ex=num_ex)
                lexdto.id_lex.set(validated_data.get('id_lex'))

                lexdto.save()

            elif validated_data.get('type_ex').type_ex == 6:

                lexdto = LexDTO.objects.create(type_ex=type_ex, num_ex=num_ex)
                lexdto.id_lex.set(validated_data.get('id_lex'))

                lexdto.save()

                for i in validated_data.get('id_var'):
                    print(i)
                    a = LexDTO.objects.get(id=lexdto.id)
                    a.id_var.add(i)
                a.save()

            else:
                print('near 5 15')

                if validated_data.get('type_ex').type_ex == 5:

                    lexdto = LexDTO.objects.create(type_ex=type_ex, num_ex=num_ex)
                    lexdto.id_lex.set(validated_data.get('id_lex'))

                    lexdto.id_miss = validated_data.get('id_miss')
                    lexdto.save()

                    print('near 5 task')
                    for i in validated_data.get('id_var'):
                        print(i)
                        a = LexDTO.objects.get(id=lexdto.id)
                        a.id_var.add(i)
                    a.save()

                else:
                    print('in 15 exercises')

                    lexdto = LexDTO.objects.create(type_ex=type_ex, num_ex=num_ex)
                    lexdto.id_lex.set(validated_data.get('id_lex'))

                    lexdto.id_miss = validated_data.get('id_miss')
                    lexdto.save()
                    for i in validated_data.get('id_var'):
                        print(i)
                        a = LexDTO.objects.get(id=lexdto.id)
                        a.id_var.add(i)
                    a.save()

        else:
            print('in else 1 3 14... exercises')
            lexdto = LexDTO.objects.create(type_ex=type_ex, num_ex=num_ex)
            lexdto.id_lex.set(validated_data.get('id_lex'))

            lexdto.save()

        return lexdto


class DialogDTOWriteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    id_rep = serializers.ListField(child=serializers.IntegerField(), allow_null=True, required=False)
    id_miss = serializers.ListField(child=serializers.IntegerField(), allow_null=True, required=False)

    # vl_rep = VlRepWriteSerializer(many=True, allow_null=True, required=False)
    # vl_miss = VlMissDWriteSerializer(many=True, allow_null=True, required=False)

    # {
    #     "type_ex": 21,
    #     "num_ex": 10,
    #     "id_rep": [96],
    #     "pic_video": "ссылка"
    # }
    # {
    #     "type_ex": 22,
    #     "num_ex": 10,
    #     "id_rep": [3, 11, 12, 14, 10, 13],
    #     "id_miss": [1, 3, 6],
    #     "pic_video": "ссылка"
    # }
    class Meta:
        model = DialogDTO
        fields = ['id', 'type_ex', 'num_ex', 'id_rep', 'id_miss', 'forlesson']

    def create(self, validated_data):

        print('near dialogdto')
        type_ex = validated_data.get('type_ex')
        num_ex = validated_data.get('num_ex')

        dialogdto = DialogDTO.objects.create(type_ex=type_ex, num_ex=num_ex)
        dialogdto.id_rep = validated_data.get('id_rep')
        dialogdto.save()
        print(validated_data.get('type_ex').type_ex)
        if validated_data.get('type_ex').type_ex == 22:

        #     dialogdto.pic_video = validated_data.get('pic_video')
        #     dialogdto.save()
        #
        # else:

            # vls_data = validated_data.pop('vl_rep')
            # print('near vl_rep')
            # for vl_data in vls_data:
            #     v = VlRep.objects.create(id_dialogdto=dialogdto, **vl_data)
            #     v.save()

            dialogdto.id_miss = validated_data.get('id_miss')

            # vls_data = validated_data.pop('vl_miss')
            # print('near vl_miss')
            # for vl_data in vls_data:
            #     v = VlMissD.objects.create(id_dialogdto=dialogdto, **vl_data)
            #     v.save()

        return dialogdto


class PhrasesDTOWriteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    id_rep = serializers.PrimaryKeyRelatedField(many=True, queryset=Replicas.objects.all())
    id_miss = serializers.ListField(child=serializers.IntegerField(), allow_null=True, required=False)
    id_var = serializers.PrimaryKeyRelatedField(many=True, queryset=Lexemes.objects.all(), allow_null=True,
                                                required=False)

    class Meta:
        model = PhrasesDTO
        fields = ['id', 'type_ex', 'num_ex', 'id_rep', 'id_miss', 'id_var', 'forlesson']

    def create(self, validated_data):

        print('near phrasedto')
        type_ex = validated_data.get('type_ex')
        num_ex = validated_data.get('num_ex')
        phrasedto = PhrasesDTO.objects.create(type_ex=type_ex, num_ex=num_ex)
        phrasedto.id_rep.set(validated_data.get('id_rep'))

        phrasedto.save()
        print(validated_data.get('type_ex').type_ex)

        if (validated_data.get('type_ex').type_ex == 19) or (validated_data.get('type_ex').type_ex == 20):
            phrasedto.id_miss = validated_data.get('id_miss')
            if validated_data.get('type_ex').type_ex == 20:
                phrasedto.id_var.set(validated_data.get('id_var'))
        phrasedto.save()
        return phrasedto


class ForLessonsDTOWriteSerializer(serializers.ModelSerializer):
    lesson_info = LessonInfoDTOWriteSerializer()
    rules = RulesDTOWriteSerializer(many=True)
    dialogs = DialogDTOWriteSerializer(many=True)
    lex = LexDTOWriteSerializer(many=True)
    phrases = PhrasesDTOWriteSerializer(many=True)

    #
    # {
    #     "name_les": "Тест 01.05_",
    #     "lessonblock": 1,
    #     "video": 1,
    #     "lesson_info": {
    #         "video_st": "В процессе",
    #         "lex_st": "В процессе",
    #         "phr_st": "В процессе",
    #         "dialog_st": "В процессе",
    #         "rules_st": "В процессе"
    #     },
    #     "rules": [
    #         {
    #             "type_ex": 23,
    #             "num_ex": 1,
    #             "id_var": [
    #                 61,
    #                 62
    #             ],
    #             "side": "право",
    #             "sound_rule": "123",
    #             "picture": "123"
    #         },
    #         {
    #             "type_ex": 17,
    #             "num_ex": 2,
    #             "id_lex": [
    #                 60
    #             ],
    #             "id_var": [
    #                 61,
    #                 62,
    #                 63
    #             ],
    #             "sound_rule": "123",
    #             "picture": "123"
    #         }
    #     ],
    #     "lex": [
    #         {
    #             "type_ex": 14,
    #             "num_ex": 3,
    #             "id_lex": [
    #                 62
    #             ]
    #         },
    #         {
    #             "type_ex": 3,
    #             "num_ex": 4,
    #             "id_lex": [
    #                 63
    #             ]
    #         },
    #         {
    #             "type_ex": 2,
    #             "num_ex": 5,
    #             "id_lex": [
    #                 72,
    #                 71
    #             ]
    #         },
    #         {
    #             "type_ex": 1,
    #             "num_ex": 6,
    #             "id_lex": [
    #                 74
    #             ]
    #         },
    #         {
    #             "type_ex": 18,
    #             "num_ex": 7,
    #             "id_lex": [
    #                 80
    #             ]
    #         },
    #         {
    #             "type_ex": 7,
    #             "num_ex": 8,
    #             "id_lex": [
    #                 72,
    #                 71,
    #                 76,
    #                 77
    #             ]
    #         },
    #         {
    #             "type_ex": 5,
    #             "num_ex": 9,
    #             "id_lex": [
    #                 74
    #             ],
    #             "id_miss": [
    #                 1
    #             ],
    #             "id_var": [
    #                 61,
    #                 62,
    #                 63
    #             ]
    #         },
    #         {
    #             "type_ex": 15,
    #             "num_ex": 10,
    #             "id_lex": [
    #                 60
    #             ],
    #             "id_miss": [
    #                 1,
    #                 2
    #             ],
    #             "id_var": [
    #                 61,
    #                 62,
    #                 63
    #             ]
    #         },
    #         {
    #             "type_ex": 6,
    #             "num_ex": 11,
    #             "id_lex": [
    #                 60
    #             ],
    #             "id_var": [
    #                 61,
    #                 62,
    #                 63
    #             ]
    #         }
    #     ],
    #     "phrases": [
    #         {
    #             "type_ex": 4,
    #             "num_ex": 16,
    #             "id_rep": [
    #                 3
    #             ]
    #         },
    #         {
    #             "type_ex": 19,
    #             "num_ex": 15,
    #             "id_rep": [
    #                 3
    #             ],
    #             "id_miss": [
    #                 1
    #             ]
    #         },
    #         {
    #             "type_ex": 20,
    #             "num_ex": 14,
    #             "id_rep": [
    #                 8
    #             ],
    #             "id_var": [
    #                 75
    #             ],
    #             "id_miss": [
    #                 1,
    #                 4
    #             ]
    #         }
    #     ],
    #     "dialogs": [
    #         {
    #             "type_ex": 21,
    #             "num_ex": 12,
    #             "id_rep": [
    #                 95
    #             ]
    #         },
    #         {
    #             "type_ex": 22,
    #             "num_ex": 13,
    #             "id_rep": [
    #                 3,
    #                 11,
    #                 12,
    #                 14,
    #                 10,
    #                 13
    #             ],
    #             "id_miss": [
    #                 1,
    #                 3,
    #                 6
    #             ]
    #         }
    #     ],
    #     "description": ""
    # }

    class Meta:
        model = ForLessonsDTO
        fields = ['id', 'name_les', 'lessonblock', 'video', 'lesson_info', 'rules', 'lex', 'phrases', 'dialogs',
                  'description']

    @transaction.atomic
    def create(self, validated_data):
        #with transaction.atomic():
        lessons_info_data = validated_data.pop('lesson_info')
        rules_data = validated_data.pop('rules')
        phrases_data = validated_data.pop('phrases')
        dialogs_data = validated_data.pop('dialogs')
        lexs_data = validated_data.pop('lex')
        forlessonsdto = ForLessonsDTO.objects.create(id=ForLessonsDTO.objects.order_by("id").values_list("id", flat=True).last() + 1,
                                                     **validated_data)

        print('near les')
        print(forlessonsdto.id)
        list_id_lb = LessonBlocks.objects.values_list('id_lb', flat=True)
        if forlessonsdto.lessonblock not in list_id_lb:
            lb = LessonBlocks.objects.create(id_lb=forlessonsdto.lessonblock)
            lb.save()
        lb1 = LessonBlocks.objects.get(id_lb=forlessonsdto.lessonblock)
        les = Lessons.objects.create(id_les=forlessonsdto.id,
                                     name_les=forlessonsdto.name_les, lessonblock=lb1,
                                     video=forlessonsdto.video, **lessons_info_data)
        les.save()
        LessonInfoDTO.objects.create(id=forlessonsdto.id, forlesson=forlessonsdto, **lessons_info_data)

        for rule_data in rules_data:
            list_id = Rules.objects.values_list('id_r', flat=True)
            if rule_data.get('type_ex').type_ex == 23:
                print("in if")
                # if RulesDTO.objects.order_by("id").values_list("id", flat=True).last() in list_id:
                #     r = RulesDTO.objects.create(,
                #                             forlesson=forlessonsdto, type_ex=rule_data.get('type_ex'),
                #                             num_ex=rule_data.get('num_ex'),
                #                             picture=rule_data.get('picture'), side=rule_data.get('side'),
                #                             sound_rule=rule_data.get('sound_rule'))
                #     r.save()
                # else:
                m = max(Exercises.objects.order_by("id_ex").values_list("id_ex", flat=True).last() + 1,
                        RulesDTO.objects.order_by("id").values_list("id", flat=True).last() + 1)
                r = RulesDTO.objects.create(id = m,
                                            forlesson=forlessonsdto, type_ex=rule_data.get('type_ex'),
                                            num_ex=rule_data.get('num_ex'),
                                            picture=rule_data.get('picture'), side=rule_data.get('side'),
                                            sound_rule=rule_data.get('sound_rule'))
                r.save()
                print('near rule if')
                print(r.id)
                rule = Rules.objects.create(id_r=r.id, lesson=les,
                                            picture=rule_data.get('picture'), side=rule_data.get('side'),
                                            sound_rule=rule_data.get('sound_rule'))
                # for i in rule_data.get('id_var'):
                #     print(i)
                #     rule.lexeme.add(i)
                # rule.save()
                rule.lexeme.set(rule_data.get('id_var'))
                rule.save()

                for i in rule_data.get('id_var'):
                    print(i)
                    a = RulesDTO.objects.get(id=r.id)
                    a.id_var.add(i)
                    a.save()

            else:
                print('in else')
                m = max(Exercises.objects.order_by("id_ex").values_list("id_ex", flat=True).last() + 1,
                        RulesDTO.objects.order_by("id").values_list("id", flat=True).last() + 1)
                ex = Exercises.objects.create(id_ex=m,
                                              type=rule_data.get('type_ex'), lesson=les, num_ex=rule_data.get('num_ex'))
                ex.save()
                print('near task')
                task = Tasks.objects.create(exercise=ex, num_task=1, lex_right=rule_data.get('id_lex')[0],
                                            picture=rule_data.get('picture'), sound=rule_data.get('sound_rule'))
                task.save()

                for i in rule_data.get('id_var'):
                    print(i)
                    variant = Variants.objects.create(task=task, lexeme=i)
                    variant.save()

                print('near rulesDTO')
                # if RulesDTO.objects.order_by("id").values_list("id", flat=True).last() in list_id:
                #     RulesDTO.objects.create(,
                #                             forlesson=forlessonsdto, type_ex=rule_data.get('type_ex'),
                #                             num_ex=rule_data.get('num_ex'), id_lex=rule_data.get('id_lex'),
                #                             picture=rule_data.get('picture'), side=rule_data.get('side'),
                #                             sound_rule=rule_data.get('sound_rule'))
                # else:
                r = RulesDTO.objects.create(id=ex.id_ex,
                                            forlesson=forlessonsdto, type_ex=rule_data.get('type_ex'),
                                            num_ex=rule_data.get('num_ex'),
                                            picture=rule_data.get('picture'), side=rule_data.get('side'),
                                            sound_rule=rule_data.get('sound_rule'))
                r.save()

                for i in rule_data.get('id_lex'):
                    print(i)
                    a = RulesDTO.objects.get(id=r.id)
                    a.id_lex.add(i)
                a.save()

                for i in rule_data.get('id_var'):
                    print(i)
                    a = RulesDTO.objects.get(id=r.id)
                    a.id_var.add(i)
                a.save()

        for lex_data in lexs_data:
            m = max(Exercises.objects.order_by("id_ex").values_list("id_ex", flat=True).last() + 1,
                    RulesDTO.objects.order_by("id").values_list("id", flat=True).last() + 1)
            if (lex_data.get('type_ex').type_ex == 2) or (lex_data.get('type_ex').type_ex == 7) or \
                    (lex_data.get('type_ex').type_ex == 5) or (lex_data.get('type_ex').type_ex == 15) or \
                    (lex_data.get('type_ex').type_ex == 6):
                if (lex_data.get('type_ex').type_ex == 2) or (lex_data.get('type_ex').type_ex == 7):

                    print('in if 2 7 exercises')
                    ex = Exercises.objects.create(id_ex=m,
                                                  type=lex_data.get('type_ex'), lesson=les,
                                                  num_ex=lex_data.get('num_ex'))
                    ex.save()

                    lex = LexDTO.objects.create(
                        id=ex.id_ex,
                        forlesson=forlessonsdto, type_ex=lex_data.get('type_ex'),
                        num_ex=lex_data.get('num_ex'))
                    lex.save()

                    for i in lex_data.get('id_lex'):
                        print(i)
                        a = LexDTO.objects.get(id=lex.id)
                        a.id_lex.add(i)
                    a.save()
                    print('near if 2 7  task')
                    count = 0
                    for i in lex_data.get('id_lex'):
                        count = count + 1
                        print(i)
                        task = Tasks.objects.create(exercise=ex, num_task=count, lex_right=i)
                        task.save()

                elif lex_data.get('type_ex').type_ex == 6:
                    print('in elif 6 exercises')
                    ex = Exercises.objects.create(id_ex=m,
                                                  type=lex_data.get('type_ex'), lesson=les,
                                                  num_ex=lex_data.get('num_ex'))
                    ex.save()
                    lex = LexDTO.objects.create(
                        id=ex.id_ex,
                        forlesson=forlessonsdto, type_ex=lex_data.get('type_ex'),
                        num_ex=lex_data.get('num_ex'))
                    lex.save()

                    for i in lex_data.get('id_lex'):
                        print(i)
                        a = LexDTO.objects.get(id=lex.id)
                        a.id_lex.add(i)
                    a.save()

                    for i in lex_data.get('id_var'):
                        print(i)
                        a = LexDTO.objects.get(id=lex.id)
                        a.id_var.add(i)
                    a.save()

                    print('near elif 6 task')
                    task = Tasks.objects.create(exercise=ex, num_task=1, lex_right=lex_data.get('id_lex')[0])
                    task.save()

                    for i in lex_data.get('id_var'):
                        print(i)
                        variant = Variants.objects.create(task=task, lexeme=i)
                        variant.save()

                else:
                    print('near 5 15')

                    if lex_data.get('type_ex').type_ex == 5:
                        print('in if 5 exercises')
                        ex = Exercises.objects.create(id_ex=m,
                                                      type=lex_data.get('type_ex'), lesson=les,
                                                      num_ex=lex_data.get('num_ex'))
                        ex.save()
                        lex = LexDTO.objects.create(
                            id=ex.id_ex,
                            forlesson=forlessonsdto, type_ex=lex_data.get('type_ex'),
                            num_ex=lex_data.get('num_ex'))

                        lex.id_miss = lex_data.get('id_miss')
                        lex.save()

                        for i in lex_data.get('id_lex'):
                            print(i)
                            a = LexDTO.objects.get(id=lex.id)
                            a.id_lex.add(i)
                        a.save()

                        print('near 5 task')
                        for i in lex_data.get('id_var'):
                            print(i)
                            a = LexDTO.objects.get(id=lex.id)
                            a.id_var.add(i)
                        a.save()
                        task = Tasks.objects.create(exercise=ex, num_task=1, lex_right=lex_data.get('id_lex')[0],
                                                    num_lex=lex_data.get('id_miss')[0])
                        task.save()

                        print('near 5 variants')
                        for i in lex_data.get('id_var'):
                            print(i)
                            variant = Variants.objects.create(task=task, lexeme=i)
                            variant.save()
                    else:
                        print('in 15 exercises')
                        ex = Exercises.objects.create(id_ex=m,
                                                      type=lex_data.get('type_ex'), lesson=les,
                                                      num_ex=lex_data.get('num_ex'))
                        ex.save()
                        lex = LexDTO.objects.create(
                            id=ex.id_ex,
                            forlesson=forlessonsdto, type_ex=lex_data.get('type_ex'),
                            num_ex=lex_data.get('num_ex'))
                        lex.id_miss = lex_data.get('id_miss')
                        lex.save()
                        for i in lex_data.get('id_var'):
                            print(i)
                            a = LexDTO.objects.get(id=lex.id)
                            a.id_var.add(i)
                        a.save()

                        for i in lex_data.get('id_lex'):
                            print(i)
                            a = LexDTO.objects.get(id=lex.id)
                            a.id_lex.add(i)
                        a.save()

                        print('near 15 task')
                        count = 0
                        flag = False
                        for i in lex_data.get('id_miss'):
                            count = count + 1
                            print(i)
                            if not flag:
                                task = Tasks.objects.create(exercise=ex, num_task=count,
                                                            lex_right=lex_data.get('id_lex')[0], num_lex=i)
                                task.save()
                            else:
                                task1 = Tasks.objects.create(exercise=ex, num_task=count,
                                                             lex_right=lex_data.get('id_lex')[0], num_lex=i)
                                task1.save()

                        print('near 15 variants')
                        print(task.id_task)
                        for i in lex_data.get('id_var'):
                            print(i)
                            variant = Variants.objects.create(task=task, lexeme=i)
                        variant.save()
            else:
                print('in else 1 3 14... exercises')
                ex = Exercises.objects.create(id_ex=m,
                                              type=lex_data.get('type_ex'), lesson=les, num_ex=lex_data.get('num_ex'))
                ex.save()

                lex = LexDTO.objects.create(
                    id=ex.id_ex,
                    forlesson=forlessonsdto, type_ex=lex_data.get('type_ex'),
                    num_ex=lex_data.get('num_ex'))
                lex.save()

                for i in lex_data.get('id_lex'):
                    print(i)
                    a = LexDTO.objects.get(id=lex.id)
                    a.id_lex.add(i)
                a.save()
                print('near 1 3 14.... task')
                task = Tasks.objects.create(exercise=ex, num_task=1, lex_right=lex_data.get('id_lex')[0])
                task.save()

        for phrase_data in phrases_data:
            print('near phrasedto')
            type_ex = phrase_data.get('type_ex')
            num_ex = phrase_data.get('num_ex')
            print('in ph exercises')
            m = max(Exercises.objects.order_by("id_ex").values_list("id_ex", flat=True).last() + 1,
                    RulesDTO.objects.order_by("id").values_list("id", flat=True).last() + 1)
            ex = Exercises.objects.create(
                id_ex=m,
                type=phrase_data.get('type_ex'), lesson=les,
                num_ex=phrase_data.get('num_ex'))
            ex.save()
            phrasedto = PhrasesDTO.objects.create(forlesson=forlessonsdto, id=ex.id_ex, type_ex=type_ex, num_ex=num_ex)
            phrasedto.id_rep.set(phrase_data.get('id_rep'))

            print(phrase_data.get('type_ex').type_ex)

            if (phrase_data.get('type_ex').type_ex == 19) or (phrase_data.get('type_ex').type_ex == 20):
                phrasedto.id_miss = phrase_data.get('id_miss')
                if phrase_data.get('type_ex').type_ex == 20:
                    phrasedto.id_var.set(phrase_data.get('id_var'))
                    print('near 20 task')
                    count = 0
                    flag = False
                    for i in phrase_data.get('id_miss'):
                        count = count + 1
                        print(i)
                        if not flag:
                            task = Tasks.objects.create(exercise=ex, num_task=count,
                                                        replic=phrase_data.get('id_rep')[0], num_lex=i)
                            task.save()
                        else:
                            task1 = Tasks.objects.create(exercise=ex, num_task=count,
                                                         replic=phrase_data.get('id_rep')[0], num_lex=i)
                            task1.save()

                    print('near 20 variants')
                    for i in phrase_data.get('id_var'):
                        print(i)
                        variant = Variants.objects.create(task=task, lexeme=i)
                        variant.save()
                else:
                    print('near ph task')
                    task = Tasks.objects.create(exercise=ex, num_task=1, replic=phrase_data.get('id_rep')[0],
                                                num_lex=phrase_data.get('id_miss')[0])
                    task.save()
                phrasedto.save()
            else:
                print('near ph task')
                task = Tasks.objects.create(exercise=ex, num_task=1, replic=phrase_data.get('id_rep')[0])
                task.save()

        for dialog_data in dialogs_data:
            print('in exercises')
            m = max(Exercises.objects.order_by("id_ex").values_list("id_ex", flat=True).last() + 1,
                    RulesDTO.objects.order_by("id").values_list("id", flat=True).last() + 1)
            ex = Exercises.objects.create(id_ex=m, type=dialog_data.get('type_ex'), lesson=les,
                                          num_ex=dialog_data.get('num_ex'))
            ex.save()
            print('near dialogdto')
            dialogdto = DialogDTO.objects.create(forlesson=forlessonsdto, id=ex.id_ex,
                                                 type_ex=dialog_data.get('type_ex'), num_ex=dialog_data.get('num_ex'),
                                                 id_rep=dialog_data.get('id_rep'))
            dialogdto.save()

            print(dialog_data.get('type_ex').type_ex)

            if dialog_data.get('type_ex').type_ex == 21:

                print('near 21 task')
                print(dialog_data.get('id_rep')[0])
                #print(Lexemes.objects.get(id_lex=dialog_data.get('id_rep')[0]))
                lexeme = Lexemes.objects.get(id_lex=dialog_data.get('id_rep')[0])
                task = Tasks.objects.create(exercise=ex, num_task=1, lex_right=lexeme)
                task.save()

            else:

                print('near 22 task')
                dialogdto.id_miss = dialog_data.get('id_miss')
                dialogdto.save()
                count = 0
                s = len(dialog_data.get('id_miss'))
                t = 0
                for i in dialog_data.get('id_rep'):
                    count = count + 1
                    print(i)
                    rep = Replicas.objects.get(id_rep=i)
                    if t < s:
                        task = Tasks.objects.create(exercise=ex, num_task=count, replic=rep,
                                                    num_lex=dialog_data.get('id_miss')[t])
                        task.save()
                        t = t + 1
                    else:
                        task = Tasks.objects.create(exercise=ex, num_task=count, replic=rep)
                        task.save()

        return forlessonsdto

    @transaction.atomic
    def update(self, forlessonsdto, validated_data):

        lessons_info_data = validated_data.pop('lesson_info')
        rules_data = validated_data.get('rules')
        print(rules_data)
        phrases_data = validated_data.pop('phrases')
        lexs_data = validated_data.pop('lex')
        dialogs_data = validated_data.pop('dialogs')
        forlessonsdto.name_les = validated_data.get('name_les', forlessonsdto.name_les)
        forlessonsdto.lessonblock = validated_data.get('lessonblock', forlessonsdto.lessonblock)
        forlessonsdto.video = validated_data.get('video', forlessonsdto.video)

        forlessonsdto.description = validated_data.get('description', forlessonsdto.description)
        forlessonsdto.save()

        print('near les')
        print(forlessonsdto.id)
        lb1 = LessonBlocks.objects.get(id_lb=forlessonsdto.lessonblock)
        if Lessons.objects.filter(id_les=forlessonsdto.id).exists():
            print('in 2 if')
            les = Lessons.objects.get(id_les=forlessonsdto.id)
            les.name_les = validated_data.get('name_les')
            les.lessonblock = lb1
            les.video = validated_data.get('video')
            les.video_st = lessons_info_data.get('video_st')
            les.lex_st = lessons_info_data.get('lex_st')
            les.phr_st = lessons_info_data.get('phr_st')
            les.dialog_st = lessons_info_data.get('dialog_st')
            les.rules_st = lessons_info_data.get('rules_st')
            les.save()

            ld = LessonInfoDTO.objects.get(id=forlessonsdto.id)
            ld.video_st = lessons_info_data.get('video_st')
            ld.lex_st = lessons_info_data.get('lex_st')
            ld.phr_st = lessons_info_data.get('phr_st')
            ld.dialog_st = lessons_info_data.get('dialog_st')
            ld.rules_st = lessons_info_data.get('rules_st')
            ld.save()

        list_id_rule = []
        for rule_data in rules_data:
            if rule_data.get('type_ex').type_ex == 23:
                print("in if")
                print(rule_data.get('id'))
                if rule_data.get('id', None):
                    r = RulesDTO.objects.get(id=rule_data.get('id'))
                    r.forlesson = forlessonsdto
                    r.type_ex = rule_data.get('type_ex')
                    r.num_ex = rule_data.get('num_ex')
                    r.picture = rule_data.get('picture')
                    r.side = rule_data.get('side')
                    r.sound_rule = rule_data.get('sound_rule')
                    r.save()

                    rule = Rules.objects.get(id_r=r.id)
                    rule.lesson = les
                    rule.picture = rule_data.get('picture')
                    rule.side = rule_data.get('side')
                    rule.sound_rule = rule_data.get('sound_rule')
                    rule.lexeme.set(rule_data.get('id_var'))
                    rule.save()
                else:
                    print('in else')
                    m = max(Exercises.objects.order_by("id_ex").values_list("id_ex", flat=True).last() + 1,
                            RulesDTO.objects.order_by("id").values_list("id", flat=True).last() + 1)
                    r = RulesDTO.objects.create(id=m,
                                                forlesson=forlessonsdto, type_ex=rule_data.get('type_ex'),
                                                num_ex=rule_data.get('num_ex'),
                                                picture=rule_data.get('picture'), side=rule_data.get('side'),
                                                sound_rule=rule_data.get('sound_rule'))
                    r.id_var.set(rule_data.get('id_var'))
                    r.save()
                    print('near rule if')
                    print(r.id)
                    rule = Rules.objects.create(id_r=r.id, lesson=les,
                                                picture=rule_data.get('picture'), side=rule_data.get('side'),
                                                sound_rule=rule_data.get('sound_rule'))

                    rule.lexeme.set(rule_data.get('id_var'))
                    rule.save()
                list_id_rule.append(r.id)
            else:
                if rule_data.get('id', None):
                    r = RulesDTO.objects.get(id=rule_data.get('id'))
                    r.forlesson = forlessonsdto
                    r.type_ex = rule_data.get('type_ex')
                    r.num_ex = rule_data.get('num_ex')
                    r.picture = rule_data.get('picture')
                    r.side = rule_data.get('side')
                    r.sound_rule = rule_data.get('sound_rule')

                    r.id_var.set(rule_data.get('id_var'))
                    r.id_lex.set(rule_data.get('id_lex'))

                    r.save()

                    ex = Exercises.objects.get(id_ex=r.id)
                    ex.type = rule_data.get('type_ex')
                    ex.lesson = les
                    ex.num_ex = rule_data.get('num_ex')
                    ex.save()
                    print('near task')
                    task = Tasks.objects.get(exercise=ex)
                    task.num_task = 1
                    task.lex_right = rule_data.get('id_lex')[0]
                    task.picture = rule_data.get('picture')
                    task.sound = rule_data.get('sound_rule')
                    task.save()

                    var_id_list = []
                    for i in rule_data.get('id_var'):
                        print(i)
                        obj, created = Variants.objects.get_or_create(task=task, lexeme = i)
                        var_id_list.append(obj.id)

                    vs = Variants.objects.filter(task=task)
                    for v in vs:
                        if v.id not in var_id_list:
                            v.delete()

                else:
                    print('in else')
                    m = max(Exercises.objects.order_by("id_ex").values_list("id_ex", flat=True).last() + 1,
                            RulesDTO.objects.order_by("id").values_list("id", flat=True).last() + 1)
                    ex = Exercises.objects.create(id_ex=m,
                                                  type=rule_data.get('type_ex'), lesson=les,
                                                  num_ex=rule_data.get('num_ex'))
                    ex.save()
                    print('near task')
                    task = Tasks.objects.create(exercise=ex, num_task=1, lex_right=rule_data.get('id_lex')[0],
                                                picture=rule_data.get('picture'), sound=rule_data.get('sound_rule'))
                    task.save()

                    for i in rule_data.get('id_var'):
                        print(i)
                        variant = Variants.objects.create(task=task, lexeme=i)
                        variant.save()

                    print('near rulesDTO')
                    r = RulesDTO.objects.create(id=ex.id_ex,
                                                forlesson=forlessonsdto, type_ex=rule_data.get('type_ex'),
                                                num_ex=rule_data.get('num_ex'),
                                                picture=rule_data.get('picture'), side=rule_data.get('side'),
                                                sound_rule=rule_data.get('sound_rule'))
                    r.save()

                    for i in rule_data.get('id_lex'):
                        print(i)
                        a = RulesDTO.objects.get(id=r.id)
                        a.id_lex.add(i)
                    a.save()

                    for i in rule_data.get('id_var'):
                        print(i)
                        a = RulesDTO.objects.get(id=r.id)
                        a.id_var.add(i)
                    a.save()
                list_id_rule.append(r.id)
        for rule_data in forlessonsdto.rules.all():
            if rule_data.id not in list_id_rule:
                if RulesDTO.objects.filter(id=rule_data.id).exists():
                    rd = RulesDTO.objects.get(id=rule_data.id)
                    rd.delete()
                    if Rules.objects.filter(id_r=rule_data.id).exists():
                        if RulesLexemes.objects.filter(rule=rule_data.id).exists():
                            RulesLexemes.objects.filter(rule=rule_data.id).delete()
                        r = Rules.objects.get(id_r=rule_data.id)
                        r.delete()
                    elif Exercises.objects.filter(id_ex=rule_data.id).exists():
                        ex = Exercises.objects.get(id_ex=rule_data.id)
                        task = Tasks.objects.filter(exercise=ex)
                        for t in task:
                            v = Variants.objects.filter(task=t.id_task)
                            v.delete()
                        task.delete()
                        ex.delete()
                rule_data.delete()

        list_id_lex = []
        for lex_data in lexs_data:
            m = max(Exercises.objects.order_by("id_ex").values_list("id_ex", flat=True).last() + 1,
                    RulesDTO.objects.order_by("id").values_list("id", flat=True).last() + 1)
            print(lex_data)
            if (lex_data.get('type_ex').type_ex == 2) or (lex_data.get('type_ex').type_ex == 7) or \
                    (lex_data.get('type_ex').type_ex == 5) or (lex_data.get('type_ex').type_ex == 15) or \
                    (lex_data.get('type_ex').type_ex == 6):
                if (lex_data.get('type_ex').type_ex == 2) or (lex_data.get('type_ex').type_ex == 7):
                    if lex_data.get('id', None):
                        print(lex_data.get('id'))
                        print('in if 2 7 exercises')
                        ex = Exercises.objects.get(id_ex=lex_data.get('id'))
                        ex.type = lex_data.get('type_ex')
                        ex.lesson = les
                        ex.num_ex = lex_data.get('num_ex')
                        ex.save()

                        lex = LexDTO.objects.get(id=lex_data.get('id'))
                        lex.forlesson = forlessonsdto
                        lex.type_ex = lex_data.get('type_ex')
                        lex.num_ex = lex_data.get('num_ex')
                        lex.id_lex.set(lex_data.get('id_lex'))
                        lex.save()

                        print('near if 2 7  task')
                        count = 0
                        task_id_list = []
                        for i in lex_data.get('id_lex'):
                            count = count + 1
                            print(i)
                            obj, created = Tasks.objects.get_or_create(exercise=ex, num_task=count, lex_right=i)
                            task_id_list.append(obj.id_task)

                        ts = Tasks.objects.filter(exercise=ex)
                        for t in ts:
                            if t.id_task not in task_id_list:
                                t.delete()
                        list_id_lex.append(lex.id)
                    else:

                        print('in if 2 7 exercises')
                        ex = Exercises.objects.create(id_ex=m,
                                                      type=lex_data.get('type_ex'), lesson=les,
                                                      num_ex=lex_data.get('num_ex'))
                        ex.save()

                        lex = LexDTO.objects.create(
                            id=ex.id_ex,
                            forlesson=forlessonsdto, type_ex=lex_data.get('type_ex'),
                            num_ex=lex_data.get('num_ex'))
                        lex.save()

                        for i in lex_data.get('id_lex'):
                            print(i)
                            a = LexDTO.objects.get(id=lex.id)
                            a.id_lex.add(i)
                        a.save()
                        print('near if 2 7  task')
                        count = 0
                        for i in lex_data.get('id_lex'):
                            count = count + 1
                            print(i)
                            task = Tasks.objects.create(exercise=ex, num_task=count, lex_right=i)
                            task.save()
                        list_id_lex.append(lex.id)
                elif lex_data.get('type_ex').type_ex == 6:
                    if lex_data.get('id', None):
                        ex = Exercises.objects.get(id_ex=lex_data.get('id'))
                        ex.type = lex_data.get('type_ex')
                        ex.lesson = les
                        ex.num_ex = lex_data.get('num_ex')
                        ex.save()

                        lex = LexDTO.objects.get(id=lex_data.get('id'))
                        lex.forlesson = forlessonsdto
                        lex.type_ex = lex_data.get('type_ex')
                        lex.num_ex = lex_data.get('num_ex')
                        lex.id_lex.set(lex_data.get('id_lex'))
                        lex.id_var.set(lex_data.get('id_var'))
                        lex.save()

                        print('near elif 6 task')
                        task = Tasks.objects.get(exercise=ex)
                        task.num_task = 1
                        task.lex_right = lex_data.get('id_lex')[0]
                        task.save()

                        var_id_list = []
                        for i in lex_data.get('id_var'):
                            print(i)
                            obj, created = Variants.objects.get_or_create(task=task, lexeme=i)
                            var_id_list.append(obj.id)

                        vs = Variants.objects.filter(task=task)
                        for v in vs:
                            if v.id not in var_id_list:
                                v.delete()
                        list_id_lex.append(lex.id)
                    else:
                        print('in elif 6 exercises')
                        ex = Exercises.objects.create(id_ex=m,
                                                      type=lex_data.get('type_ex'), lesson=les,
                                                      num_ex=lex_data.get('num_ex'))
                        ex.save()
                        lex = LexDTO.objects.create(
                            id=ex.id_ex,
                            forlesson=forlessonsdto, type_ex=lex_data.get('type_ex'),
                            num_ex=lex_data.get('num_ex'))
                        lex.save()

                        for i in lex_data.get('id_lex'):
                            print(i)
                            a = LexDTO.objects.get(id=lex.id)
                            a.id_lex.add(i)
                        a.save()

                        for i in lex_data.get('id_var'):
                            print(i)
                            a = LexDTO.objects.get(id=lex.id)
                            a.id_var.add(i)
                        a.save()

                        print('near elif 6 task')
                        task = Tasks.objects.create(exercise=ex, num_task=1, lex_right=lex_data.get('id_lex')[0])
                        task.save()

                        for i in lex_data.get('id_var'):
                            print(i)
                            variant = Variants.objects.create(task=task, lexeme=i)
                            variant.save()
                        list_id_lex.append(lex.id)
                else:
                    print('near 5 15')
                    if lex_data.get('type_ex').type_ex == 5:
                        if lex_data.get('id', None):
                            ex = Exercises.objects.get(id_ex=lex_data.get('id'))
                            ex.type = lex_data.get('type_ex')
                            ex.lesson = les
                            ex.num_ex = lex_data.get('num_ex')
                            ex.save()

                            lex = LexDTO.objects.get(id=lex_data.get('id'))
                            lex.forlesson = forlessonsdto
                            lex.type_ex = lex_data.get('type_ex')
                            lex.num_ex = lex_data.get('num_ex')
                            lex.id_lex.set(lex_data.get('id_lex'))
                            lex.id_var.set(lex_data.get('id_var'))
                            lex.id_miss = lex_data.get('id_miss')
                            lex.save()

                            print('near 5 task')
                            task = Tasks.objects.get(exercise=ex)
                            task.num_task = 1
                            task.lex_right = lex_data.get('id_lex')[0]
                            task.num_lex = lex_data.get('id_miss')[0]
                            task.save()

                            print('near 5 variants')
                            var_id_list = []
                            for i in lex_data.get('id_var'):
                                print(i)
                                obj, created = Variants.objects.get_or_create(task=task, lexeme=i)
                                var_id_list.append(obj.id)

                            vs = Variants.objects.filter(task=task)
                            for v in vs:
                                if v.id not in var_id_list:
                                    v.delete()
                            list_id_lex.append(lex.id)
                        else:
                            print('in if 5 exercises')
                            ex = Exercises.objects.create(id_ex=m,
                                                          type=lex_data.get('type_ex'), lesson=les,
                                                          num_ex=lex_data.get('num_ex'))
                            ex.save()
                            lex = LexDTO.objects.create(
                                id=ex.id_ex,
                                forlesson=forlessonsdto, type_ex=lex_data.get('type_ex'),
                                num_ex=lex_data.get('num_ex'))
                            lex.save()
                            lex.id_miss = lex_data.get('id_miss')
                            for i in lex_data.get('id_lex'):
                                print(i)
                                a = LexDTO.objects.get(id=lex.id)
                                a.id_lex.add(i)
                            a.save()

                            print('near 5 task')
                            for i in lex_data.get('id_var'):
                                print(i)
                                a = LexDTO.objects.get(id=lex.id)
                                a.id_var.add(i)
                            a.save()
                            task = Tasks.objects.create(exercise=ex, num_task=1, lex_right=lex_data.get('id_lex')[0],
                                                        num_lex=lex_data.get('id_miss')[0])
                            task.save()

                            print('near 5 variants')
                            for i in lex_data.get('id_var'):
                                print(i)
                                variant = Variants.objects.create(task=task, lexeme=i)
                                variant.save()
                            list_id_lex.append(lex.id)
                    else:
                        print('in 15 exercises')
                        if lex_data.get('id', None):
                            ex = Exercises.objects.get(id_ex=lex_data.get('id'))
                            ex.type = lex_data.get('type_ex')
                            ex.lesson = les
                            ex.num_ex = lex_data.get('num_ex')
                            ex.save()

                            lex = LexDTO.objects.get(id=lex_data.get('id'))
                            lex.forlesson = forlessonsdto
                            lex.type_ex = lex_data.get('type_ex')
                            lex.num_ex = lex_data.get('num_ex')
                            lex.id_lex.set(lex_data.get('id_lex'))
                            lex.id_var.set(lex_data.get('id_var'))
                            lex.id_miss = lex_data.get('id_miss')
                            lex.save()

                            print('near 15 task')
                            count = 0
                            flag = False
                            task_id_list = []
                            for i in lex_data.get('id_miss'):
                                count = count + 1
                                print(i)
                                if not flag:
                                    obj, created = Tasks.objects.get_or_create(exercise=ex, num_task=count,
                                                                               lex_right=lex_data.get('id_lex')[0],
                                                                               num_lex=i)
                                    task_id_list.append(obj.id_task)
                                else:
                                    obj1, created1 = Tasks.objects.get_or_create(exercise=ex, num_task=count,
                                                                                 lex_right=lex_data.get('id_lex')[0],
                                                                                 num_lex=i)
                                    task_id_list.append(obj1.id_task)
                            ts = Tasks.objects.filter(exercise=ex)
                            for t in ts:
                                if t.id_task not in task_id_list:
                                    t.delete()
                            print('near 15 variants')

                            var_id_list = []
                            for i in lex_data.get('id_var'):
                                print(i)
                                obj2, created = Variants.objects.get_or_create(task=obj, lexeme=i)
                                var_id_list.append(obj2.id)

                            vs = Variants.objects.filter(task=obj)
                            for v in vs:
                                if v.id not in var_id_list:
                                    v.delete()
                            list_id_lex.append(lex.id)
                        else:
                            ex = Exercises.objects.create(id_ex=m,
                                                          type=lex_data.get('type_ex'), lesson=les,
                                                          num_ex=lex_data.get('num_ex'))
                            ex.save()
                            lex = LexDTO.objects.create(
                                id=ex.id_ex,
                                forlesson=forlessonsdto, type_ex=lex_data.get('type_ex'),
                                num_ex=lex_data.get('num_ex'))
                            lex.save()
                            lex.id_miss = lex_data.get('id_miss')
                            for i in lex_data.get('id_lex'):
                                print(i)
                                a = LexDTO.objects.get(id=lex.id)
                                a.id_lex.add(i)
                            a.save()

                            print('near 15 task')
                            count = 0
                            flag = False
                            for i in lex_data.get('id_miss'):
                                count = count + 1
                                print(i)
                                if not flag:
                                    task = Tasks.objects.create(exercise=ex, num_task=count,
                                                                lex_right=lex_data.get('id_lex')[0], num_lex=i)
                                    task.save()
                                else:
                                    task1 = Tasks.objects.create(exercise=ex, num_task=count,
                                                                 lex_right=lex_data.get('id_lex')[0], num_lex=i)
                                    task1.save()

                            print('near 15 variants')
                            for i in lex_data.get('id_var'):
                                print(i)
                                variant = Variants.objects.create(task=task, lexeme=i)
                                variant.save()
            else:
                if lex_data.get('id', None):
                    ex = Exercises.objects.get(id_ex=lex_data.get('id'))
                    ex.type = lex_data.get('type_ex')
                    ex.lesson = les
                    ex.num_ex = lex_data.get('num_ex')
                    ex.save()

                    lex = LexDTO.objects.get(id=lex_data.get('id'))
                    lex.forlesson = forlessonsdto
                    lex.type_ex = lex_data.get('type_ex')
                    lex.num_ex = lex_data.get('num_ex')
                    lex.id_lex.set(lex_data.get('id_lex'))
                    lex.save()

                    print('near 1 3 14.... task')
                    task = Tasks.objects.get(exercise=ex)
                    task.num_task = 1
                    task.lex_right = lex_data.get('id_lex')[0]
                    task.save()

                    list_id_lex.append(lex.id)
                else:
                    print('in else 1 3 14... exercises')
                    ex = Exercises.objects.create(id_ex=m,
                                                  type=lex_data.get('type_ex'), lesson=les, num_ex=lex_data.get('num_ex'))
                    ex.save()

                    lex = LexDTO.objects.create(
                        id=ex.id_ex,
                        forlesson=forlessonsdto, type_ex=lex_data.get('type_ex'),
                        num_ex=lex_data.get('num_ex'))
                    lex.save()

                    for i in lex_data.get('id_lex'):
                        print(i)
                        a = LexDTO.objects.get(id=lex.id)
                        a.id_lex.add(i)
                    a.save()
                    print('near 1 3 14.... task')
                    task = Tasks.objects.create(exercise=ex, num_task=1, lex_right=lex_data.get('id_lex')[0])
                    task.save()

                    list_id_lex.append(lex.id)
        for lex_data in forlessonsdto.lex.all():
            if lex_data.id not in list_id_lex:
                if LexDTO.objects.filter(id=lex_data.id).exists():
                    ld = LexDTO.objects.get(id=lex_data.id)
                    ld.delete()
                    if Exercises.objects.filter(id_ex=lex_data.id).exists():
                        ex = Exercises.objects.get(id_ex=lex_data.id)
                        task = Tasks.objects.filter(exercise=ex)
                        for t in task:
                            v = Variants.objects.filter(task=t.id_task)
                            v.delete()
                        task.delete()
                        ex.delete()
                lex_data.delete()

        list_id_phr = []
        for phrase_data in phrases_data:
            print(phrase_data)
            if phrase_data.get('id', None):
                print('near phrasedto')
                ex = Exercises.objects.get(id_ex=phrase_data.get('id'))
                ex.type = phrase_data.get('type_ex')
                ex.lesson = les
                ex.num_ex = phrase_data.get('num_ex')
                ex.save()

                phrasedto = PhrasesDTO.objects.get(id=phrase_data.get('id'))
                phrasedto.forlesson = forlessonsdto
                phrasedto.type_ex = phrase_data.get('type_ex')
                phrasedto.num_ex = phrase_data.get('num_ex')
                phrasedto.id_rep.set(phrase_data.get('id_rep'))

                print(phrase_data.get('type_ex').type_ex)

                if (phrase_data.get('type_ex').type_ex == 19) or (phrase_data.get('type_ex').type_ex == 20):
                    phrasedto.id_miss = phrase_data.get('id_miss')
                    if phrase_data.get('type_ex').type_ex == 20:
                        phrasedto.id_var.set(phrase_data.get('id_var'))
                        print('near 20 task')
                        count = 0
                        flag = False
                        task_id_list = []
                        for i in phrase_data.get('id_miss'):
                            count = count + 1
                            print(i)
                            if not flag:
                                obj, created = Tasks.objects.get_or_create(exercise=ex, num_task=count,
                                                                           replic=phrase_data.get('id_rep')[0],
                                                                           num_lex=i)
                                task_id_list.append(obj.id_task)
                            else:
                                obj1, created1 = Tasks.objects.get_or_create(exercise=ex, num_task=count,
                                                                             replic=phrase_data.get('id_rep')[0],
                                                                             num_lex=i)
                                task_id_list.append(obj1.id_task)

                        ts = Tasks.objects.filter(exercise=ex)
                        for t in ts:
                            if t.id_task not in task_id_list:
                                t.delete()

                        print('near 20 variants')
                        var_id_list = []
                        for i in phrase_data.get('id_var'):
                            print(i)
                            obj2, created = Variants.objects.get_or_create(task=obj, lexeme=i)
                            var_id_list.append(obj2.id)

                        vs = Variants.objects.filter(task=obj)
                        for v in vs:
                            if v.id not in var_id_list:
                                v.delete()
                    else:
                        print('near ph task')
                        task = Tasks.objects.get(exercise=ex)
                        task.num_task = 1
                        task.replic = phrase_data.get('id_rep')[0]
                        task.num_lex = phrase_data.get('id_miss')[0]
                        task.save()
                    phrasedto.save()
                    list_id_phr.append(phrasedto.id)
                else:
                    print('near ph task')
                    task = Tasks.objects.get(exercise=ex)
                    task.num_task = 1
                    task.replic = phrase_data.get('id_rep')[0]
                    task.save()
                    list_id_phr.append(phrasedto.id)
            else:
                print('near phrasedto else')
                type_ex = phrase_data.get('type_ex')
                num_ex = phrase_data.get('num_ex')
                print('in ph exercises')
                m = max(Exercises.objects.order_by("id_ex").values_list("id_ex", flat=True).last() + 1,
                        RulesDTO.objects.order_by("id").values_list("id", flat=True).last() + 1)
                ex = Exercises.objects.create(
                    id_ex=m,
                    type=phrase_data.get('type_ex'), lesson=les,
                    num_ex=phrase_data.get('num_ex'))
                ex.save()
                phrasedto = PhrasesDTO.objects.create(forlesson=forlessonsdto, id=ex.id_ex, type_ex=type_ex, num_ex=num_ex)
                phrasedto.id_rep.set(phrase_data.get('id_rep'))

                print(phrase_data.get('type_ex').type_ex)

                if (phrase_data.get('type_ex').type_ex == 19) or (phrase_data.get('type_ex').type_ex == 20):
                    phrasedto.id_miss = phrase_data.get('id_miss')
                    if phrase_data.get('type_ex').type_ex == 20:
                        phrasedto.id_var.set(phrase_data.get('id_var'))
                        print('near 20 task')
                        count = 0
                        flag = False
                        for i in phrase_data.get('id_miss'):
                            count = count + 1
                            print(i)
                            if not flag:
                                task = Tasks.objects.create(exercise=ex, num_task=count,
                                                            replic=phrase_data.get('id_rep')[0], num_lex=i)
                                task.save()
                            else:
                                task1 = Tasks.objects.create(exercise=ex, num_task=count,
                                                             replic=phrase_data.get('id_rep')[0], num_lex=i)
                                task1.save()

                        print('near 20 variants')
                        for i in phrase_data.get('id_var'):
                            print(i)
                            variant = Variants.objects.create(task=task, lexeme=i)
                            variant.save()
                    else:
                        print('near ph task')
                        task = Tasks.objects.create(exercise=ex, num_task=1, replic=phrase_data.get('id_rep')[0],
                                                    num_lex=phrase_data.get('id_miss')[0])
                        task.save()
                    phrasedto.save()
                    list_id_phr.append(phrasedto.id)
                else:
                    print('near ph task')
                    task = Tasks.objects.create(exercise=ex, num_task=1, replic=phrase_data.get('id_rep')[0])
                    task.save()
                    list_id_phr.append(phrasedto.id)
        for phrase_data in forlessonsdto.phrases.all():
            if phrase_data.id not in list_id_phr:
                if PhrasesDTO.objects.filter(id=phrase_data.id).exists():
                    pd = PhrasesDTO.objects.get(id=phrase_data.id)
                    pd.delete()
                    if Exercises.objects.filter(id_ex=phrase_data.id).exists():
                        ex = Exercises.objects.get(id_ex=phrase_data.id)
                        task = Tasks.objects.filter(exercise=ex)
                        for t in task:
                            v = Variants.objects.filter(task=t.id_task)
                            v.delete()
                        task.delete()
                        ex.delete()
                phrase_data.delete()

        list_id_dia = []
        for dialog_data in dialogs_data:
            if dialog_data.get('id', None):
                print('in exercises')
                ex = Exercises.objects.get(id_ex=dialog_data.get('id'))
                ex.type = dialog_data.get('type_ex')
                ex.lesson = les
                ex.num_ex = dialog_data.get('num_ex')
                ex.save()

                print('near dialogdto')
                dialogdto = DialogDTO.objects.get(id=dialog_data.get('id'))
                dialogdto.forlesson = forlessonsdto
                dialogdto.type_ex = dialog_data.get('type_ex')
                dialogdto.num_ex = dialog_data.get('num_ex')
                dialogdto.id_rep = dialog_data.get('id_rep')
                dialogdto.save()

                print(dialog_data.get('type_ex').type_ex)

                if dialog_data.get('type_ex').type_ex == 21:

                    print('near 21 task')
                    print(dialog_data.get('id_rep')[0])
                    lexeme = Lexemes.objects.get(id_lex=dialog_data.get('id_rep')[0])
                    task = Tasks.objects.get(exercise=ex)
                    task.num_task = 1
                    task.lex_right = lexeme
                    task.save()
                    list_id_dia.append(dialogdto.id)
                else:
                    print('near 22 task')
                    dialogdto.id_miss = dialog_data.get('id_miss')
                    dialogdto.save()
                    count = 0
                    s = len(dialog_data.get('id_miss'))
                    t = 0
                    task_id_list = []
                    for i in dialog_data.get('id_rep'):
                        count = count + 1
                        print(i)
                        rep = Replicas.objects.get(id_rep=i)
                        if t < s:
                            obj, created = Tasks.objects.get_or_create(exercise=ex, num_task=count, replic=rep,
                                                               num_lex=dialog_data.get('id_miss')[t])
                            t = t + 1
                            task_id_list.append(obj.id_task)
                        else:
                            obj, created = Tasks.objects.get_or_create(exercise=ex, num_task=count, replic=rep)
                            task_id_list.append(obj.id_task)

                    ts = Tasks.objects.filter(exercise=ex)
                    for t in ts:
                        if t.id_task not in task_id_list:
                            t.delete()
                    list_id_dia.append(dialogdto.id)
            else:
                print('in exercises')
                m = max(Exercises.objects.order_by("id_ex").values_list("id_ex", flat=True).last() + 1,
                        RulesDTO.objects.order_by("id").values_list("id", flat=True).last() + 1)
                ex = Exercises.objects.create(id_ex=m, type=dialog_data.get('type_ex'), lesson=les,
                                              num_ex=dialog_data.get('num_ex'))
                ex.save()
                print('near dialogdto')
                dialogdto = DialogDTO.objects.create(forlesson=forlessonsdto, id=ex.id_ex,
                                                     type_ex=dialog_data.get('type_ex'), num_ex=dialog_data.get('num_ex'),
                                                     id_rep=dialog_data.get('id_rep'))
                dialogdto.save()

                print(dialog_data.get('type_ex').type_ex)

                if dialog_data.get('type_ex').type_ex == 21:
                    print('near 21 task')
                    print(dialog_data.get('id_rep')[0])
                    lexeme = Lexemes.objects.get(id_lex=dialog_data.get('id_rep')[0])
                    task = Tasks.objects.create(exercise=ex, num_task=1, lex_right=lexeme)
                    task.save()
                    list_id_dia.append(dialogdto.id)
                else:
                    print('near 22 task')
                    dialogdto.id_miss = dialog_data.get('id_miss')
                    dialogdto.save()
                    count = 0
                    s = len(dialog_data.get('id_miss'))
                    t = 0
                    for i in dialog_data.get('id_rep'):
                        count = count + 1
                        print(i)
                        rep = Replicas.objects.get(id_rep=i)
                        if t < s:
                            task = Tasks.objects.create(exercise=ex, num_task=count, replic=rep,
                                                        num_lex=dialog_data.get('id_miss')[t])
                            task.save()
                            t = t + 1
                        else:
                            task = Tasks.objects.create(exercise=ex, num_task=count, replic=rep)
                            task.save()
                    list_id_dia.append(dialogdto.id)

        for dialog_data in forlessonsdto.dialogs.all():
            if dialog_data.id not in list_id_dia:
                if DialogDTO.objects.filter(id=dialog_data.id).exists():
                    d = DialogDTO.objects.get(id=dialog_data.id)
                    d.delete()
                    if Exercises.objects.filter(id_ex=dialog_data.id).exists():
                        ex = Exercises.objects.get(id_ex=dialog_data.id)
                        task = Tasks.objects.filter(exercise=ex)
                        task.delete()
                        ex.delete()
                dialog_data.delete()
        return forlessonsdto


class LessonsWriteSerializer(serializers.ModelSerializer):
    # exercises_info = ExercisesWriteSerializer(many=True)
    # lessonblock = serializers.PrimaryKeyRelatedField(queryset=LessonBlocks.objects.all())
    # lessonblock = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    class Meta:
        model = Lessons
        fields = (
        'id_les', 'name_les', 'lessonblock', 'video', 'video_st', 'lex_st', 'phr_st', 'dialog_st', 'rules_st',)
        # 'exercises_info'
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
    lesson_info = LessonsWriteSerializer(many=True)

    class Meta:
        model = LessonBlocks
        fields = ["id_lb", 'lesson_info']

    def create(self, validated_data):
        lessons_info = validated_data.pop('lesson_info')
        lessonblock = LessonBlocks.objects.create(**validated_data)
        for lesson in lessons_info:
            les = Lessons.objects.create(**lesson, lessonblock=lessonblock)
            les.save()
        return lessonblock

    def update(self, instance, validated_data):
        lessons_data = validated_data.get('lesson_info')
        instance.save()

        for lesson_data in lessons_data:
            les_id = lesson_data.get('id_les', None)
            if les_id:
                lesson = Lessons.objects.get(id_les=les_id)
                lesson.name_les = lesson_data.get('name_les', lesson.name_les)
                lesson.lessonblock = lesson_data('lessonblock', instance.id_lb)
                lesson.video = lesson_data.get('video', lesson.video)
                lesson.video_st = lesson_data.get('video_st', lesson.video_st)
                lesson.lex_st = lesson_data.get('lex_st', lesson.lex_st)
                lesson.phr_st = lesson_data.get('phr_st', lesson.phr_st)
                lesson.dialog_st = lesson_data.get('dialog_st', lesson.dialog_st)
                lesson.rules_st = lesson_data.get('rules_st', lesson.rules_st)
                lesson.save()
            else:
                Lessons.objects.create(**lesson_data, lessonblock=instance)
        return instance


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
    # lexeme = serializers.ReadOnlyField(source='lexemes.id_lex')

    class Meta:
        model = RulesLexemes
        fields = ('id', 'rule', 'lexeme')


class MediaWriteSerializer(serializers.ModelSerializer):
    link_med = serializers.FileField(required=False)

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
    med_ik = serializers.FileField(required=False)

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


class ProgressWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ('id', 'id_ex', 'login', 'mean_pr', 'count_attempt')


class VowelSoundWriteSerializer(serializers.ModelSerializer):
    sound1 = serializers.FileField(required=False)
    sound2 = serializers.FileField(required=False)

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
        fields = ('name_les', 'id_ex', 'num_ex', 'id_r', 'id_task', 'picture', 'sound_rule', 'side', 'mean_lex', 'var_lex',
                  'var_transcr', 'var_sound', 'var_pic', 'mean_type_ex')


class ShowInfoAboutWordsLettersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowInfoAboutWordsLetters
        fields = ('name_les', 'id_ex', 'num_ex', 'id_task', 'num_task', 'mean_lex1', 'sound1', 'mean_lex2', 'transcr1',
                  'transcr2', 'sound2', 'stress', 'pic', 'mean_type_ex', 'variant', 'miss')


class ShowInfoAboutPhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowInfoAboutPhrase
        fields = ('name_les', 'id_ex', 'num_ex', 'id_task', 'num_task', 'replica', 'ik', 'pic_video', 'sound2', 'variant', 'miss',
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
