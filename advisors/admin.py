from django.contrib import admin

from .models import Advisor

class AdvisorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25
    
admin.site.register(Advisor, AdvisorAdmin)

