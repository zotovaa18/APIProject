#from django.shortcuts import render, HttpResponse
from .models import Countries, PeopleGroups, People, TypesLex, TypesMed, LessonBlocks, Lessons, ShowInfoAboutPhrase
from .models import Lexemes, Medias, Ik, Replicas, LecFilling, Rules, RulesLexemes, TypesEx, ShowInfoAboutWordsLetters
from .models import Exercises, Progress, Tasks, Variants, Favorites, Status, VowelSound, ShowInfoAboutRules
from .models import Newletters, Newwords, Newphrases, Matchsyllablessound, Collectwordsletters, Missingletter
from .models import Pronunciationwords, Recoverphrases, Selectwords, Wordpicturematch, Wordpictureselect, Writewords
from .serializers import CountriesSerializer, PeopleGroupsSerializer, PeopleSerializer, TypesLexSerializer, TypesMedSerializer, LessonBlocksWriteSerializer, LessonBlocksReadSerializer
from .serializers import MediaReadSerializer, MediaWriteSerializer, IkSerializer, ReplicasReadSerializer, ReplicasWriteSerializer
from .serializers import ExercisesWriteSerializer, ExercisesReadSerializer, ProgressSerializer, TasksReadSerializer, TasksWriteSerializer, VariantsWriteSerializer, VariantsReadSerializer, FavoritesReadSerializer, FavoritesWriteSerializer, RulesLexemesSerializer, TypesExSerializer
from .serializers import NewlettersSerializer, NewwordsSerializer, NewphrasesSerializer, MatchsyllablessoundSerializer, CollectwordslettersSerializer, MissingletterSerializer
from .serializers import PronunciationwordsSerializer, RecoverphrasesSerializer, SelectwordsSerializer, WordpicturematchSerializer, WordpictureselectSerializer
from .serializers import LexemesWriteSerializer, LexemesReadSerializer, LessonsWriteSerializer, LessonsReadSerializer, StatusSerializer
from .serializers import LecFillingReadSerializer, LecFillingWriteSerializer, RulesSerializer, WritewordsSerializer, RulesReadSerializer
from .serializers import VowelSoundReadSerializer, VowelSoundWriteSerializer, ShowInfoAboutRulesSerializer, ShowInfoAboutWordsLettersSerializer
from .serializers import ShowInfoAboutPhraseSerializer
'''from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view'''
from rest_framework.response import Response
#from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework import mixins
import coreapi
from rest_framework.schemas import AutoSchema
from rest_framework import viewsets

# Create your views here.


from rest_framework import viewsets

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

# @method_decorator(name='list', decorator=swagger_auto_schema(
#     operation_description="description from swagger_auto_schema via method_decorator"
# ))
class CountryList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    """retrieve:
        """
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class CountryDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class PeopleGroupsList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = PeopleGroups.objects.all()
    serializer_class = PeopleGroupsSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class PeopleGroupsDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin):
    queryset = PeopleGroups.objects.all()
    serializer_class = PeopleGroupsSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class StatusList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class StatusDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class PeopleList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class PeopleDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class TypesLexList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = TypesLex.objects.all()
    serializer_class = TypesLexSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class TypesLexDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = TypesLex.objects.all()
    serializer_class = TypesLexSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class TypesMedList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = TypesMed.objects.all()
    serializer_class = TypesMedSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class TypesMedDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = TypesMed.objects.all()
    serializer_class = TypesMedSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class LessonBlocksList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = LessonBlocks.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return LessonBlocksWriteSerializer
        else:
            return LessonBlocksReadSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LessonBlocksDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin):
    queryset = LessonBlocks.objects.all()
    serializer_class = LessonBlocksWriteSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class LessonsList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Lessons.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return LessonsWriteSerializer
        else:
            return LessonsReadSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LessonsDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Lessons.objects.all()
    serializer_class = LessonsWriteSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class LexemesViewsets(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Lexemes.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return LexemesWriteSerializer
        else:
            return LexemesReadSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LexemesDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Lexemes.objects.all()
    serializer_class = LexemesWriteSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)
    
    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class VowelSoundList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = VowelSound.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return VowelSoundWriteSerializer
        else:
            return VowelSoundReadSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VowelSoundDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    queryset = VowelSound.objects.all()
    serializer_class = VowelSoundWriteSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class MediaList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Medias.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return MediaWriteSerializer
        else:
            return MediaReadSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MediaDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Medias.objects.all()
    serializer_class = MediaWriteSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)
    
    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class IkList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Ik.objects.all()
    serializer_class = IkSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class IkDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Ik.objects.all()
    serializer_class = IkSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class ReplicasList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Replicas.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return ReplicasWriteSerializer
        else:
            return ReplicasReadSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ReplicasDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Replicas.objects.all()
    serializer_class = ReplicasWriteSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class LecFillingList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = LecFilling.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return LecFillingWriteSerializer
        else:
            return LecFillingReadSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LecFillingDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    queryset = LecFilling.objects.all()
    serializer_class = LecFillingWriteSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class RulesList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Rules.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return RulesSerializer
        else:
            return RulesReadSerializer

    def get(self, request, *args, **kwargs):
        id_v = request.GET.get("id_v")
        if id_v is not None:
            cer_video = RulesLexemes.objects.filter(id_v=id_v)
            serializer = RulesLexemesSerializer(cer_video, many=True)
            return Response(serializer.data)
        else:
            return self.list(request, *args, **kwargs)

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
    queryset = Rules.objects.all()
    serializer_class = RulesSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class RulesLexemesList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = RulesLexemes.objects.all()
    serializer_class = RulesLexemesSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class RulesLexemesDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = RulesLexemes.objects.all()
    serializer_class = RulesLexemesSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class TypesExList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = TypesEx.objects.all()
    serializer_class = TypesExSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class TypesExDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = TypesEx.objects.all()
    serializer_class = TypesExSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class ExercisesList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = Exercises.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return ExercisesWriteSerializer
        else:
            return ExercisesReadSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class ExercisesDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Exercises.objects.all()

    serializer_class = ExercisesWriteSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class ProgressList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class ProgressDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class TasksList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = Tasks.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return TasksWriteSerializer
        else:
            return TasksReadSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class TasksDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Tasks.objects.all()
    serializer_class = TasksWriteSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class VariantsList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Variants.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return VariantsWriteSerializer
        else:
            return VariantsReadSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class VariantsDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Variants.objects.all()
    serializer_class = VariantsReadSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class FavoritesList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Favorites.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return FavoritesWriteSerializer
        else:
            return FavoritesReadSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class FavoritesDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesWriteSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


