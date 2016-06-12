# coding: utf-8
from django.contrib import admin
# Register your models here.
from mycalendarapp.models import Event

#zarejestrowanie danego modelu by był widoczny w adminie:
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # wszystkie pola:
    #['name', 'desc', 'place', 'time_begin', 'time_end', 'repeat_me', 'date_begin', 'date_end', 'repeat_shift']

    # elementy widoczne w kolumnach tabeli (domyślnie pierwsza wyświetla linki):
    list_display = ['name', 'place', 'time_begin', 'time_end', 'date_begin', 'date_end',  'repeat_me']
    list_filter = ['place', 'repeat_me']
    search_fields = ['name', 'place', 'desc']

    # kiedy data i godzina zakończenia miną, można edtyować tylko trzy elementy
    def get_fields(self, request, obj=Event):
        # if obj.is_past:
        #     return ['name', 'desc', 'place']
        return ['name', 'desc', 'place', 'time_begin', 'time_end', 'repeat_me', 'date_begin', 'date_end', 'repeat_shift']

    def get_readonly_fields(self, request, obj=None):
        if obj.is_past:
            return ['time_begin', 'time_end', 'repeat_me', 'date_begin', 'date_end', 'repeat_shift']
        #nie jest przeszłe - nie ma pól readOnly:
        return []
