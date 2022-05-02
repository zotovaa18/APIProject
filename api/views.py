#from django.shortcuts import render, HttpResponse
from .models import *
from .serializers import *
'''from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view'''
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.schemas import AutoSchema
from rest_framework import viewsets
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action


class WeakPointsList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       дто для экранов со слабыми уроками для пользователей
       Писать /?login=, если нужен доступ к конкретному пользователю
    """
    queryset = WeakPoints.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        return WeakPointsSerializer

    @swagger_auto_schema(operation_summary='получить статистику')
    def get(self, request, *args, **kwargs):
        login = request.GET.get("login")
        if login is not None:
            show_info = WeakPoints.objects.filter(login=login)
            serializer = WeakPointsSerializer(show_info, many=True)
            return Response(serializer.data)
        else:
            return self.list(request, *args, **kwargs)


class WeaksList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       дто для экранов со слабыми уроками для пользователей
       Писать /?login=, если нужен доступ к конкретному пользователю
    """
    queryset = Weaks.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        return WeaksSerializer

    @swagger_auto_schema(operation_summary='получить статистику')
    def get(self, request, *args, **kwargs):
        login = request.GET.get("login")
        if login is not None:
            show_info = Weaks.objects.filter(login=login)
            serializer = WeaksSerializer(show_info, many=True)
            return Response(serializer.data)
        else:
            return self.list(request, *args, **kwargs)


class NumberOfWeakPointsList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       дто для экранов со слабыми уроками для пользователей
       Писать /?login=, если нужен доступ к конкретному пользователю
    """
    queryset = NumberOfWeakPoints.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        return NumberOfWeakPointsSerializer

    @swagger_auto_schema(operation_summary='получить статистику')
    def get(self, request, *args, **kwargs):
        login = request.GET.get("login")
        if login is not None:
            show_info = NumberOfWeakPoints.objects.filter(login=login)
            serializer = NumberOfWeakPointsSerializer(show_info, many=True)
            return Response(serializer.data)
        else:
            return self.list(request, *args, **kwargs)


# class WeakPointsList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = WeakPoints.objects.all()
#     serializer_class = WeakPointsSerializer
#
#     def get(self, request):
#         return self.list(request)
#
#
# class WeakPointsDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
#                         mixins.DestroyModelMixin):
#     queryset = WeakPoints.objects.all()
#     serializer_class = WeakPointsSerializer
#
#     def get(self, request, pk):
#         return self.retrieve(request, pk=pk)


class DialogDTOList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    queryset = DialogDTO.objects.all()

    serializer_class = DialogDTOWriteSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class PhrasesDTOList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    queryset = PhrasesDTO.objects.all()

    serializer_class = PhrasesDTOWriteSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class RatingList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get(self, request):
        return self.list(request)

    # def post(self, request):
    #     return self.create(request)


class LexDTOList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    queryset = LexDTO.objects.all()

    serializer_class = LexDTOWriteSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class RulesDTOList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = RulesDTO.objects.all()
    serializer_class = RulesDTOWriteSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class LessonInfoList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = LessonInfoDTO.objects.all()
    serializer_class = LessonInfoDTOWriteSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ForLessonsList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = ForLessonsDTO.objects.all()
    serializer_class = ForLessonsDTOWriteSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class TimeSpentList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = TimeSpent.objects.all()
    serializer_class = TimeSpentSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class TimeSpentDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin):

    queryset = TimeSpent.objects.all()
    serializer_class = TimeSpentSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class ProgressBlocksList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       дто для экранов с местом остановки пользователей
       Писать, например ?login=103333743383425053665,
       если нужен доступ к конкретному пользователю в конкретном уроке и разделе
    """

    queryset = ProgressBlocks.objects.all()

    @swagger_auto_schema(operation_summary='получить порядковый номер остановки')
    def get_serializer_class(self):
        method = self.request.method
        return ProgressBlocksSerializer

    def get(self, request, *args, **kwargs):
        login = request.GET.get("login")
        if login is not None:
            show_info = ProgressBlocks.objects.filter(login=login)
            serializer = ProgressBlocksSerializer(show_info, many=True)
            return Response(serializer.data)
        else:
            return self.list(request, *args, **kwargs)


