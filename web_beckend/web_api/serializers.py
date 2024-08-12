from rest_framework import serializers
from api.models import Artist,Albom,Songs,SongsAlbom



class ArtistSerializersWeb(serializers.ModelSerializer):
    class Meta:
        model=Artist
        fields=('id','first_name','last_name','nick_name','image')


class AlbomSerializersWeb(serializers.ModelSerializer):
    class Meta:
        model=Albom
        fields=('id','artist','description','title')


class SongsSerializersWeb(serializers.ModelSerializer):
    class Meta:
        model=Songs
        fields=('id','artist','title','description')

class SongsAlbomSerializersWeb(serializers.ModelSerializer):
    class Meta:
        model=SongsAlbom
        fields=('id','songs','artist')





