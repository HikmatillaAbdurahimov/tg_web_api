from django.shortcuts import render
from rest_framework import viewsets
from api.models import Albom,Artist,Songs
from .serializers import ArtistSerializersTg,AlbomSerializersTg,SongsAlbomSerializersTg

class ArtistViewSetTg(viewsets.ModelViewSet):
    def get_queryset(self):
        return Artist.objects.all()

    serializer_class = ArtistSerializersTg

class AlbomViewSetTg(viewsets.ModelViewSet):
    def get_queryset(self):
        return Albom.objects.all()

    serializer_class = AlbomSerializersTg

class SongsViewSetTg(viewsets.ModelViewSet):
    def get_queryset(self):
        return Songs.objects.all()

    serializer_class = SongsAlbomSerializersTg