class NumStopList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       дто для экранов с местом остановки пользователей
       Писать, например ?block=wordsletters&login=103333743383425053665,
       если нужен доступ к конкретному пользователю в конкретном разделе
       Писать, например ?login=103333743383425053665,
       если нужен доступ к конкретному пользователю

    """

    queryset = NumStop.objects.all()

    @swagger_auto_schema(operation_summary='получить порядковый номер остановки')
    def get_serializer_class(self):
        method = self.request.method
        return NumStopSerializer

    def get(self, request, *args, **kwargs):
        login = request.GET.get("login")
        block = request.GET.get("block")
        if (login is not None) and (block is not None):
            show_info = NumStop.objects.filter(block=block, login=login)
            serializer = NumStopSerializer(show_info, many=True)
            return Response(serializer.data)
        elif (login is None) and (block is not None):
            show_info = NumStop.objects.filter(block=block)
            serializer = NumStopSerializer(show_info, many=True)
            return Response(serializer.data)
        elif(login is not None) and (block is not None):
            show_info = NumStop.objects.filter(block=block, login=login)
            serializer = NumStopSerializer(show_info, many=True)
            return Response(serializer.data)
        else:
            return self.list(request, *args, **kwargs)


class CountryList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    """
     get:
       возвращает список стран
     post:
       добавляет данные о новой страны
    """
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer

    @swagger_auto_schema(operation_summary='получить список всех стран')
    def get(self, request):
        return self.list(request)

    @swagger_auto_schema(operation_summary='добавить новую страну')
    def post(self, request):
        return self.create(request)


class CountryDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретном стране
     put:
       изменяет данные о конкретном стране
     delete:
       удаляет данные о конкретной стране
    """
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретной стране по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретной стране')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретной стране')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class PeopleGroupsList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает список групп пользователей: пользователи (обычные люди), администраторы
     post:
       добавляет новую группу пользователей
    """
    queryset = PeopleGroups.objects.all()
    serializer_class = PeopleGroupsSerializer

    @swagger_auto_schema(operation_summary='получить список групп пользователей')
    def get(self, request):
        return self.list(request)

    @swagger_auto_schema(operation_summary='добавить новую группу пользователей')
    def post(self, request):
        return self.create(request)


class PeopleGroupsDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретной группе пользователей
     put:
       изменяет данные о конкретной группе пользователей
     delete:
       удаляет данные о конкретном группе пользователей
    """
    queryset = PeopleGroups.objects.all()
    serializer_class = PeopleGroupsSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретной группе пользователей по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретной группе пользователей')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретном группе пользователей')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class StatusList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает список всех статусов для частей урока (пустой, в процессе, готово). Для лингвистов.
     post:
       добавляет новый статус. Это нужно для лингвистов.
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    @swagger_auto_schema(operation_summary='получить список статусов')
    def get(self, request):
        return self.list(request)

    @swagger_auto_schema(operation_summary='добавить новый статус')
    def post(self, request):
        return self.create(request)


class StatusDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """
     get:
       возвращает конкретный статус
     put:
       изменяет данные о конкретном статусе
     delete:
       удаляет данные о конкретном статусе
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    @swagger_auto_schema(operation_summary='получить конкретный статус по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретном статусе')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретном статусе')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class PeopleList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает список пользователей приложения и веба.
     post:
       добавляет нового пользователя. password_admin заполняется, если администратор.
    """
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    @swagger_auto_schema(operation_summary='получить список пользователей')
    def get(self, request):
        return self.list(request)

    @swagger_auto_schema(operation_summary='добавить нового пользователя')
    def post(self, request):
        return self.create(request)


class PeopleDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретном пользователе
     put:
       изменяет данные о конкретном пользователе
     delete:
       удаляет данные о конкретном пользователе
    """
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретном пользователе по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретном пользователе')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретном пользователе')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class TypesLexList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает список типов лексем (буква, слово и тд)
     post:
       добавляет новый тип лексем
    """
    queryset = TypesLex.objects.all()
    serializer_class = TypesLexSerializer

    @swagger_auto_schema(operation_summary='получить список типов лексем')
    def get(self, request):
        return self.list(request)

    @swagger_auto_schema(operation_summary='добавить новый тип лексем')
    def post(self, request):
        return self.create(request)


class TypesLexDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретном типе лексем
     put:
       изменяет данные о конкретном типе лексем
     delete:
       удаляет данные о конкретном типе лексем
    """
    queryset = TypesLex.objects.all()
    serializer_class = TypesLexSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретном типе лексем по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретном типе лексем')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретном типе лексем')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class TypesMedList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает список типов медиа (картинка, видео, звук и тд)
     post:
       добавляет новый тип медиа
    """
    queryset = TypesMed.objects.all()
    serializer_class = TypesMedSerializer

    @swagger_auto_schema(operation_summary='получить список типов медиа')
    def get(self, request):
        return self.list(request)

    @swagger_auto_schema(operation_summary='добавить новый тип медиа')
    def post(self, request):
        return self.create(request)


class TypesMedDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретном типе медиа
     put:
       изменяет данные о конкретном типе медиа
     delete:
       удаляет данные о конкретном типе медиа
    """
    queryset = TypesMed.objects.all()
    serializer_class = TypesMedSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретном типе медиа по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретном типе медиа')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретном типе медиа')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)

class LessonBlocksViewSet(viewsets.ModelViewSet):
    serializer_class = LessonsWriteSerializer
    queryset = LessonBlocks.objects.all()



class LessonBlocksList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает список блоков уроков
     post:
       добавляет новый блок уроков
    """
    queryset = LessonBlocks.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return LessonBlocksWriteSerializer
        else:
            return LessonBlocksReadSerializer

    @swagger_auto_schema(operation_summary='получить список блоков уроков')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='добавить новый блок уроков')
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LessonBlocksDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретном блоке уроков
     put:
       изменяет данные о конкретном блоке уроков
     delete:
       удаляет данные о конкретном блоке уроков
    """
    queryset = LessonBlocks.objects.all()
    serializer_class = LessonBlocksWriteSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретном блоке уроков по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретном блоке уроков')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретном блоке уроков')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)

    # @action(detail=True, methods=["PUT"])
    # def lessons(self, request, pk=None):
    #     lessonblock = self.get_object()
    #     lessons = Lessons.objects.filter(lessonblock=lessonblock)
    #     serializer = LexemesWriteSerializer(lessons, many=True)
    #     return Response(serializer.data)

class LessonsList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает список уроков
     post:
       добавляет новый урок. Можно добавить видео для урока и указать статусы готовности блоков и id этих частей
    """
    queryset = Lessons.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return LessonsWriteSerializer
        else:
            return LessonsReadSerializer

    @swagger_auto_schema(operation_summary='получить список уроков')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='добавить новый урок')
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LessonsDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретном уроке
     put:
       изменяет данные о конкретном уроке
     delete:
       удаляет данные о конкретном уроке
    """
    queryset = Lessons.objects.all()
    serializer_class = LessonsWriteSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретном уроке по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретном уроке')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретном уроке')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)

    # @action(detail=True, methods=["GET"])
    # def exercises(self, request, pk=None):
    #     lesson = self.get_object()
    #     exercises = Exercises.objects.filter(lesson=lesson)
    #     serializer = LexemesWriteSerializer(exercises, many=True)
    #     return Response(serializer.data)


class LexemesViewsets(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает список лексем. Поля transcr, stress заполняются только для слов. Слова состоят из слогов и букв, слога и букв, фразы из слов
     post:
       добавляет новую лексему
    """
    queryset = Lexemes.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return LexemesWriteSerializer
        else:
            return LexemesReadSerializer

    @swagger_auto_schema(operation_summary='получить список лексем')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='добавить новую лексему')
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LexemesDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретной лексеме
     put:
       изменяет данные о конкретной лексеме
     delete:
       удаляет данные о конкретной лексеме
    """
    queryset = Lexemes.objects.all()
    serializer_class = LexemesWriteSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретной лексеме по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретной лексеме')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретной лексеме')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class VowelSoundList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает список звуков гласных. Например, буква о имеет звук о или а
     post:
       добавляет новый звук гласной
    """
    queryset = VowelSound.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return VowelSoundWriteSerializer
        else:
            return VowelSoundReadSerializer

    @swagger_auto_schema(operation_summary='получить список звуков гласных')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='добавить новый звук гласной')
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VowelSoundDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретном звуке гласной
     put:
       изменяет данные о конкретном звуке гласной
     delete:
       удаляет данные о конкретном звуке гласной
    """
    queryset = VowelSound.objects.all()
    serializer_class = VowelSoundWriteSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретном звуке гласной по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретном звуке гласной')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретном звуке гласной')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class MediaList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает список медиа
     post:
       добавляет новое медиа. Можно добавить медиа без лексемы
    """
    queryset = Medias.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return MediaWriteSerializer
        else:
            return MediaReadSerializer

    @swagger_auto_schema(operation_summary='получить список медиа')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='добавить новое медиа')
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MediaDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретном медиа
     put:
       изменяет данные о конкретном медиа
     delete:
       удаляет данные о конкретном медиа
    """
    queryset = Medias.objects.all()
    serializer_class = MediaWriteSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретном медиа по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретном медиа')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретном медиа')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class IkList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает список интонационных конструкций (ИК-1, ИК-2 и тд)
     post:
       добавляют новую интонационную конструкцию
    """
    queryset = Ik.objects.all()
    serializer_class = IkSerializer

    @swagger_auto_schema(operation_summary='получить список интонационных конструкций')
    def get(self, request):
        return self.list(request)

    @swagger_auto_schema(operation_summary='добавить новую интонационную конструкцию')
    def post(self, request):
        return self.create(request)


class IkDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретной интонационной конструкции
     put:
       изменяет данные о конкретной интонационной конструкции
     delete:
       удаляет данные о конкретной интонационной конструкции
    """
    queryset = Ik.objects.all()
    serializer_class = IkSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретной интонационной конструкции по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретной интонационной конструкции')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретной интонационной конструкции')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class ReplicasList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает список реплик. Указывается промежуток времени из видео, где говорится фраза с конкретной интонацией.
       symbol - знак, который пишется в конце фразы
     post:
       добавляет новую реплику. Указывается промежуток времени из видео, где говорится фраза с конкретной интонацией.
       symbol - знак, который пишется в конце фразы
    """
    queryset = Replicas.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return ReplicasWriteSerializer
        else:
            return ReplicasReadSerializer

    @swagger_auto_schema(operation_summary='получить список реплик')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='добавить новую реплику')
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ReplicasDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретной реплике
     put:
       изменяет данные о конкретной реплике
     delete:
       удаляет данные о конкретной реплике
    """
    queryset = Replicas.objects.all()
    serializer_class = ReplicasWriteSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретной реплике по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретной реплике')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретной реплике')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class LecFillingList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает список составляющих лексем (слова - буквы, фразы - слова и тд). Отношение M:N
     post:
       добавляет новую составляющую лексем (слова - буквы, фразы - слова и тд). Отношение M:N
    """
    queryset = LecFilling.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return LecFillingWriteSerializer
        else:
            return LecFillingReadSerializer

    @swagger_auto_schema(operation_summary='получить список составляющих лексем')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='добавить новое составляющее лексемы')
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LecFillingDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о составляющей лексемы
     put:
       изменяет данные о составляющей лексемы
     delete:
       удаляет данные о составляющей лексемы
    """
    queryset = LecFilling.objects.all()
    serializer_class = LecFillingWriteSerializer

    @swagger_auto_schema(operation_summary='получить данные о составляющей лексемы по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о составляющей лексемы')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о составляющей лексемы')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class RulesList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает список правил
     post:
       добавляет новое правило. Side - сторона экрана, где должно располагаться правило
    """
    queryset = Rules.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return RulesSerializer
        else:
            return RulesReadSerializer

    @swagger_auto_schema(operation_summary='получить список правил')
    def get(self, request, *args, **kwargs):
        id_v = request.GET.get("id_v")
        if id_v is not None:
            cer_video = RulesLexemes.objects.filter(id_v=id_v)
            serializer = RulesLexemesSerializer(cer_video, many=True)
            return Response(serializer.data)
        else:
            return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='добавить новое правило')
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     data = request.data
    #
    #     new_rules = Rules.objects.create(picture=data["picture"])
    #
    #     new_rules.save()
    #
    #     for lexeme in data["id_lex"]:
    #         lexeme_obj = Lexemes.objects.get(id_lex=lexeme["id_lex"])
    #         new_rules.id_lex.add(lexeme_obj)
    #
    #     serializer = RulesSerializer(new_rules)
    #
    #     return Response(serializer.data)


class RulesDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретном правиле
     put:
       изменяет данные о конкретном правиле
     delete:
       удаляет данные о конкретном правиле
    """
    queryset = Rules.objects.all()
    serializer_class = RulesSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретном правиле по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретном правиле')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретном правиле')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class RulesLexemesList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает список лексем, которые задействованы в правиле
     post:
       добавляет связь лексема-правило (M:N), которые задействованы
    """
    queryset = RulesLexemes.objects.all()
    serializer_class = RulesLexemesSerializer

    @swagger_auto_schema(operation_summary='получить список лексем из правил')
    def get(self, request):
        return self.list(request)

    @swagger_auto_schema(operation_summary='добавить новую лексему для правила')
    def post(self, request):
        return self.create(request)


class RulesLexemesDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретных лексем из правила
     put:
       изменяет данные о конкретных лексем из правила
     delete:
       удаляет данные о конкретных лексем из правила
    """
    queryset = RulesLexemes.objects.all()
    serializer_class = RulesLexemesSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретных лексем из правила по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретных лексем и их правил')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить конкретные лексемы для конкретных правил')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class TypesExList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    """
     get:
       возвращает список всех типов упражнений
     post:
       добавляет новый тип упражнений
    """
    queryset = TypesEx.objects.all()
    serializer_class = TypesExSerializer

    @swagger_auto_schema(operation_summary='получить список типов упражнений')
    def get(self, request):
        return self.list(request)

    @swagger_auto_schema(operation_summary='добавить новый тип упражнений')
    def post(self, request):
        return self.create(request)


class TypesExDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретном типе упражнений
     put:
       изменяет данные о конкретном типе упражнений
     delete:
       удаляет данные о конкретном типе упражнений
    """
    queryset = TypesEx.objects.all()
    serializer_class = TypesExSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретном типе упражнений по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретном типе упражнений')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретном типе упражнений')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class ExercisesList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает список всех упражнений
     post:
       добавляет номер упражнения. num_ex - номер упражнения в уроке.
    """
    queryset = Exercises.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return ExercisesWriteSerializer
        else:
            return ExercisesReadSerializer

    @swagger_auto_schema(operation_summary='получить список упражнений')
    def get(self, request):
        return self.list(request)

    @swagger_auto_schema(operation_summary='добавить новое упражнение')
    def post(self, request):
        return self.create(request)


class ExercisesDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретном упражнении
     put:
       изменяет данные о конкретном упражнении
     delete:
       удаляет данные о конкретном упражнении
    """
    queryset = Exercises.objects.all()
    serializer_class = ExercisesWriteSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретном упражнении по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретном упражнении')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретном упражнении')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class ProgressList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает прогресс всех пользователей
     post:
       добавляет прогресс для пользователя
    """

    queryset = Progress.objects.all()

    serializer_class = ProgressWriteSerializer

    @swagger_auto_schema(operation_summary='получить список прогресса')
    def get(self, request):
        return self.list(request)

    @swagger_auto_schema(operation_summary='добавить новый прогресс')
    def post(self, request):
        return self.create(request)

    def delete(self, request):
        return self.destroy(request)


class ProgressDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретном прогрессе
     put:
       изменяет данные о конкретном прогрессе
     delete:
       удаляет данные о конкретном прогрессе
    """
    queryset = Progress.objects.all()
    serializer_class = ProgressWriteSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретном прогрессе по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретном прогрессе')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретном прогрессе')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class TasksList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает список заданий
     post:
       добавляет новое задание.
       num_lex - номера пропущенных.
       count_miss - рандомно убрать столько лексем.
       picture - ссылка на картинку или видео для задания.
       sound - звук фразы
       pronunciation - микрофон для фраз
    """
    queryset = Tasks.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return TasksWriteSerializer
        else:
            return TasksReadSerializer

    @swagger_auto_schema(operation_summary='получить список заданий для упражнений')
    def get(self, request):
        return self.list(request)

    @swagger_auto_schema(operation_summary='добавить новое задание для упражнений')
    def post(self, request):
        return self.create(request)


class TasksDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретном задании
     put:
       изменяет данные о конкретном задании
     delete:
       удаляет данные о конкретном задании
    """
    queryset = Tasks.objects.all()
    serializer_class = TasksWriteSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретном задании по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить конкретное задание')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретном задании')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class VariantsList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает список всех вариантов для каждого ответа.
     post:
       добавляет новый вариант. Если это работа с фразами, то добавлять только неправильные ответы.
    """
    queryset = Variants.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return VariantsWriteSerializer
        else:
            return VariantsReadSerializer

    @swagger_auto_schema(operation_summary='получить список вариантов для упражнений')
    def get(self, request):
        return self.list(request)

    @swagger_auto_schema(operation_summary='добавить новый вариант для упражнений')
    def post(self, request):
        return self.create(request)


class VariantsDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретном варианте для упражнения
     put:
       изменяет данные о конкретном варианте для упражнения
     delete:
       удаляет данные о конкретном варианте для упражнения
    """
    queryset = Variants.objects.all()
    serializer_class = VariantsReadSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретном варианте для упражнения по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретном варианте для упражнения')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретном варианте для упражнения')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class FavoritesList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает список избранных
     post:
       добавляет новый элемент избранного для конкретного пользователя
    """
    queryset = Favorites.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return FavoritesWriteSerializer
        else:
            return FavoritesReadSerializer

    @swagger_auto_schema(operation_summary='получить список избранных')
    def get(self, request):
        return self.list(request)

    @swagger_auto_schema(operation_summary='добавить новое избранное')
    def post(self, request):
        return self.create(request)


class FavoritesDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретном избранном
     put:
       изменяет данные о конкретном избранном
     delete:
       удаляет данные о конкретном избранном
    """
    queryset = Favorites.objects.all()
    serializer_class = FavoritesWriteSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретном избранном по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретном избранном')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретном избранном')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class ShowInfoAboutRulesList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       дто для экранов в приложении для блока правил.
       Писать /?id_r=0, если нужен доступ в правилам. /?id_ex=0 - к заданию.
    """
    queryset = ShowInfoAboutRules.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        return ShowInfoAboutRulesSerializer

    @swagger_auto_schema(operation_summary='получить дто правил')
    def get(self, request, *args, **kwargs):
        id_ex = request.GET.get("id_ex")
        id_r = request.GET.get("id_r")
        if id_ex is not None:
            show_info = ShowInfoAboutRules.objects.filter(id_ex=id_ex)
            serializer = ShowInfoAboutRulesSerializer(show_info, many=True)
            return Response(serializer.data)
        elif id_r is not None:
            show_info = ShowInfoAboutRules.objects.filter(id_r=id_r)
            serializer = ShowInfoAboutRulesSerializer(show_info, many=True)
            return Response(serializer.data)
        else:
            return self.list(request, *args, **kwargs)


class ShowInfoAboutWordsLettersList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       дто для экранов в приложении для блока буквы-слова. Писать /api/showinfoaboutwordsletters/?id_ex=1
    """
    queryset = ShowInfoAboutWordsLetters.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        return ShowInfoAboutWordsLettersSerializer

    @swagger_auto_schema(operation_summary='получить дто букв-слов')
    def get(self, request, *args, **kwargs):
        id_ex = request.GET.get("id_ex")
        if id_ex is not None:
            show_info = ShowInfoAboutWordsLetters.objects.filter(id_ex=id_ex)
            serializer = ShowInfoAboutWordsLettersSerializer(show_info, many=True)
            return Response(serializer.data)
        else:
            return self.list(request, *args, **kwargs)


