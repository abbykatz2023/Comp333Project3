from django.shortcuts import render
from rest_framework import viewsets # We use a viewset.
from .serializers import UserSerializer, SongSerializer, RatingSerializer# Import our serializer file.
from .models import User,Song,Rating #Avg_Rating # Import our Todo model.

# Our Todo view.
class UserView(viewsets.ModelViewSet):
  # Create a new TodoSerializer instance.
  serializer_class = UserSerializer
  # Todo.objects.all() retrieves all the Todo objects in the database.
  queryset = User.objects.all()

class SongView(viewsets.ModelViewSet):
  serializer_class = SongSerializer
  queryset = Song.objects.all()

class RatingView(viewsets.ModelViewSet):
  serializer_class = RatingSerializer
  queryset = Rating.objects.all()

#class Avg_RatingView(viewsets.ModelViewSet):
#  serializer_class = Avg_RatingSerializer
#  queryset = Avg_Rating.objects.all()

'''

class ArtistView(viewsets.ModelViewSet):
  # Create a new TodoSerializer instance.
  serializer_class = ArtistSerializer
  # Todo.objects.all() retrieves all the Todo objects in the database.
  queryset = Artist.objects.all()

class SongView(viewsets.ModelViewSet):
  # Create a new TodoSerializer instance.
  serializer_class = SongSerializer
  # Todo.objects.all() retrieves all the Todo objects in the database.
  queryset = Song.objects.all()

class RatingsView(viewsets.ModelViewSet):
  # Create a new TodoSerializer instance.
  serializer_class = RatingsSerializer
  # Todo.objects.all() retrieves all the Todo objects in the database.
  queryset = Ratings.objects.all()

'''