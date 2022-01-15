# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 01:53:05 2021

@author: zotov
"""


from django.urls import path
from .views import CountryList, CountryDetails, PeopleGroupsList, PeopleGroupsDetails, ExercisesList, ExercisesDetails, ProgressDetails
from .views import FavoritesList, IkList, IkDetails, LecFillingList, LessonBlocksList, LessonBlocksDetails, LecFillingDetails,  RulesLexemesDetails
from .views import LessonsList, LessonsDetails, LexemesViewsets, LexemesDetails, MediaDetails, MediaList, PeopleDetails, PeopleList
from .views import ProgressList, RulesList, RulesDetails, RulesLexemesList, ReplicasList, ReplicasDetails, TasksList, TasksDetails
from .views import TypesExList, TypesExDetails, TypesLexDetails, TypesLexList, TypesMedDetails, TypesMedList, VariantsList, FavoritesDetails, VariantsDetails
from .views import NewlettersList, NewwordsList, NewphrasesList, MatchsyllablessoundList, CollectwordslettersList, MissingletterList, PronunciationwordsList
from .views import RecoverphrasesList, SelectwordsList, WordpicturematchList, WordpictureselectList, WritewordsList
#country_list, country_details LexemesList


urlpatterns = [
    
    path('countries/', CountryList.as_view()),
    path('countries/<str:pk>/', CountryDetails.as_view()),
    path('peoplegroups/', PeopleGroupsList.as_view()),
    path('peoplegroups/<str:pk>/', PeopleGroupsDetails.as_view()),
    path('exercises/',ExercisesList.as_view()),
    path('exercises/<int:pk>/', ExercisesDetails.as_view()),
    path('favorites/',FavoritesList.as_view()),
    path('favorites/<int:pk>/', FavoritesDetails.as_view()),
    path('ik/',IkList.as_view()),
    path('ik/<str:pk>/', IkDetails.as_view()),
    path('lecfilling/',LecFillingList.as_view()),
    path('lecfilling/<int:pk>/', LecFillingDetails.as_view()),
    path('lessonblocks/', LessonBlocksList.as_view()),
    path('lessonblocks/<int:pk>/', LessonBlocksDetails.as_view()),
    path('lessons/', LessonsList.as_view()),
    path('lessons/<int:pk>/', LessonsDetails.as_view()),
    path('lexemes/', LexemesViewsets.as_view()),
    path('lexemes/<int:pk>/', LexemesDetails.as_view()),
    path('media/', MediaList.as_view()),
    path('media/<int:pk>/', MediaDetails.as_view()),
    path('people/', PeopleList.as_view()),
    path('people/<str:pk>/', PeopleDetails.as_view()),
    path('progress/', ProgressList.as_view()),
    path('progress/<int:pk>/', ProgressDetails.as_view()),
    path('rules/', RulesList.as_view({'get': 'list'})),
    path('rules/<int:pk>/', RulesDetails.as_view()),
    path('ruleslexemes/', RulesLexemesList.as_view()),
    path('ruleslexemes/<int:pk>/', RulesLexemesDetails.as_view()),
    path('replicas/', ReplicasList.as_view()),
    path('replicas/<int:pk>/', ReplicasDetails.as_view()),
    path('tasks/', TasksList.as_view()),
    path('tasks/<int:pk>/', TasksDetails.as_view()),
    path('typesEx/', TypesExList.as_view()),
    path('typesEx/<int:pk>/', TypesExDetails.as_view()),
    path('typesLex/', TypesLexList.as_view()),
    path('typesLex/<int:pk>/', TypesLexDetails.as_view()),
    path('typesMed/', TypesMedList.as_view()),
    path('typesMed/<int:pk>/', TypesMedDetails.as_view()),
    path('variants/', VariantsList.as_view()),
    path('variants/<int:pk>/', VariantsDetails.as_view()),
    path('newletters/', NewlettersList.as_view()),
    path('newwords/', NewwordsList.as_view()),
    path('newphrases/', NewphrasesList.as_view()),
    path('matchsyllablessound/', MatchsyllablessoundList.as_view()),
    path('collectwordsletters/', CollectwordslettersList.as_view()),
    path('missingletter/', MissingletterList.as_view()),
    path('pronunciationwords/', PronunciationwordsList.as_view()),
    path('recoverphrases/', RecoverphrasesList.as_view()),
    path('selectwords/', SelectwordsList.as_view()),
    path('wordpicturematch/', WordpicturematchList.as_view()),
    path('wordpictureselect/', WordpictureselectList.as_view()),
    path('writewords/', WritewordsList.as_view()),
]