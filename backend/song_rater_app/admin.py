from django.contrib import admin

from .models import User,Song

#class Song_RaterAdmin(admin.ModelAdmin):
#    list_display = ('id','username','song','rating')

# Register your models here.

#admin.site.register(Ratings)
#admin.site.register(Artist)

class SongAdmin(admin.ModelAdmin):
    list_display = ('title','artist','rating')

admin.site.register(User)
admin.site.register(Song)