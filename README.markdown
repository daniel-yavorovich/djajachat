Djajachat
==================================
Djajachat (Django Ajax Chat) - it is the Open Source chat based on Django and jQuery-XMPP-plugin (https://github.com/maxpowel/jQuery-XMPP-plugin)

Requirements
-----------
* jQuery: http://jquery.com/
* jQuery-XMPP-plugin: https://github.com/maxpowel/jQuery-XMPP-plugin
* jQuery form: http://jquery.malsup.com/form/
* Django: https://www.djangoproject.com/
* Django sessions: https://docs.djangoproject.com/en/dev/topics/http/sessions/

Usage
==========

* Download /static/* content into your Static Directory.

* Download 'chat' directory into your project.

* Add 'chat' into you INSTALLED_APPS.

* Modify your urls.py. Example:

        url(r'^djajachat/', include('chat.urls')),

* Restart your Django Project.
