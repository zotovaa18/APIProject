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
from .views import RecoverphrasesList, SelectwordsList, WordpicturematchList, WordpictureselectList, WritewordsList, TimeSpentList
#country_list, country_details LexemesList


urlpatterns = [

    path('api/countries/', CountryList.as_view()),
    path('api/countries/<str:pk>/', CountryDetails.as_view()),
    path('api/peoplegroups/', PeopleGroupsList.as_view()),
    path('api/peoplegroups/<str:pk>/', PeopleGroupsDetails.as_view()),
    path('api/exercises/',ExercisesList.as_view()),
    path('api/exercises/<int:pk>/', ExercisesDetails.as_view()),
    path('api/favorites/',FavoritesList.as_view()),
    path('api/favorites/<int:pk>/', FavoritesDetails.as_view()),
    path('api/ik/',IkList.as_view()),
    path('api/ik/<str:pk>/', IkDetails.as_view()),
    path('api/lecfilling/',LecFillingList.as_view()),
    path('api/lecfilling/<int:pk>/', LecFillingDetails.as_view()),
    path('api/lessonblocks/', LessonBlocksList.as_view()),
    path('api/lessonblocks/<int:pk>/', LessonBlocksDetails.as_view()),
    path('api/lessons/', LessonsList.as_view()),
    path('api/lessons/<int:pk>/', LessonsDetails.as_view()),
    path('api/lexemes/', LexemesViewsets.as_view()),
    path('api/lexemes/<int:pk>/', LexemesDetails.as_view()),
    path('api/media/', MediaList.as_view()),
    path('api/media/<int:pk>/', MediaDetails.as_view()),
    path('api/people/', PeopleList.as_view()),
    path('api/people/<str:pk>/', PeopleDetails.as_view()),
    path('api/progress/', ProgressList.as_view()),
    path('api/progress/<int:pk>/', ProgressDetails.as_view()),
    path('api/rules/', RulesList.as_view()),
    path('api/rules/<int:pk>/', RulesDetails.as_view()),
    path('api/ruleslexemes/', RulesLexemesList.as_view()),
    path('api/ruleslexemes/<int:pk>/', RulesLexemesDetails.as_view()),
    path('api/replicas/', ReplicasList.as_view()),
    path('api/replicas/<int:pk>/', ReplicasDetails.as_view()),
    path('api/tasks/', TasksList.as_view()),
    path('api/tasks/<int:pk>/', TasksDetails.as_view()),
    path('api/typesEx/', TypesExList.as_view()),
    path('api/typesEx/<int:pk>/', TypesExDetails.as_view()),
    path('api/typesLex/', TypesLexList.as_view()),
    path('api/typesLex/<int:pk>/', TypesLexDetails.as_view()),
    path('api/typesMed/', TypesMedList.as_view()),
    path('api/typesMed/<int:pk>/', TypesMedDetails.as_view()),
    path('api/variants/', VariantsList.as_view()),
    path('api/variants/<int:pk>/', VariantsDetails.as_view()),
    path('api/newletters/', NewlettersList.as_view()),
    path('api/newwords/', NewwordsList.as_view()),
    path('api/newphrases/', NewphrasesList.as_view()),
    path('api/matchsyllablessound/', MatchsyllablessoundList.as_view()),
    path('api/collectwordsletters/', CollectwordslettersList.as_view()),
    path('api/missingletter/', MissingletterList.as_view()),
    path('api/pronunciationwords/', PronunciationwordsList.as_view()),
    path('api/recoverphrases/', RecoverphrasesList.as_view()),
    path('api/selectwords/', SelectwordsList.as_view()),
    path('api/wordpicturematch/', WordpicturematchList.as_view()),
    path('api/wordpictureselect/', WordpictureselectList.as_view()),
    path('api/writewords/', WritewordsList.as_view()),
    path('api/time_spent/', TimeSpentList.as_view())
]