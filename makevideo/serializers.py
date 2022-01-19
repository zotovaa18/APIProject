from rest_framework import serializers

from .models import Video, VideoCommands


class VideoSerializer(serializers.ModelSerializer):
   class Meta:
       model = Video
       fields = ('id_v', 'name_video')


class VideoCommandsSerializer(serializers.ModelSerializer):
   class Meta:
       model = VideoCommands
       fields = ('id', 'id_v', 'command', 'num')