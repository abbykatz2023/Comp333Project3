from rest_framework import serializers
from .models import Rating, User,Song #Avg_Rating

# The serializer translates a Todo object into a format that
# can be stored in our database. We use the Todo model.
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    # The id is automatically created as a primary key by our Django model
    # and we can included it here as well.
    fields = ('username','password')

class SongSerializer(serializers.ModelSerializer):
  class Meta:
    model = Song
    fields = ('id','name','artist') #MAYBE ADD 'id', AT THE BEGINNNING

class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rating
    fields = ('id','song','rating','user')

#class Avg_RatingSerializer(serializers.ModelSerializer):
#  class Meta:
#    model = Avg_Rating
#    fields = ('id','song','avg_rating')
'''
class ArtistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artist
    # The id is automatically created as a primary key by our Django model
    # and we can included it here as well.
    fields = ('id', 'artist','hometown','age')

class SongSerializer(serializers.ModelSerializer):
  class Meta:
    model = Song
    # The id is automatically created as a primary key by our Django model
    # and we can included it here as well.
    fields = ('id', 'song','artist','genre')

class RatingsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ratings
    # The id is automatically created as a primary key by our Django model
    # and we can included it here as well.
    fields = ('id', 'username','song','rating')
  
'''