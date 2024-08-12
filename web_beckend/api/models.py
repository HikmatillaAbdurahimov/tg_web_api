from django.db import models
from .helpers import SaveMediaFiles

class Artist(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    image=models.URLField()
    nick_name=models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['id']

    def __str__(self):
        return self.nick_name

class Albom(models.Model):
    title=models.CharField(max_length=50)
    image=models.URLField()
    description=models.TextField()
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['id']

    def __str__(self):
        pass

class Songs(models.Model):
    title=models.CharField(max_length=50)
    description = models.TextField()
    image = models.URLField()
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE)

    class Meta:
        ordering=['id']

    def __str__(self):
        pass

class SongsAlbom(models.Model):
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE)
    songs=models.ManyToManyField(Songs)


