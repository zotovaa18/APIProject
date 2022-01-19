from django.urls import path
from .views import VideoList, VideoDetails, VideoCommandsList, VideoCommandsDetails

urlpatterns = [
    path('makevideo/video/', VideoList.as_view()),
    path('makevideo/video/<str:pk>/', VideoDetails.as_view()),
    path('makevideo/videocommands/', VideoCommandsList.as_view()),
    path('makevideo/videocommands/<str:pk>/', VideoCommandsDetails.as_view()),
]
