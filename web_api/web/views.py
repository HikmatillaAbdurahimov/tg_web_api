from django.shortcuts import render
from django.views import  View
import requests

class HomeView(View):
    def get(self,request):
        return render(request,'home.html')

class ArtistView(View):
    def get(self,request):
        artists=requests.get("http://127.0.0.1:8002/web_api/artists_web/").json()
        context={
            "artists":artists
        }
        return render(request,'artist.html',context)

class AlbomView(View):
    def get(self,request):
        albom=requests.get("http://127.0.0.1:8002/web_api/albom_web/").json()
        context = {
            "albom": albom
        }
        return render(request,'albom.html',context)

class SongsView(View):
    def get(self,request):
        songs=requests.get("http://127.0.0.1:8002/web_api/songs_web/").json()
        context = {
            "songs": songs
        }
        return render(request,'songs.html',context)