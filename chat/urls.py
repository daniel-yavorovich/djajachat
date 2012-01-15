# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('chat.views',
    url(r'^$', 'chat', name='chat'),
    url(r'^logout/$', 'logout', name='chat_logout'),
)
