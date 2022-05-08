import os

from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Video
# , VideoCommands
from .serializers import VideoSerializer \
    # , VideoCommandsReadSerializer, VideoCommandsWriteSerializer


# Create your views here.


class VideoList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает данные о всех видео и о командах, из которых состоит видео
     post:
       добавляет новые данные о видео. Команды запоминаться в массив. Писать '{"бежать", "стоять"}
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    @swagger_auto_schema(operation_summary='получить список данных для видео')
    def get(self, request):
        return self.list(request)

    @swagger_auto_schema(operation_summary='добавить новые данные для видео')
    def post(self, request):
        return self.create(request)


class VideoDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретном видео с командами
     put:
       изменяет данные о конкретном видео с командами. Команды запоминаться в массив. Писать '{"бежать", "стоять"}'
     delete:
       удаляет данные о видео и командах
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретном видео по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретном видео')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретном видео')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


@api_view(['GET'])
def showcommands(request):
    if request.method == 'GET':
        l = []
        for filenames in os.listdir('media/video'):
            veter = filenames.replace('.', '')
            veter = veter.replace(' ', '')
            veter = veter.replace('mov', '')
            veter = veter.replace(veter[0], '').lower()
            l.append(veter)
        return Response(l)

# class VideoCommandsList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = VideoCommands.objects.all()
#
#     def get_serializer_class(self):
#         method = self.request.method
#         if method == 'PUT' or method == 'POST':
#             return VideoCommandsWriteSerializer
#         else:
#             return VideoCommandsReadSerializer
#
#     def get(self, request, *args, **kwargs):
#         id_v = request.GET.get("id_v")
#         if id_v is not None:
#             cer_video = VideoCommands.objects.filter(id_v=id_v)
#             serializer = VideoCommandsWriteSerializer(cer_video, many=True)
#             return Response(serializer.data)
#         else:
#             return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class VideoCommandsDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
#                            mixins.DestroyModelMixin):
#     queryset = VideoCommands.objects.all()
#     serializer_class = VideoCommandsWriteSerializer
#
#     def get(self, request, pk):
#         return self.retrieve(request, pk=pk)
#
#     def put(self, request, pk):
#         return self.update(request, pk=pk)
#
#     def delete(self, request, pk):
#         return self.destroy(request, pk=pk)
#
