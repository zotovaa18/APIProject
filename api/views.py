#from django.shortcuts import render, HttpResponse
from .models import Countries, PeopleGroups, People, TypesLex, TypesMed, LessonBlocks, Lessons
from .models import Lexemes, Media, Ik, Replicas, LecFilling, Reduction, ReductionLexemes, TypesEx
from .models import Exercises, Progress, Tasks, Variants, Favorites
from .models import Newletters, Newwords, Newphrases, Matchsyllablessound, Collectwordsletters, Missingletter
from .models import Pronunciationwords, Recoverphrases, Selectwords, Wordpicturematch, Wordpictureselect, Writewords
from .serializers import CountriesSerializer, PeopleGroupsSerializer, PeopleSerializer, TypesLexSerializer, TypesMedSerializer, LessonBlocksSerializer, LexemesSerializer
from .serializers import LessonsSerializer, MediaSerializer, IkSerializer, ReplicasSerializer, LecFillingSerializer,ReductionSerializer, ReductionLexemesSerializer, TypesExSerializer
from .serializers import ExercisesSerializer, ProgressSerializer, TasksSerializer, VariantsSerializer, FavoritesSerializer
from .serializers import NewlettersSerializer, NewwordsSerializer, NewphrasesSerializer, MatchsyllablessoundSerializer, CollectwordslettersSerializer, MissingletterSerializer
from .serializers import PronunciationwordsSerializer, RecoverphrasesSerializer, SelectwordsSerializer, WordpicturematchSerializer, WordpictureselectSerializer, WritewordsSerializer
'''from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view'''
from rest_framework.response import Response
#from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework import mixins
# Create your views here.

class CountryList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class CountryDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)
    
    
    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)
  
class PeopleGroupsList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = PeopleGroups.objects.all()
    serializer_class = PeopleGroupsSerializer
    
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class PeopleGroupsDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = PeopleGroups.objects.all()
    serializer_class = PeopleGroupsSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)
    
    
    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)

class PeopleList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class PeopleDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)
    
    
    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)
    
class TypesLexList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = TypesLex.objects.all()
    serializer_class = TypesLexSerializer
    
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class TypesLexDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = TypesLex.objects.all()
    serializer_class = TypesLexSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)
    
    
    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)
    
class TypesMedList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = TypesMed.objects.all()
    serializer_class = TypesMedSerializer
    
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class TypesMedDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
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
    serializer_class = LessonBlocksSerializer
    
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class LessonBlocksDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = LessonBlocks.objects.all()
    serializer_class = LessonBlocksSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)
    
    
    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class LessonsList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
    
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class LessonsDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)
    
    
    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)    

    
class LexemesList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = Lexemes.objects.all()
    serializer_class = LexemesSerializer
    
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class LexemesDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Lexemes.objects.all()
    serializer_class = LexemesSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)
    
    
    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)

class MediaList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class MediaDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)
    
    
    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)

class IkList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
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

class ReplicasList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = Replicas.objects.all()
    serializer_class = ReplicasSerializer
    
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class ReplicasDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Replicas.objects.all()
    serializer_class = ReplicasSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)
    
    
    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)

class LecFillingList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = LecFilling.objects.all()
    serializer_class = LecFillingSerializer
    
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class LecFillingDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = LecFilling.objects.all()
    serializer_class = LecFillingSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)
    
    
    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)

class ReductionList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = Reduction.objects.all()
    serializer_class = ReductionSerializer
    
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class ReductionDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Reduction.objects.all()
    serializer_class = ReductionSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)
    
    
    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)

class ReductionLexemesList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = ReductionLexemes.objects.all()
    serializer_class = ReductionLexemesSerializer
    
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class ReductionLexemesDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = ReductionLexemes.objects.all()
    serializer_class = ReductionLexemesSerializer
    
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
    serializer_class = ExercisesSerializer
    
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class ExercisesDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Exercises.objects.all()
    serializer_class = ExercisesSerializer
    
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
    serializer_class = TasksSerializer
    
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class TasksDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)
    
    
    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)
    
class VariantsList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = Variants.objects.all()
    serializer_class = VariantsSerializer
    
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class VariantsDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Variants.objects.all()
    serializer_class = VariantsSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)
    
    
    def put(self, request, pk):
        return self.update(request, pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)
    
class FavoritesList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
    
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class FavoritesDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
    
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


