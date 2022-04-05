from django.contrib import admin

from .models import Ratings,Artist,User,Song

#class Song_RaterAdmin(admin.ModelAdmin):
#    list_display = ('id','username','song','rating')

# Register your models here.

admin.site.register(Ratings)
admin.site.register(Artist)
admin.site.register(User)
admin.site.register(Song)