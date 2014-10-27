from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Restaurant, Food, Town

class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [('Description', {'fields':['name', 'desc', 'menu']}),
                 ('Address', {'fields':['address', 'postcode', 'town']}),
                 ('Contact', {'fields':['web', 'gmap_url', 'phone']}),
                 ('Food', {'fields':['food']}),
                 ('Pictures', {'fields':['picture', 'map']}),
                 ]

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food)
admin.site.register(Town)
