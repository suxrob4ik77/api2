from django.contrib import admin

from configapp.models import Movie,Actors

# Register your models here.
admin.site.register(Movie)
admin.site.register(Actors)