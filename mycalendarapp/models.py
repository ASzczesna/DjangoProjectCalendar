# coding: utf-8

from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100, verbose_name=_(u'Tytuł'), default=_(u'Tytuł wydarzenia'))
    desc = models.TextField(max_length=500, verbose_name=_(u'Opis'), default=_(u'Opis wydarzenia'), null=True, blank=True)
    created = models.DateTimeField(verbose_name=_(u'Czas'), default=timezone.now)
    place = models.CharField(max_length=100, verbose_name=_(u'Miejsce'), default=_(u'Tytuł wydarzenia'))

    time_begin = models.DateTimeField(verbose_name=_(u'Początek'), default=timezone.now)
    time_end = models.DateTimeField(verbose_name=_(u'Koniec'), default=timezone.now)

    date_begin = models.DateTimeField(verbose_name=_(u'Początek'), default=timezone.now)
    date_end = models.DateTimeField(verbose_name=_(u'Koniec'), default=timezone.now)

    repeat_shift = models.IntegerField(verbose_name=_(u'Powtarzane co'), default=0)