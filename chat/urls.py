# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('chat.views',
    url(r'^login/', 'login', name='login'),
    url(r'^logout/', 'logout', name='logout'),
    url(r'^chat/send/', 'send', name='send'),
    url(r'^chat/process/', 'process', name='process'),
    url(r'^chat/', 'chat', name='chat'),
    url(r'^$', 'index', name='djajachat'),
)
