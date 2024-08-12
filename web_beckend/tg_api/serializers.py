from rest_framework import serializers
from api.models import Artist,Albom,Songs,SongsAlbom



class ArtistSerializersTg(serializers.ModelSerializer):
    class Meta:
        model=Artist
        fields=('first_name','last_name','nick_name')


class AlbomSerializersTg(serializers.ModelSerializer):
    class Meta:
        model=Albom
        fields=('artist','title')


class SongsSerializersTg(serializers.ModelSerializer):
    class Meta:
        model=Songs
        fields=('artist','title')

class SongsAlbomSerializersTg(serializers.ModelSerializer):
    class Meta:
        model=SongsAlbom
        fields=('id','songs','artist')

