from django.contrib import admin
from .models import Albom,Artist,SongsAlbom,Songs




admin.site.register([Artist,Albom,SongsAlbom,Songs])

