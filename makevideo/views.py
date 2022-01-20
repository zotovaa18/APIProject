from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

from .models import Video, VideoCommands
from .serializers import VideoSerializer, VideoCommandsReadSerializer, VideoCommandsWriteSerializer

# Create your views here.


class VideoList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class VideoDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class VideoCommandsList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = VideoCommands.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return VideoCommandsWriteSerializer
        else:
            return VideoCommandsReadSerializer

    def get(self, request, *args, **kwargs):
        id_v = request.GET.get("id_v")
        if id_v is not None:
            cer_video = VideoCommands.objects.filter(id_v=id_v)
            serializer = VideoCommandsWriteSerializer(cer_video, many=True)
            return Response(serializer.data)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VideoCommandsDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin):
    queryset = VideoCommands.objects.all()
    serializer_class = VideoCommandsWriteSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)

