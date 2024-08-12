from django.shortcuts import render
from rest_framework import viewsets
from api.models import Albom,Artist,Songs
from .serializers import AlbomSerializersWeb,ArtistSerializersWeb,SongsSerializersWeb

class ArtistViewSetWeb(viewsets.ModelViewSet):
    def get_queryset(self):
        return Artist.objects.all()

    serializer_class = ArtistSerializersWeb

class AlbomViewSetWeb(viewsets.ModelViewSet):
    def get_queryset(self):
        return Albom.objects.all()

    serializer_class = AlbomSerializersWeb

class SongsViewSetWeb(viewsets.ModelViewSet):
    def get_queryset(self):
        return Songs.objects.all()

    serializer_class = SongsSerializersWeb
