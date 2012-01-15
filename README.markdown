Djajachat
==================================
Djajachat (Django Ajax Chat) - it is the Open Source Live Chat based on Django and jQuery-XMPP-plugin (https://github.com/maxpowel/jQuery-XMPP-plugin).

License
==================================
This file is part of Djajachat.

Djajachat is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Djajachat is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Djajachat.  If not, see <http://www.gnu.org/licenses/>.


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
