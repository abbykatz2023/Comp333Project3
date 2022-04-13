from tkinter import CASCADE
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg, Max, Min, Sum

# Create your models here.

from django.db import models


class User(models.Model):
    def __str__(self):
        return self.username
    username = models.CharField(max_length=200, primary_key=True)
    password = models.CharField(max_length=200)


# class Song(models.Model):
#     def __str__(self):
#         return str(str(self.name) + " by " + str(self.artist) + "with rating" + str(self.rating_avg))
#         # return self.song
#     name = models.CharField(max_length=200, primary_key=True)
#     artist = models.CharField(max_length= 200)
#     rating_avg = Rating.objects.filter()
#     #rating = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
#     #ratingNumber = models.PositiveIntegerField()

class Song(models.Model):
    def __str__(self):
        return str(str(self.name) + " by " + str(self.artist))
        # return self.song
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length= 200)
    # def number_of_songs(self): 
    #     rating_list = Rating.obects.filter(song = self)
    #     return len(rating_list)
    # def average_rating(self):
    #     rating_list = Rating.objects.filter(song= self)
    #     sum=0
    #     for i in rating_list:
    #         sum+= i.rating
    #     if len(rating_list) > 0:
    #         return sum / len(rating_list)
    #     else:
    #         return 0
        

    #rating= models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #avg_ratings = Rating.objects.all().values('song').order_by('song').annotate(rating_average=Avg('rating'))

    #rating_avg = Rating.objects.filter().aggregate(Avg('rating'))

class Rating(models.Model):
    def __str__(self):
        return str(self.song)+ " by user " +str(self.user) + "with rating" + str(self.rating)
    song=models.ForeignKey(Song, on_delete=models.CASCADE)
    rating= models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# class Avg_Rating(models.Model):
#     def __str__(self):
#         return str(self.rating)
#     song=models.ForeignKey(Song, on_delete=models.CASCADE)
#     avg_rating = Rating.objects.filter(song = Rating.song).aggregate(Avg('rating'))



# class Song(models.Model):
#     def __str__(self):
#         return str(str(self.name) + " by " + str(self.artist) + "with rating" + str(self.rating_avg))
#         # return self.song
#     name = models.CharField(max_length=200, primary_key=True)
#     artist = models.CharField(max_length= 200)
#     rating_avg = Rating.objects.filter().aggregate(Avg('rating'))


# class Artist(models.Model):
#     def __str__(self):
#         return self.artist
#     artist = models.CharField(max_length = 200,primary_key=True)
#     hometown = models.CharField(max_length = 200)
#     age = models.PositiveIntegerField()

# class Song(models.Model):
#     def __str__(self):
#         return str(str(self.song) + " by " + str(self.artist) + " in genre " + str(self.genre))
#         # return self.song
#     song = models.CharField(max_length=200, primary_key=True)
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
#     genre = models.CharField(max_length=200)

# class Ratings(models.Model):
#     def __str__(self):
#         return str(str(self.song.song) + " by " + str(self.song.artist) + " - " + str(self.rating))
#     id = models.AutoField(primary_key=True)
#     username = models.ForeignKey(User,on_delete = models.CASCADE)  #models.CharField(max_length=200)
#     song = models.ForeignKey(Song,on_delete = models.CASCADE)  #models.CharField(max_length=200)
#     rating= models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])

