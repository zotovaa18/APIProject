from rest_framework import serializers

from .models import Video, VideoCommands


class VideoSerializer(serializers.ModelSerializer):
   class Meta:
       model = Video
       fields = ('id_v', 'name_video')


class VideoCommandsWriteSerializer(serializers.ModelSerializer):
   class Meta:
       model = VideoCommands
       fields = ('id', 'id_v', 'command', 'num')


class VideoCommandsReadSerializer(serializers.ModelSerializer):
   class Meta(VideoCommandsWriteSerializer.Meta):
       depth = 1