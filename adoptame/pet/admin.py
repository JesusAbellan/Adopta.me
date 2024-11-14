from django.contrib import admin

from .models import Specie, Pet, Race

admin.site.register(Specie)
admin.site.register(Race)
admin.site.register(Pet)
