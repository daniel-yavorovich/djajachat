# -*- coding: utf-8 -*-
from django.db import models

RESOURCE_STATUSES_CHOICES = (
    (1, 'Online'),
    (2, 'Offline'),
    (3, 'Basy')
)

DIRECTIONS_CHOICES = (
    (1, 'Me'),
    (2, 'Admin'),
)

MESSAGE_STATUSES_CHOICES = (
    (1, 'Доставлено'),
    (2, 'Недоставлено'),
)

class ResourcesStatuse(models.Model):
    name        = models.CharField('Имя Jabber ресурсы', max_length=100)
    status      = models.IntegerField('Статус ресурса', max_length=1, choices=RESOURCE_STATUSES_CHOICES)
    first_name  = models.CharField('Имя', max_length=100, null=True, blank=True, unique=False)
    last_name   = models.CharField('Фамилия', max_length=100, null=True, blank=True, unique=False)
    sess_name   = models.CharField('Имя сессии чата', max_length=100, null=True, blank=True, unique=False)
    
    def __unicode__(self):
        return self.name

class Message(models.Model):
    resource    = models.ForeignKey('ResourcesStatuse')
    date_time   = models.DateTimeField('Время сообщения')
    message     = models.TextField('Текст сообщения')
    direction   = models.IntegerField('Направление сообщения', max_length=1, choices=DIRECTIONS_CHOICES)
    status      = models.IntegerField('Статус доставки', max_length=1, choices=MESSAGE_STATUSES_CHOICES, default=2)
    
    def __unicode__(self):
        return self.message