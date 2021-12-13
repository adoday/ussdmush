from django.contrib import admin
from .models import * #import all models
# Register your models here.

class MushroomAdmin (admin.ModelAdmin):
    list_display =['phoneNumber', 'names']
    search_fields =['phoneNumber']

class AmakuruyibihumyoAdmin (admin.ModelAdmin):
    list_display =['phone_number' , 'category']
    search_fields =['phone_number' , 'category']

admin.site.register(Mushroom, MushroomuserAdmin)

admin.site.register(Amakuruyibihumyo, AmakuruyibihumyoAdmin)

