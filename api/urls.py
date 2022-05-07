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
    path('mediafiles/', MediaList.as_view()),
    path('mediafiles/<int:pk>/', MediaDetails.as_view()),
    path('people/', PeopleList.as_view()),
    path('people/<str:pk>/', PeopleDetails.as_view()),
    path('progress/', ProgressList.as_view()),
    path('progress/<int:pk>/', ProgressDetails.as_view()),
    path('rules/', RulesList.as_view()),
    path('rules/<int:pk>/', RulesDetails.as_view()),
    path('ruleslexemes/', RulesLexemesList.as_view()),
    path('ruleslexemes/<int:pk>/', RulesLexemesDetails.as_view()),
    path('replicas/', ReplicasList.as_view()),
    path('replicas/<int:pk>/', ReplicasDetails.as_view()),
    path('tasks/', TasksList.as_view()),
    path('tasks/<int:pk>/', TasksDetails.as_view()),
    path('typesex/', TypesExList.as_view()),
    path('typesex/<int:pk>/', TypesExDetails.as_view()),
    path('typeslex/', TypesLexList.as_view()),
    path('typeslex/<str:pk>/', TypesLexDetails.as_view()),
    path('typesmed/', TypesMedList.as_view()),
    path('typesmed/<str:pk>/', TypesMedDetails.as_view()),
    path('status/', StatusList.as_view()),
    path('status/<str:pk>/', StatusDetails.as_view()),
    path('variants/', VariantsList.as_view()),
    path('variants/<int:pk>/', VariantsDetails.as_view()),
    path('vowelsound/', VowelSoundList.as_view()),
    path('vowelsound/<int:pk>/', VowelSoundDetails.as_view()),
    path('showinfoaboutrules/', ShowInfoAboutRulesList.as_view()),
    path('showinfoaboutwordsletters/', ShowInfoAboutWordsLettersList.as_view()),
    path('showinfoaboutphrase/', ShowInfoAboutPhraseList.as_view()),
    path('forlessonsdto/', ForLessonsList.as_view()),
    path('forlessonsdto/<int:pk>/', ForLessonsDetails.as_view()),
    path('lessoninfodto/', LessonInfoList.as_view()),
    path('rulesdto/', RulesDTOList.as_view()),
    path('lexdto/', LexDTOList.as_view()),
    path('time_spent/', TimeSpentList.as_view()),
    path('time_spent/<int:pk>/', TimeSpentDetails.as_view()),
    path('dialogdto/', DialogDTOList.as_view()),
    path('phrasesdto/', PhrasesDTOList.as_view()),
    path('rating/', RatingList.as_view()),
    path('num_stop/', NumStopList.as_view()),
    # path('weak_points/', WeakPointsList.as_view()),
    # path('weak_points/<int:pk>/', WeakPointsDetails.as_view()),
    path('number_of_weak_points/', NumberOfWeakPointsList.as_view()),
    path('progress_blocks/', ProgressBlocksList.as_view()),
    path('weak_points/', WeakPointsList.as_view()),
    path('weaks/', WeaksList.as_view()),
    path('deletedto/', DeleteDTOList.as_view()),

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