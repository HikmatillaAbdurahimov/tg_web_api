from django.urls import path,include
from .views import ArtistViewSetTg,AlbomViewSetTg,SongsViewSetTg
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'artists_tg',ArtistViewSetTg,basename='artists_tg')
router.register(r'albom_tg',AlbomViewSetTg,basename='albom_tg')
router.register(r'songs_tg',SongsViewSetTg,basename='songs_tg')

urlpatterns=[
    path('',include(router.urls)),
    ]