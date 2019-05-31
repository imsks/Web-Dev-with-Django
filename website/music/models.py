from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length = 250)
    albumTitle = models.CharField(max_length = 500)
    genre = models.CharField(max_length = 100)
    albumLogo = models.CharField(max_length = 1000)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    fileType = models.CharField(max_length = 10)
    songTitle = models.CharField(max_length = 250)