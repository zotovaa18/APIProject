# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 01:53:05 2021

@author: zotov
"""


from django.urls import path, include
#country_list, country_details LexemesList, ForLessonsList
from .views import *

from rest_framework import routers

from api import views

# router = routers.DefaultRouter()
# router.register(r'lessons', views.LessonsDetails)

urlpatterns = [
    # path('api/', include(router.urls)),
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
    path('api/typesex/', TypesExList.as_view()),
    path('api/typesex/<int:pk>/', TypesExDetails.as_view()),
    path('api/typeslex/', TypesLexList.as_view()),
    path('api/typeslex/<str:pk>/', TypesLexDetails.as_view()),
    path('api/typesmed/', TypesMedList.as_view()),
    path('api/typesmed/<str:pk>/', TypesMedDetails.as_view()),
    path('api/status/', StatusList.as_view()),
    path('api/status/<str:pk>/', StatusDetails.as_view()),
    path('api/variants/', VariantsList.as_view()),
    path('api/variants/<int:pk>/', VariantsDetails.as_view()),
    path('api/vowelsound/', VowelSoundList.as_view()),
    path('api/vowelsound/<int:pk>/', VowelSoundDetails.as_view()),
    path('api/showinfoaboutrules/', ShowInfoAboutRulesList.as_view()),
    path('api/showinfoaboutwordsletters/', ShowInfoAboutWordsLettersList.as_view()),
    path('api/showinfoaboutphrase/', ShowInfoAboutPhraseList.as_view()),
    path('api/forlessonsdto/',ForLessonsList.as_view()),
    path('api/lessoninfodto/', LessonInfoList.as_view()),
    path('api/rulesdto/', RulesDTOList.as_view()),
    path('api/time_spent/', TimeSpentList.as_view()),
    path('api/time_spent/<int:pk>/', TimeSpentDetails.as_view()),

    # path('api/newletters/', NewlettersList.as_view()),
    # path('api/newwords/', NewwordsList.as_view()),
    # path('api/newphrases/', NewphrasesList.as_view()),
    # path('api/matchsyllablessound/', MatchsyllablessoundList.as_view()),
    # path('api/collectwordsletters/', CollectwordslettersList.as_view()),
    # path('api/missingletter/', MissingletterList.as_view()),
    # path('api/pronunciationwords/', PronunciationwordsList.as_view()),
    # path('api/recoverphrases/', RecoverphrasesList.as_view()),
    # path('api/selectwords/', SelectwordsList.as_view()),
    # path('api/wordpicturematch/', WordpicturematchList.as_view()),
    # path('api/wordpictureselect/', WordpictureselectList.as_view()),
    # path('api/writewords/', WritewordsList.as_view()),
]