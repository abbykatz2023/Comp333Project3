"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# We use include for routing to our URLs.
from django.urls import path, include
# The Django REST Framework comes with a router.
# We can use it to route users to our API.
from rest_framework import routers
from song_rater_app import views

# Create a new router.
router = routers.DefaultRouter()
# Register our TodoView for use under the /todos path (first argument).
# r indicates a raw string in Python meaning that characters like '\' are escaped.
# Reference to our TodoView (second argument).
# The basename 'todo' for use in our code (third argument)
# https://stackoverflow.com/questions/22083090/what-base-name-parameter-do-i-need-in-my-route-to-make-this-django-api-work
# For more info see: https://www.django-rest-framework.org/api-guide/routers/
router.register(r'user', views.UserView, 'user')
#router.register(r'artist', views.ArtistView, 'artist')
router.register(r'song', views.SongView, 'song')
#router.register(r'ratings', views.RatingsView, 'ratings')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]