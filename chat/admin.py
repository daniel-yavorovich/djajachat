# -*- coding: utf-8 -*-
from django.contrib import admin
from chat.models import ResourcesStatuse, Message

class ResourcesStatuseAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'first_name', 'last_name')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('resource', 'date_time', 'direction', 'status')

admin.site.register(ResourcesStatuse, ResourcesStatuseAdmin)
admin.site.register(Message, MessageAdmin)