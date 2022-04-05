from tkinter import CASCADE
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

from django.db import models


class User(models.Model):
    def __str__(self):
        return self.username
    username = models.CharField(max_length=200, primary_key=True)
    password = models.CharField(max_length=200)

class Artist(models.Model):
    def __str__(self):
        return self.artist
    artist = models.CharField(max_length = 200,primary_key=True)
    hometown = models.CharField(max_length = 200)
    age = models.PositiveIntegerField()

class Song(models.Model):
    def __str__(self):
        return str(str(self.song) + " by " + str(self.artist) + " in genre " + str(self.genre))
        # return self.song
    song = models.CharField(max_length=200, primary_key=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.CharField(max_length=200)

class Ratings(models.Model):
    def __str__(self):
        return str(str(self.song.song) + " by " + str(self.song.artist) + " - " + str(self.rating))
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User,on_delete = models.CASCADE)  #models.CharField(max_length=200)
    song = models.ForeignKey(Song,on_delete = models.CASCADE)  #models.CharField(max_length=200)
    rating= models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])