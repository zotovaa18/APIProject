from django.urls import path
from .views import VideoList, VideoDetails\
    #, VideoCommandsList, VideoCommandsDetails

urlpatterns = [
    path('api/makevideo/video/', VideoList.as_view()),
    path('api/makevideo/video/<str:pk>/', VideoDetails.as_view()),
    #path('api/makevideo/videocommands/', VideoCommandsList.as_view()),
    #path('api/makevideo/videocommands/<str:pk>/', VideoCommandsDetails.as_view()),
]
