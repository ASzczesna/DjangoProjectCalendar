from django.contrib import admin

# Register your models here.
from mycalendarapp.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = 
    pass