# -*- coding: utf-8 -*-
import sys
import hashlib, time
from django.shortcuts import render_to_response
from django.template import RequestContext
from chat.models import ResourcesStatuse, Message
from django.http import HttpResponseRedirect
from chat.forms import LoginForm
from django.core.urlresolvers import reverse
from datetime import datetime
from django.http import HttpResponse
from django.utils import simplejson
from django.core.mail import mail_admins
from django.utils.translation import ugettext as _
from chat.xmpp_client import StartXMPPClient

def index(request):
    # Если это авторизованный пользователь
    if request.session.get('session_id', False):
        return HttpResponseRedirect(reverse('chat'))
    # Иначе отправляем на авторизацию
    else:
        return HttpResponseRedirect(reverse('login'))

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            first_name  = form.cleaned_data['first_name']
            last_name   = form.cleaned_data['last_name']
            resource_name = "%s_%s_%s" % (first_name, last_name, datetime.now())
            sess_name  = hashlib.md5(resource_name).hexdigest()
            
            StartXMPPClient(resource_name).start()
            
            # Поиск свободных ресурсов
            all_resources = ResourcesStatuse.objects.filter(status=1)
	    
	    while not all_resources:
		time.sleep(5)
                all_resources = ResourcesStatuse.objects.filter(status=1)
            
            # Проверка наличия свободного ресурса
            if all_resources:
                # Выбор первого попавшегося свободного ресурса
                resource = all_resources[0]
            else:
                return render_to_response('chat/info.html',
                                  { 'content': 'На данный момент все линии заняты. Перезвоните, пожалуйста, позже :)' },
                                  context_instance=RequestContext(request))
            
            # Привязка ресурса к конкретному пользователю
            resource.first_name = first_name
            resource.last_name  = last_name
            # Изменение статуса ресурса на "Занят"
            resource.status     = 3
            # Указание сессии в таблице БД
            resource.sess_name = sess_name
            resource.save()
            
            # Привязка пользователя к ресурсу
            request.session['session_id'] = sess_name
            
            return HttpResponseRedirect(reverse('chat'))
        else:
            return render_to_response('chat/login_form.html',
                                  {'form': form },
                                  context_instance=RequestContext(request))
    
    else:
        form = LoginForm()
        return render_to_response('chat/login_form.html',
                                  {'form': form },
                                  context_instance=RequestContext(request))

def logout(request):
    try:
        session_id  = request.session['session_id']
        try:
            resource    = ResourcesStatuse.objects.get(sess_name=session_id)
            # Удалляем ресурс
            resource.delete()
        except:
            pass
        del request.session['session_id']
    except KeyError:
        pass
    return render_to_response('chat/logout.html',
                                  {},
                                  context_instance=RequestContext(request))

def chat(request):
    if request.session.get('session_id', False):
        return render_to_response('chat/chat.html',
                                  {},
                                  context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect(reverse('login'))

def send(request):
    if request.session.get('session_id', False):
        if request.method == 'POST':
            session_id  = request.session['session_id']
            message     = request.POST['message']
            resource    = ResourcesStatuse.objects.get(sess_name=session_id)
            date_time   = datetime.now()
            Message.objects.create(
                                   resource     = resource,
                                   date_time    = date_time,
                                   message      = message,
                                   direction    = 1
                                   )
            return HttpResponse('Message sended')
        else:
            return HttpResponse('Error sending message')
    else:
        return HttpResponse('Error sending message')

def process(request):
    if request.session.get('session_id', False):
        session_id      = request.session['session_id']
        resource        = ResourcesStatuse.objects.get(sess_name=session_id)
        messages        = Message.objects.filter(resource=resource)
        return render_to_response('chat/messages.html',
                                  { 'resource': resource,
                                    'messages': messages },
                                  context_instance=RequestContext(request))
    else:
        return HttpResponse('Error getting message')
