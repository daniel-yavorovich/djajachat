# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from chat.forms import LoginForm
from django.conf import settings

def chat(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            first_name  = form.cleaned_data['first_name']
            last_name   = form.cleaned_data['last_name']
            
            request.session['first_name']   = first_name
            request.session['last_name']    = last_name
            request.session['is_login']     = True
            
            return render_to_response('chat/chat.html',
                                  {
                                   'first_name': first_name,
                                   'last_name': last_name,
                                   'jabber_id': settings.JABBER_ID,
                                   'jabber_pass': settings.JABBER_PASSWORD,
                                   'jabber_recipient': settings.JABBER_RECIPIENT,
                                   'http_bind': settings.JABBER_HTTP_BIND_URL,
                                   },
                                  context_instance=RequestContext(request))
        else:
            return render_to_response('chat/login_form.html',
                                  {'form': form },
                                  context_instance=RequestContext(request))
    
    else:
        if request.session.get('is_login', False):
            first_name  = request.session.get('first_name', False)
            last_name   = request.session.get('last_name', False)
            
            return render_to_response('chat/chat.html',
                                  {
                                   'first_name': first_name,
                                   'last_name': last_name,
                                   'jabber_id': settings.JABBER_ID,
                                   'jabber_pass': settings.JABBER_PASSWORD,
                                   'jabber_recipient': settings.JABBER_RECIPIENT,
                                   'http_bind': settings.JABBER_HTTP_BIND_URL,
                                   },
                                  context_instance=RequestContext(request))
        else:
            form = LoginForm()
            return render_to_response('chat/login_form.html',
                                      {'form': form },
                                      context_instance=RequestContext(request))

def logout(request):
    del request.session['is_login']
    del request.session['first_name']
    del request.session['last_name']
    return render_to_response('chat/logout.html',
                              {},
                              context_instance=RequestContext(request))