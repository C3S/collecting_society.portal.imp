# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal.imp

import logging

from collecting_society_portal.models import Tdb

log = logging.getLogger(__name__)


class Client(Tdb):
    """
    Model wrapper for Tryton model object 'client'
    """

    __name__ = 'client'

    @classmethod
    @Tdb.transaction(readonly=True)
    def search_all(cls, active=True):
        """
        Fetches all clients

        Returns:
          list: client
          None: if no match is found
        """
        return cls.get().search([('active', 'in', (True, active))])

    @classmethod
    @Tdb.transaction(readonly=True)
    def search_by_uuid(cls, uuid, active=True):
        """
        Searches a client by uuid

        Args:
          uuid (string): uuid of client

        Returns:
          obj: client
          None: if no match is found
        """
        result = cls.get().search([
            ('uuid', '=', uuid),
            ('active', 'in', (True, active))
        ])
        return result[0] if result else None

    @classmethod
    @Tdb.transaction(readonly=True)
    def search_by_web_user(cls, web_user_id, active=True):
        """
        Searches a client by web_user id

        Args:
          web_user_id (int): web.user.id

        Returns:
          list: clients of web_user
          None: if no match is found
        """
        return cls.get().search([
            ('web_user', '=', web_user_id),
            ('active', 'in', (True, active))
        ])

    @classmethod
    @Tdb.transaction(readonly=True)
    def get_player_names_by_web_user(cls, web_user):
        """
        Fetches all distinct player names for a web_user

        Args:
          web_user (obj): web.user

        Returns:
          set: player names
          None: if no match is found
        """
        player_names = set()
        clients = cls.search_by_web_user(web_user)
        [player_names.add(client.player_name) or client
         for client in clients
         if client.player_name not in player_names]
        return sorted(player_names)

    @classmethod
    @Tdb.transaction(readonly=False)
    def disable(cls, client):
        """
        Disables client

        Args:
          client (obj): client
        """
        client.active = False
        client.save()

    @classmethod
    @Tdb.transaction(readonly=False)
    def delete(cls, client):
        """
        Deletes client

        Args:
          client (list): clients::

            [client1, client2, ...]

        Returns:
          ?
        """
        return cls.get().delete(client)

    @classmethod
    @Tdb.transaction(readonly=False)
    def create(cls, vlist):
        """
        Creates clients

        Args:
          vlist (list): list of dicts with attributes to create clients::

            [
                {
                    'web_user': web.user (required),
                    'uuid': str (required),
                    'player_name': str (required),
                    'player_version': str,
                    'plugin_name': str,
                    'plugin_version': str,
                    'plugin_vendor': str,
                    'active': bool
                },
                {
                    ...
                }
            ]

        Raises:
          KeyError: if required field is missing

        Returns:
          list: created client
          None: if no object was created
        """
        log.debug('create clients:\n{}'.format(vlist))
        for values in vlist:
            if 'web_user' not in values:
                raise KeyError('web_user is missing')
            if 'uuid' not in values:
                raise KeyError('uuid is missing')
            if 'player_name' not in values:
                raise KeyError('player_name is missing')
        result = cls.get().create(vlist)
        return result or None
