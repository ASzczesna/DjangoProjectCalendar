# coding: utf-8

from __future__ import unicode_literals

from datetime import date, time

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


# Create your models here.
# przesunięcie godzinne, ale działa tylko dla DateTimeField:
# def hour_shift():
#     return timezone.now() + timezone.timedelta(hours=1)


# class ConvertingDateTimeField(models.DateTimeField):
#     def get_prep_value(self, value):
#         return str(datetime.strptime(value, '%d.%m.%Y %H:%M'))


class Event(models.Model):
    # na potrzeby bardziej zrozumiałego wyświetlania:
    class Meta:
        verbose_name = 'wydarzenie'
        verbose_name_plural = 'wydarzenia'

    name = models.CharField(max_length=100, verbose_name=_(u'Tytuł'))
    desc = models.TextField(max_length=500, verbose_name=_(u'Opis'), null=True, blank=True)
    created = models.DateTimeField(verbose_name=_(u'Czas'), default=timezone.now)
    place = models.CharField(max_length=100, verbose_name=_(u'Miejsce'))

    time_begin = models.TimeField(verbose_name=_(u'Od'))
    time_end = models.TimeField(verbose_name=_(u'Do'))

    repeat_me = models.BooleanField(verbose_name=_(u'Powtarzanie'), default=False)

    date_begin = models.DateField(verbose_name=_(u'Data'), default=timezone.now)
    date_end = models.DateField(verbose_name=_(u'Data zakończenia'), default=timezone.now)

    repeat_shift = models.IntegerField(verbose_name=_(u'Powtarzane co'), default=0)

    def is_past(self):
        if date.today() > self.date_end and time.hour > self.time_end.hour:
            return True
        return False
