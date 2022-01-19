from django.contrib import admin
from .models import Video, VideoCommands

# Register your models here.

@admin.register(Video)
class VideoModel(admin.ModelAdmin):
    list_filter = ('id_v', 'name_video')
    list_display = ('id_v', 'name_video')

@admin.register(VideoCommands)
class VideoCommandsModel(admin.ModelAdmin):
    list_filter = ('id', 'id_v', 'command', 'num')
    list_display = ('id', 'id_v', 'command', 'num')