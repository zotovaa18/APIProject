from django.db import transaction
from moviepy.editor import *
from rest_framework import serializers

from .models import Video


# VideoCommands


class VideoSerializer(serializers.ModelSerializer):
    commands = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Video
        fields = ('id_v', 'name_video', 'commands', 'video_link')

    @transaction.atomic
    def create(self, validated_data):
        print(validated_data.get('name_video'))
        videocreate = Video.objects.create(name_video=validated_data.get('name_video'))
        videocreate.commands = validated_data.get('commands')
        videocreate.save()
        clips = []

        for filename in os.listdir('media/video'):
            veter = filename.replace('.', '')
            veter = veter.replace(' ', '')
            veter = veter.replace('mov', '')
            veter = veter.replace(veter[0], '').lower()
            print(veter)
            if veter in validated_data.get('commands'):
                print('true')
                clips.append(VideoFileClip(os.path.dirname('media/video/') + '/' + filename))
        video = concatenate_videoclips(clips, method='compose')
        video.write_videofile('media/video_lesson/' + videocreate.name_video + '.mp4')
        videocreate.video_link = 'http://api.unolingua.flareon.ru/' + 'media/video_lesson/' + videocreate.name_video + '.mp4'

        # with open('media/video_lesson/'+videocreate.name_video+'.mp4') as f:
        #     videocreate.video_link.save(videocreate.name_video+'.mp4', File(f))

        return videocreate

# class VideoCommandsWriteSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = VideoCommands
#        fields = ('id', 'id_v', 'command', 'num')
#
#
# class VideoCommandsReadSerializer(serializers.ModelSerializer):
#    class Meta(VideoCommandsWriteSerializer.Meta):
#        depth = 1
