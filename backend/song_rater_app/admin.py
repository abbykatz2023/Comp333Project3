from django.contrib import admin

from .models import User,Song, Rating  #Avg_Rating

#class Song_RaterAdmin(admin.ModelAdmin):
#    list_display = ('id','username','song','rating')

# Register your models here.

#admin.site.register(Ratings)
#admin.site.register(Artist)

class SongAdmin(admin.ModelAdmin):
    list_display = ('title','artist','rating')

admin.site.register(User)
admin.site.register(Song)
admin.site.register(Rating)
#admin.site.register(Avg_Rating)