# class NewlettersList(generics.GenericAPIView, mixins.ListModelMixin,
#                   mixins.CreateModelMixin):
#     queryset = Newletters.objects.all()
#     serializer_class = NewlettersSerializer
    
    
#     def get(self, request):
#         return self.list(request)


class ShowInfoAboutRulesList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = ShowInfoAboutRules.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        return ShowInfoAboutRulesSerializer

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

# писать /api/showinfoaboutrules/?id_ex=0


class ShowInfoAboutWordsLettersList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = ShowInfoAboutWordsLetters.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        return ShowInfoAboutWordsLettersSerializer

    def get(self, request, *args, **kwargs):
        id_ex = request.GET.get("id_ex")
        if id_ex is not None:
            show_info = ShowInfoAboutWordsLetters.objects.filter(id_ex=id_ex)
            serializer = ShowInfoAboutWordsLettersSerializer(show_info, many=True)
            return Response(serializer.data)
        else:
            return self.list(request, *args, **kwargs)
# Писать /api/showinfoaboutwordsletters/?id_ex=1


class ShowInfoAboutPhraseList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = ShowInfoAboutPhrase.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        return ShowInfoAboutPhraseSerializer

    def get(self, request, *args, **kwargs):
        id_ex = request.GET.get("id_ex")
        if id_ex is not None:
            show_info = ShowInfoAboutPhrase.objects.filter(id_ex=id_ex)
            serializer = ShowInfoAboutPhraseSerializer(show_info, many=True)
            return Response(serializer.data)
        else:
            return self.list(request, *args, **kwargs)
# Писать /api/showinfoaboutphrase/?id_ex=1


class NewlettersList(APIView):
    def get(self, request):
        newletter = Newletters.objects.all()
        serializer = NewlettersSerializer(newletter, many=True)
        return Response(serializer.data)

    
class NewwordsList(APIView):
    def get(self, request):
        newword = Newwords.objects.all()
        serializer = NewwordsSerializer(newword, many=True)
        return Response(serializer.data)


class NewphrasesList(APIView):
    def get(self, request):
        newword = Newphrases.objects.all()
        serializer = NewphrasesSerializer(newword, many=True)
        return Response(serializer.data)


class MatchsyllablessoundList(APIView):
    def get(self, request):
        matchsyllablesound = Matchsyllablessound.objects.all()
        serializer = MatchsyllablessoundSerializer(matchsyllablesound, many=True)
        return Response(serializer.data)    


class CollectwordslettersList(APIView):
    def get(self, request):
        collectwordletter = Collectwordsletters.objects.all()
        serializer = CollectwordslettersSerializer(collectwordletter, many=True)
        return Response(serializer.data)   
    

class MissingletterList(APIView):
    def get(self, request):
        missletter = Missingletter.objects.all()
        serializer = MissingletterSerializer(missletter, many=True)
        return Response(serializer.data)   


class PronunciationwordsList(APIView):
    def get(self, request):
        pronunciationword = Pronunciationwords.objects.all()
        serializer = PronunciationwordsSerializer(pronunciationword, many=True)
        return Response(serializer.data)       


class RecoverphrasesList(APIView):
    def get(self, request):
        recoverphrase = Recoverphrases.objects.all()
        serializer = RecoverphrasesSerializer(recoverphrase, many=True)
        return Response(serializer.data) 


class SelectwordsList(APIView):
    def get(self, request):
        selectword = Selectwords.objects.all()
        serializer = SelectwordsSerializer(selectword, many=True)
        return Response(serializer.data) 


class WordpicturematchList(APIView):
    def get(self, request):
        wordpicturem = Wordpicturematch.objects.all()
        serializer =WordpicturematchSerializer(wordpicturem, many=True)
        return Response(serializer.data) 


class WordpictureselectList(APIView):
    def get(self, request):
        wordpictures = Wordpictureselect.objects.all()
        serializer = WordpictureselectSerializer(wordpictures, many=True)
        return Response(serializer.data) 

    
class WritewordsList(APIView):
    def get(self, request):
        writeword = Writewords.objects.all()
        serializer = WritewordsSerializer(writeword, many=True)
        return Response(serializer.data)     


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
