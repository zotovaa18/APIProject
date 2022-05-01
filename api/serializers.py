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


class VlWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = Vl
       fields = ['id', 'value', 'label', 'id_r']


class RulesDTOWriteSerializer(serializers.ModelSerializer):
    vl_var = VlWriteSerializer(many=True)
    id_var = serializers.PrimaryKeyRelatedField(many=True, queryset=Lexemes.objects.all())
    class Meta:
        model = RulesDTO
        fields = '__all__'

    # {
    #     "type": 23,
    #     "num_ex": 0,
    #     "id_lex": null,
    #     "id_var": [61, 62],
    #     "vl_var": [{
    #         "value": 61,
    #         "label": "к"
    #     },
    #         {
    #             "value": 62,
    #             "label": "э"
    #         }],
    #     "side": "лево",
    #     "sound_rule": "прол",
    #     "picture": "лдолд"
    # }

    def create(self, validated_data):
        vls_data = validated_data.pop('vl_var')
        print('near rulesdto')
        picture = validated_data.get('picture')
        sound_rule = validated_data.get('sound_rule')
        side = validated_data.get('side')
        type_ex = validated_data.get('type')
        num_ex = validated_data.get('num_ex')
        id_lex = validated_data.get('id_lex')
        rulesdto = RulesDTO.objects.create(type_ex=type_ex, num_ex=num_ex, id_lex=id_lex, side=side,
                                           sound_rule=sound_rule, picture=picture)
        rulesdto.id_var.set(validated_data.get('id_var'))
        rulesdto.save()
        print('near for')
        #print(vls_data)
        for vl_data in vls_data:
            v = Vl.objects.create(id_r=rulesdto, **vl_data)
            v.save()
            #rulesdto.vl_var.set(v.id)
        return rulesdto

class VlLexWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = VlLex
       fields = ['id', 'value', 'label', 'id_lexdto']


class VlMissWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = VlMiss
       fields = ['id', 'value', 'label', 'id_lexdto']


class VlVarWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = VlVar
       fields = ['id', 'value', 'label', 'id_lexdto']


class LexDTOWriteSerializer(serializers.ModelSerializer):
    id_lex = serializers.PrimaryKeyRelatedField(many=True, queryset=Lexemes.objects.all())
    #id_miss = serializers.PrimaryKeyRelatedField(many=True, queryset=Lexemes.objects.all(), allow_null=True, required=False)
    id_miss = serializers.ListField(child=serializers.IntegerField(), allow_null=True, required=False)
    id_variant = serializers.PrimaryKeyRelatedField(many=True, queryset=Lexemes.objects.all(), allow_null=True, required=False)
    vl_lex = VlLexWriteSerializer(many=True, allow_null=True, required=False)
    vl_miss = VlMissWriteSerializer(many=True, allow_null=True, required=False)
    vl_variant = VlVarWriteSerializer(many=True, allow_null=True, required=False)
    class Meta:
       model = LexDTO
       fields = ['id', 'type_ex', 'num_ex', 'id_lex', 'id_lex', 'vl_lex', 'id_miss', 'vl_miss', 'id_variant',
                 'vl_variant', 'forlesson']

    def create(self, validated_data):

        print('near lexdto')
        type_ex = validated_data.get('type_ex')
        num_ex = validated_data.get('num_ex')

        lexdto = LexDTO.objects.create(type_ex=type_ex, num_ex=num_ex)
        lexdto.id_lex.set(validated_data.get('id_lex'))

        lexdto.save()
        print(validated_data.get('type_ex').type_ex)
        if (validated_data.get('type_ex').type_ex == 2) or (validated_data.get('type_ex').type_ex == 7) or \
                (validated_data.get('type_ex').type_ex == 5) or (validated_data.get('type_ex').type_ex == 15) or \
                (validated_data.get('type_ex').type_ex == 6):
            if (validated_data.get('type_ex').type_ex == 2) or (validated_data.get('type_ex').type_ex == 7):

                vls_data = validated_data.pop('vl_lex')

                print('near vl_lex else')
                for vl_data in vls_data:
                    v = VlLex.objects.create(id_lexdto=lexdto, **vl_data)
                    v.save()

            elif validated_data.get('type_ex').type_ex == 6:
                lexdto.id_variant.set(validated_data.get('id_variant'))
                vls_data = validated_data.pop('vl_variant')
                print('near vl_variant else')
                for vl_data in vls_data:
                    v = VlVar.objects.create(id_lexdto=lexdto, **vl_data)
                    v.save()
            else:
                print(validated_data.get('id_miss')[0])
                lexdto.id_miss = validated_data.get('id_miss')

                vls_data = validated_data.pop('vl_miss')
                print('near vl_miss else')
                for vl_data in vls_data:
                    v = VlMiss.objects.create(id_lexdto=lexdto, **vl_data)
                    v.save()

                lexdto.id_variant.set(validated_data.get('id_variant'))
                vls_data = validated_data.pop('vl_variant')
                print('near vl_variant else')
                for vl_data in vls_data:
                    v = VlVar.objects.create(id_lexdto=lexdto, **vl_data)
                    v.save()
        return lexdto


class DialogDTOWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = DialogDTO
       fields = ['id', 'type_ex', 'num_ex', 'pic_video', 'forlesson']


class PhrasesDTOWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = PhrasesDTO
       fields = "__all__"
       depth = 5


class ForLessonsDTOWriteSerializer(serializers.ModelSerializer):
    lesson_info = LessonInfoDTOWriteSerializer()
    rules = RulesDTOWriteSerializer(many=True)
    dialogs = DialogDTOWriteSerializer(many=True)
    lex = LexDTOWriteSerializer(many=True)
    # phrase_dto = PhrasesDTOWriteSerializer(many=True)

    # {
    #     "name_les": "Тест 30.04_1",
    #     "lessonblock": 1,
    #     "video": null,
    #     "lesson_info": {
    #         "video_st": "Пусто     ",
    #         "lex_st": "В процессе",
    #         "phr_st": "В процессе",
    #         "dialog_st": "В процессе",
    #         "rules_st": "В процессе"
    #     },
    #     "rules": [
    #         {
    #             "id": 0,
    #             "type_ex": 23,
    #             "num_ex": 0,
    #             "id_var": [
    #                 61,
    #                 62,
    #                 63
    #             ],
    #             "vl_var": [
    #                 {
    #                     "value": 61,
    #                     "label": "к"
    #                 },
    #                 {
    #                     "value": 62,
    #                     "label": "э"
    #                 },
    #                 {
    #                     "value": 63,
    #                     "label": "т"
    #                 }
    #             ],
    #             "side": "право",
    #             "sound_rule": "ссылка",
    #             "picture": "ссылка"
    #         },
    #         {
    #             "id": 1,
    #             "type_ex": 17,
    #             "num_ex": 1,
    #             "id_lex": 74,
    #             "id_var": [
    #                 61,
    #                 62,
    #                 63
    #             ],
    #             "vl_var": [
    #                 {
    #                     "value": 61,
    #                     "label": "к"
    #                 },
    #                 {
    #                     "value": 62,
    #                     "label": "э"
    #                 },
    #                 {
    #                     "value": 63,
    #                     "label": "т"
    #                 }
    #             ],
    #             "sound_rule": "ссылка",
    #             "picture": "ссылка"
    #         }
    #     ],
    #     "lex": [
    #         {
    #             "type_ex": 14,
    #             "num_ex": 2,
    #             "id_lex": [62]
    #         },
    #         {
    #             "type_ex": 3,
    #             "num_ex": 3,
    #             "id_lex": [61]
    #         },
    #         {
    #             "type_ex": 2,
    #             "num_ex": 4,
    #             "id_lex": [
    #                 72,
    #                 71
    #             ],
    #             "vl_lex": [
    #                 {
    #                     "value": 72,
    #                     "label": "эм"
    #                 },
    #                 {
    #                     "value": 71,
    #                     "label": "мэ"
    #                 }
    #             ]
    #         },
    #         {
    #             "type_ex": 1,
    #             "num_ex": 5,
    #             "id_lex": [74]
    #         },
    #         {
    #             "type_ex": 18,
    #             "num_ex": 6,
    #             "id_lex": [74]
    #         },
    #         {
    #             "id": 6,
    #             "type_ex": 5,
    #             "num_ex": 7,
    #             "id_lex": [74],
    #             "id_miss": [
    #                 2
    #             ],
    #             "vl_miss": [
    #                 {
    #                     "value": 2,
    #                     "label": "2"
    #                 }
    #             ],
    #             "id_variant": [
    #                 61,
    #                 62,
    #                 63
    #             ],
    #             "vl_variant": [
    #                 {
    #                     "value": 61,
    #                     "label": "к"
    #                 },
    #                 {
    #                     "value": 62,
    #                     "label": "э"
    #                 },
    #                 {
    #                     "value": 63,
    #                     "label": "т"
    #                 }
    #             ]
    #         },
    #         {
    #             "id": 7,
    #             "type_ex": 15,
    #             "num_ex": 8,
    #             "id_lex": [74],
    #             "id_miss": [
    #                 1,
    #                 2,
    #                 3
    #             ],
    #             "vl_miss": [
    #                 {
    #                     "value": 1,
    #                     "label": "1"
    #                 },
    #                 {
    #                     "value": 2,
    #                     "label": "2"
    #                 },
    #                 {
    #                     "value": 3,
    #                     "label": "3"
    #                 }
    #             ],
    #             "id_variant": [
    #                 61,
    #                 62,
    #                 63,
    #                 70
    #             ],
    #             "vl_variant": [
    #                 {
    #                     "value": 61,
    #                     "label": "к"
    #                 },
    #                 {
    #                     "value": 62,
    #                     "label": "э"
    #                 },
    #                 {
    #                     "value": 63,
    #                     "label": "т"
    #                 },
    #                 {
    #                     "value": 70,
    #                     "label": "м"
    #                 }
    #             ]
    #         },
    #         {
    #             "type_ex": 7,
    #             "num_ex": 9,
    #             "id_lex": [
    #                 72,
    #                 71,
    #                 76,
    #                 77
    #             ],
    #             "vl_lex": [
    #                 {
    #                     "value": 72,
    #                     "label": "эм"
    #                 },
    #                 {
    #                     "value": 71,
    #                     "label": "мэ"
    #                 },
    #                 {
    #                     "value": 76,
    #                     "label": "ма"
    #                 },
    #                 {
    #                     "value": 77,
    #                     "label": "ам"
    #                 }
    #             ]
    #         }
    #     ],
    #     "dialogs": [
    #         {
    #             "type_ex": 21,
    #             "num_ex": 10,
    #             "pic_video": "ссылка"
    #         }
    #     ],
    #     "description": ""
    # }
    class Meta:
        model = ForLessonsDTO
        fields = ['id', 'name_les', 'lessonblock', 'video', 'lesson_info', 'rules', 'lex', 'dialogs', 'description']

    def create(self, validated_data):
        lessons_info_data = validated_data.pop('lesson_info')
        rules_data = validated_data.pop('rules')
        dialogs_data = validated_data.pop('dialogs')
        lexs_data = validated_data.pop('lex')
        print(Lessons.objects.order_by("id_les").values_list("id_les", flat=True).last()+1)
        forlessonsdto = ForLessonsDTO.objects.create(id=Lessons.objects.order_by("id_les").values_list("id_les", flat=True).last()+1,
                                                     **validated_data)
        # for lesson_info_data in lessons_info_data:

        print('near les')
        print(forlessonsdto.id)
        les = Lessons.objects.create(id_les=forlessonsdto.id,
                                     name_les=forlessonsdto.name_les, lessonblock=forlessonsdto.lessonblock,
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
                r = RulesDTO.objects.create(id=RulesDTO.objects.order_by("id").values_list("id", flat=True).last()+1,
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

                vls_data = rule_data.pop('vl_var')

                print('near vl_data if')
                for vl_data in vls_data:
                    v = Vl.objects.create(id_r=r, **vl_data)
                    v.save()

            else:
                print('in else')
                ex = Exercises.objects.create(type=rule_data.get('type_ex'), lesson=les, num_ex=rule_data.get('num_ex'))
                ex.save()
                print('near task')
                task = Tasks.objects.create(exercise=ex, num_task=1, lex_right=rule_data.get('id_lex'),
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
                r = RulesDTO.objects.create(id=RulesDTO.objects.order_by("id").values_list("id", flat=True).last()+1,
                                            forlesson=forlessonsdto, type_ex=rule_data.get('type_ex'),
                                        num_ex=rule_data.get('num_ex'), id_lex=rule_data.get('id_lex'),
                                        picture=rule_data.get('picture'), side=rule_data.get('side'),
                                        sound_rule=rule_data.get('sound_rule'))
                r.save()


                # if RulesDTO.objects.order_by("id").values_list("id", flat=True).last() in list_id:
                #     a = RulesDTO.objects.get(id=id_rd)
                #     a.id.set(Rules.objects.last() + 1)
                #     a.save()

                for i in rule_data.get('id_var'):
                    print(i)
                    a = RulesDTO.objects.get(id=r.id)
                    a.id_var.add(i)
                a.save()

                vls_data = rule_data.pop('vl_var')

                print('near vl_data else')
                # print(vls_data)
                for vl_data in vls_data:
                    v = Vl.objects.create(id_r=r, **vl_data)
                    v.save()

        for lex_data in lexs_data:

            lex = LexDTO.objects.create(id=LexDTO.objects.order_by("id").values_list("id", flat=True).last()+1,
                                        forlesson=forlessonsdto, type_ex=lex_data.get('type_ex'),
                                        num_ex=lex_data.get('num_ex'))
            lex.save()

            for i in lex_data.get('id_lex'):
                print(i)
                a = LexDTO.objects.get(id=lex.id)
                a.id_lex.add(i)
            a.save()
            if (lex_data.get('type_ex').type_ex == 2) or (lex_data.get('type_ex').type_ex == 7) or \
                    (lex_data.get('type_ex').type_ex == 5) or (lex_data.get('type_ex').type_ex == 15) or \
                    (lex_data.get('type_ex').type_ex == 6):
                if (lex_data.get('type_ex').type_ex == 2) or (lex_data.get('type_ex').type_ex == 7):
                    vls_data = lex_data.pop('vl_lex')

                    print('near vl_lex else')
                    for vl_data in vls_data:
                        v = VlLex.objects.create(id_lexdto=lex, **vl_data)
                        v.save()
                    print('in if 2 7 exercises')
                    ex = Exercises.objects.create(type=lex_data.get('type_ex'), lesson=les,
                                                  num_ex=lex_data.get('num_ex'))
                    ex.save()

                    print('near if 2 7  task')
                    count = 0
                    for i in lex_data.get('id_lex'):
                        count = count + 1
                        print(i)
                        print('near task')
                        task = Tasks.objects.create(exercise=ex, num_task=count, lex_right=i)
                        task.save()

                elif lex_data.get('type_ex').type_ex == 6:
                    for i in lex_data.get('id_variant'):
                        print(i)
                        a = LexDTO.objects.get(id=lex.id)
                        a.id_variant.add(i)
                    a.save()

                    vls_data = lex_data.pop('vl_variant')
                    print('near vl_variant else')
                    for vl_data in vls_data:
                        v = VlVar.objects.create(id_lexdto=lex, **vl_data)
                        v.save()

                    print('in elif 6 exercises')
                    ex = Exercises.objects.create(type=rule_data.get('type_ex'), lesson=les,
                                                  num_ex=lex_data.get('num_ex'))
                    ex.save()
                    print('near elif 6 task')
                    task = Tasks.objects.create(exercise=ex, num_task=1, lex_right=rule_data.get('id_lex')[0])
                    task.save()

                    for i in lex_data.get('id_variant'):
                        print(i)
                        variant = Variants.objects.create(task=task, lexeme=i)
                        variant.save()

                else:
                    lex.id_miss = lex_data.get('id_miss')

                    # for i in lex_data.get('id_miss'):
                    #     print(i)
                    #     a = LexDTO.objects.get(id=lex.id)
                    #     a.id_miss.add(i)
                    # a.save()

                    vls_data = lex_data.pop('vl_miss')
                    print('near vl_miss else')
                    for vl_data in vls_data:
                        v = VlMiss.objects.create(id_lexdto=lex, **vl_data)
                        v.save()

                    for i in lex_data.get('id_variant'):
                        print(i)
                        a = LexDTO.objects.get(id=lex.id)
                        a.id_variant.add(i)
                    a.save()

                    vls_data = lex_data.pop('vl_variant')
                    print('near vl_variant else')
                    for vl_data in vls_data:
                        v = VlVar.objects.create(id_lexdto=lex, **vl_data)
                        v.save()

                    if lex_data.get('type_ex').type_ex == 5:
                        print('in if 5 exercises')
                        ex = Exercises.objects.create(type=lex_data.get('type_ex'), lesson=les,
                                                      num_ex=lex_data.get('num_ex'))
                        ex.save()
                        print('near 5 task')

                        task = Tasks.objects.create(exercise=ex, num_task=1, lex_right=lex_data.get('id_lex')[0],
                                                    num_lex=lex_data.get('id_miss')[0])
                        task.save()

                        print('near 5 variants')
                        for i in lex_data.get('id_variant'):
                            print(i)
                            variant = Variants.objects.create(task=task, lexeme=i)
                            variant.save()
                    else:
                        print('in 15 exercises')
                        ex = Exercises.objects.create(type=lex_data.get('type_ex'), lesson=les,
                                                      num_ex=lex_data.get('num_ex'))
                        ex.save()

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
                        for i in lex_data.get('id_variant'):
                            print(i)
                            variant = Variants.objects.create(task=task, lexeme=i)
                            variant.save()
            else:
                print('in else 1 3 14... exercises')
                ex = Exercises.objects.create(type=lex_data.get('type_ex'), lesson=les, num_ex=lex_data.get('num_ex'))
                ex.save()
                print('near 1 3 14.... task')
                task = Tasks.objects.create(exercise=ex, num_task=1, lex_right=lex_data.get('id_lex')[0])
                task.save()

        for dialog_data in dialogs_data:

            DialogDTO.objects.create(forlesson=forlessonsdto, id=les.id_les, **dialog_data)
        return forlessonsdto


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
    lesson_info = LessonsWriteSerializer(many=True)
    class Meta:
        model = LessonBlocks
        fields = ["id_lb", 'lesson_info']

    # #"lesson_info"
    def create(self, validated_data):
        lessons_info = validated_data.pop('lesson_info')
        lessonblock = LessonBlocks.objects.create(**validated_data)
        for lesson in lessons_info:
            les = Lessons.objects.create(**lesson, lessonblock=lessonblock)
            les.save()
        return lessonblock

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


class ProgressWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = Progress
       fields = ('id', 'id_ex', 'login', 'mean_pr', 'count_attempt')


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
