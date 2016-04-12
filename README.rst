collecting_society.portal.imp
=============================

Plugin for `Web Portal <https://github.com/C3S/collecting_society.portal.imp>`_ 
including:

- IMP web frontend
- Musician
- Musicfan
- Client API

For a working development setup, see https://github.com/C3S/c3s.ado


IMP web frontend
----------------

IMP ("Integration of micropayment within the context of a collecting society")
is a system, in which musicfans are able to donate micro amounts to musicians 
("out of the pocket of musicfans into the hat of musicians") by monitoring their
music player ("clients") via plugin and distributing their monthly budget to
all musicians involved in creation and performance of the track, they have
listened to ("utilisazion").

This plugin includes the web frontend part of this system.


Musician
--------

Enables artists to manage their hat and to view the list of their creations,
musicfans had listened to.


Musicfan
--------

Enables web users to manage their pocket, to manage their clients and to view
the list of creations, they have listened to.


Client API
----------

Includes an API for registering new clients and for recieving new utilisations.


Translations
------------

Explanation
```````````
- **.pot**: "Portable Object Template" file, list of message identifiers, template for **.po** files
- **.po**: "Portable Object" file, human editable list of translated messages
- **.mo**: "Machine Object" file, machine readable list of messages, created from a **.po** file

Installation
````````````
- **poedit**: ``$apt-get install poedit``
- **gettext**: ``$apt-get install gettext``
- **lingua**: ``$pip install lingua``

**Note**: If you are running different python versions on the host, you need to ensure, that the right ``pip`` (e.g. ``pip2.7``) is called.

Updates
```````

e.g. for project **collecting_society.portal.imp** and language **de**

- only once, to start translation of a project, create the **.pot** file for the project
    - ``$cd c3s.ado/ado/src/collecting_society.portal.imp``
    - ``$mkdir collecting_society_portal_imp/locale``
    - ``$pot-create -o collecting_society_portal_imp/locale/collecting_society_portal_imp.pot collecting_society_portal_imp``
- only once, if you need a new language, create the **.po** file for the language
    - ``$cd c3s.ado/ado/src/collecting_society.portal.imp/collecting_society_portal_imp/locale``
    - ``$mkdir -p de/LC_MESSAGES``
    - ``$msginit -l de -o de/LC_MESSAGES/collecting_society_portal_imp.po``
- each time, the code or templates changed, recreate the **.pot** file:
    - ``$cd c3s.ado/ado/src/collecting_society.portal.imp``
    - ``$pot-create -o collecting_society_portal_imp/locale/collecting_society_portal_imp.pot collecting_society_portal_imp``
- every time the **.pot** file changed, recreate the **.po** files for all languages
    - ``$cd c3s.ado/ado/src/collecting_society.portal.imp``
    - ``$msgmerge --update collecting_society_portal_imp/locale/*/LC_MESSAGES/collecting_society_portal_imp.po collecting_society_portal_imp/locale/collecting_society_portal_imp.pot``
- to edit translations, change the **.po** file via poedit
    - ``$cd c3s.ado/ado/src/collecting_society.portal.imp``
    - ``$poedit collecting_society_portal_imp/locale/de/LC_MESSAGES/collecting_society_portal_imp.po``
- every time the **.po** file changed, create a **.mo** file
    - ``$cd c3s.ado/ado/src/collecting_society.portal.imp``
    - ``$msgfmt -o collecting_society_portal_imp/locale/de/LC_MESSAGES/collecting_society_portal_imp.mo collecting_society_portal_imp/locale/de/LC_MESSAGES/collecting_society_portal_imp.po``

Further information
```````````````````

- see `pyramid documentation <http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/i18n.html#working-with-gettext-translation-files>`_


Copyright / License
-------------------

For infos on copyright and licenses, see ``./COPYRIGHT.rst``
