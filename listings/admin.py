from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'parking', 'dist_to_bus_stop', 'nearestuni')
    list_display_links = ('id', 'title')
    list_filter = ('advisor', 'nearestuni', 'price')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'nearestuni', 'postcode', 'price')
    list_per_page = 25
admin.site.register(Listing, ListingAdmin)