class ShowInfoAboutPhraseList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       дто для экранов в приложении для блока фразы. Писать /api/showinfoaboutphrase/?id_ex=1
       в variant отображены только те варианты, которые не правильные. Правильные брать по номеру пропущенного
    """
    queryset = ShowInfoAboutPhrase.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        return ShowInfoAboutPhraseSerializer

    @swagger_auto_schema(operation_summary='получить дто фраз')
    def get(self, request, *args, **kwargs):
        id_ex = request.GET.get("id_ex")
        if id_ex is not None:
            show_info = ShowInfoAboutPhrase.objects.filter(id_ex=id_ex)
            serializer = ShowInfoAboutPhraseSerializer(show_info, many=True)
            return Response(serializer.data)
        else:
            return self.list(request, *args, **kwargs)


# class NewlettersList(APIView):
#     def get(self, request):
#         newletter = Newletters.objects.all()
#         serializer = NewlettersSerializer(newletter, many=True)
#         return Response(serializer.data)
#
#
# class NewwordsList(APIView):
#     def get(self, request):
#         newword = Newwords.objects.all()
#         serializer = NewwordsSerializer(newword, many=True)
#         return Response(serializer.data)
#
#
# class NewphrasesList(APIView):
#     def get(self, request):
#         newword = Newphrases.objects.all()
#         serializer = NewphrasesSerializer(newword, many=True)
#         return Response(serializer.data)
#
#
# class MatchsyllablessoundList(APIView):
#     def get(self, request):
#         matchsyllablesound = Matchsyllablessound.objects.all()
#         serializer = MatchsyllablessoundSerializer(matchsyllablesound, many=True)
#         return Response(serializer.data)
#
#
# class CollectwordslettersList(APIView):
#     def get(self, request):
#         collectwordletter = Collectwordsletters.objects.all()
#         serializer = CollectwordslettersSerializer(collectwordletter, many=True)
#         return Response(serializer.data)
#
#
# class MissingletterList(APIView):
#     def get(self, request):
#         missletter = Missingletter.objects.all()
#         serializer = MissingletterSerializer(missletter, many=True)
#         return Response(serializer.data)
#
#
# class PronunciationwordsList(APIView):
#     def get(self, request):
#         pronunciationword = Pronunciationwords.objects.all()
#         serializer = PronunciationwordsSerializer(pronunciationword, many=True)
#         return Response(serializer.data)
#
#
# class RecoverphrasesList(APIView):
#     def get(self, request):
#         recoverphrase = Recoverphrases.objects.all()
#         serializer = RecoverphrasesSerializer(recoverphrase, many=True)
#         return Response(serializer.data)
#
#
# class SelectwordsList(APIView):
#     def get(self, request):
#         selectword = Selectwords.objects.all()
#         serializer = SelectwordsSerializer(selectword, many=True)
#         return Response(serializer.data)
#
#
# class WordpicturematchList(APIView):
#     def get(self, request):
#         wordpicturem = Wordpicturematch.objects.all()
#         serializer =WordpicturematchSerializer(wordpicturem, many=True)
#         return Response(serializer.data)
#
#
# class WordpictureselectList(APIView):
#     def get(self, request):
#         wordpictures = Wordpictureselect.objects.all()
#         serializer = WordpictureselectSerializer(wordpictures, many=True)
#         return Response(serializer.data)
#
#
# class WritewordsList(APIView):
#     def get(self, request):
#         writeword = Writewords.objects.all()
#         serializer = WritewordsSerializer(writeword, many=True)
#         return Response(serializer.data)
#

'''
class CountryList(APIView):
    def get(self, request):
        countries = Countries.objects.all()
        serializer = CountriesSerializer(countries, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CountriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CountryDetails(APIView):
      def get_object(self, pk):
          try:
              return Countries.objects.get(pk=pk)
        
          except Countries.DoesNotExist:
              return Response(status=status.HTTP_404_NOT_FOUND)

      def get(self, request, pk):  
        country = self.get_object(pk)
        serializer = CountriesSerializer(country)
        return Response(serializer.data) 
    
      def put(self, request, pk):
        country = self.get_object(pk)
        serializer = CountriesSerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      def delete(self, request, pk):
         country = self.get_object(pk)
         country.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)



ДРУГОЙ СПОСОБ
@api_view(['GET', 'POST'])
def country_list(request):
    
    
    #get all countries
    if request.method == 'GET':
        countries = Countries.objects.all()
        serializer = CountriesSerializer(countries, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CountriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def country_details(request, pk):
    try:
        country = Countries.objects.get(pk=pk)
        
    except Countries.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == "GET":
        serializer = CountriesSerializer(country)
        return Response(serializer.data)
    
    
    elif request.method == 'PUT':
        serializer = CountriesSerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
