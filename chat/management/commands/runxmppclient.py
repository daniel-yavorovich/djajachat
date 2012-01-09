# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
import sys, xmpp, time
from chat.xmpp_client import presenceCB, messageCB
from django.conf import settings
from chat.models import ResourcesStatuse, Message

class Command(BaseCommand):
    args = '<jabber_resource_name>'
    help = 'Run jabber client'

    def handle(self, *args, **options):
        if args:
            try:
                jabber_resource = args[0]
                jid=xmpp.JID(settings.JABBER_ID)
                user, server, password=jid.getNode(), jid.getDomain(), settings.JABBER_PASSWORD
            
                conn=xmpp.Client(server,debug=[])
                conres=conn.connect()
                if not conres:
                    print "Unable to connect to server %s!"%server
                    sys.exit(1)
                if conres<>'tls':
                    print "Warning: unable to establish secure connection - TLS failed!"
                authres=conn.auth(user, password, jabber_resource)
                if not authres:
                    print "Unable to authorize on %s - check login/password." % server
                    sys.exit(1)
                if authres <> 'sasl':
                    print "Warning: unable to perform SASL auth os %s. Old authentication method used!" % server
                conn.RegisterHandler('message', messageCB)
                conn.RegisterHandler('presence', presenceCB)
                conn.sendInitPresence()
                
                try:
                    resource        = ResourcesStatuse.objects.get(name=jabber_resource)
                    resource.status = 1
                    resource.save()
                except:
                    resource = ResourcesStatuse.objects.create(name=jabber_resource, status=1)
                
                self.stdout.write('XMPP client started for resource "%s" successfully\n' % jabber_resource)
                
                while resource.status != 2:
                    conn.Process(1)
                    # Проверка активности соединения
                    if not conn.isConnected():
                        conn.reconnectAndReauth()
                    # Проверка активности ресурса
                    ResourcesStatuse.objects.update()
                    resource = ResourcesStatuse.objects.get(name=jabber_resource)
                    # Поиск и если это нужно - отправка непрочитанных сообщений для администратора в этом ресурсе
                    messages_to_admin = Message.objects.filter(resource=resource).filter(direction=1).filter(status=2)
                    for message in messages_to_admin:
                        m = xmpp.protocol.Message(to=settings.JABBER_RECIPIENT, body=message, typ='chat')
                        conn.send(m)
                        message.status=1
                        message.save()
                else:
                    resource.status=2
                    resource.save()
                    self.stdout.write('XMPP client stopped for resource "%s" successfully\n' % jabber_resource)
            except:
                self.stdout.write('ERROR starting XMPP client!\n')
                raise
        else:
            self.stdout.write('Please run "manage.py runxmppclient -help"\n')