# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal.imp

import logging

from collecting_society_portal.models import Tdb

log = logging.getLogger(__name__)


class CreationUtilisationIMP(Tdb):
    """
    Model wrapper for Tryton model object 'client'
    """

    __name__ = 'creation.utilisation.imp'

    @classmethod
    @Tdb.transaction(readonly=True)
    def search_all(cls):
        """
        Fetches all utilisations of IMP

        Returns:
          list: creation.utilisation.imp
          None: if no match is found
        """
        return cls.get().search([])

    @classmethod
    @Tdb.transaction(readonly=True)
    def search_by_musicfan(cls, web_user_id):
        result = cls.get().search([('client.web_user', '=', web_user_id)])
        return result or None

    @classmethod
    @Tdb.transaction(readonly=True)
    def search_by_musician(cls, party_id):
        Utilisations = cls.get('creation.utilisation')
        result = Utilisations.search([
            'OR',
            ('creation.artist.party', '=', party_id),
            ('creation.artist.solo_artists.party', '=', party_id)
        ])
        return result or None

    @classmethod
    @Tdb.transaction(readonly=False)
    def create(cls, vlist):
        """
        Creates utilisations for IMP

        Args:
          vlist (list): list of dicts with attributes to create utilisations::

            [
                {
                    'client': int (required),
                    'artist': str,
                    'release': str,
                    'title': str,
                    'track_number': str,
                    'duration': str,
                    'time_played': obj DateTime,
                    'fingerprint': str,
                    'fingerprinting_algorithm': str,
                    'fingerprinting_version': str
                },
                {
                    ...
                }
            ]

        Raises:
          KeyError: if required field is missing

        Returns:
          list: created creation.utilisation.imp
          None: if no object was created
        """
        log.debug('create utilisations:\n{}'.format(vlist))
        for values in vlist:
            if 'client' not in values:
                raise KeyError('client is missing')
        result = cls.get().create(vlist)
        return result or None
