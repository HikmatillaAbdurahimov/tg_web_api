from django.urls import path,include
from .views import ArtistViewSetWeb,AlbomViewSetWeb,SongsViewSetWeb
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'artists_web',ArtistViewSetWeb,basename='artists_web')
router.register(r'albom_web',ArtistViewSetWeb,basename='albom_web')
router.register(r'songs_web',ArtistViewSetWeb,basename='songs_web')

urlpatterns=[
    path('',include(router.urls)),
    ]
