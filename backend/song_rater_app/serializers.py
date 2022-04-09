from rest_framework import serializers
from .models import User,Song

# The serializer translates a Todo object into a format that
# can be stored in our database. We use the Todo model.
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    # The id is automatically created as a primary key by our Django model
    # and we can included it here as well.
    fields = ('id', 'username','password')

class SongSerializer(serializers.ModelSerializer):
  class Meta:
    model = Song
    fields = ('id','name','artist','rating','ratingNumber')

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