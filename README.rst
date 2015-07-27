collecting_society.portal.imp
=============================

Plugin for `Web Portal <https://github.com/C3S/collecting_society.portal>`_ 
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


Copyright / License
-------------------

For infos on copyright and licenses, see ``./COPYRIGHT.rst``
