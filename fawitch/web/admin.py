from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.ChannelModel)
class ChannelAdmin(admin.ModelAdmin):
    pass
