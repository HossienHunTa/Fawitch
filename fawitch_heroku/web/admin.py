from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.ChannelModel)
class ChannelAdmin(admin.ModelAdmin):
    #template = 'panel.html'
    list_display = ['channel','show']
    list_filter = ['show']
    ordering = ['-show','channel']
    search_fields = ['channel']
    
