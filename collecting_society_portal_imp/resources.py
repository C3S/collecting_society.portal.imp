# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal.imp

import logging

from collecting_society_portal.services import _
from collecting_society_portal.resources import (
    ResourceBase,
    FrontendResource,
    BackendResource
)
from collecting_society_portal.views.widgets import news_widget
from collecting_society_portal_creative.resources import (
    ArtistResource,
    AddArtistResource,
    CreationResource
)
from .views.widgets import (
    plugins_widget,
    todo_musician_widget,
    todo_musicfan_widget,
    pocket_widget
)

log = logging.getLogger(__name__)


def include_web_resources(config):

    # Frontend
    FrontendResource.add_child(MusicfanDummyResource)
    MusicfanDummyResource.add_child(ClientResource)

    # Backend
    BackendResource.add_child(MusicfanResource)
    BackendResource.add_child(MusicianResource)

    @BackendResource.extend_registry
    def register_roles(self):
        reg = self.dict()
        # menue roles
        reg['menues']['roles'] = [
            {
                'name': _(u'Musicfan'),
                'active': MusicfanResource,
                'url': self.request.resource_path(
                    MusicfanResource(self.request), ''
                )
            },
            {
                'name': _(u'Musician'),
                'active': MusicianResource,
                'url': self.request.resource_path(
                    MusicianResource(self.request), ''
                )
            }
        ]
        return reg

    # Musicfan
    MusicfanResource.add_child(ClientResource)
    MusicfanResource.add_child(UtilisationIMPMusicfanResource)

    # Musician
    MusicianResource.add_child(ArtistResource)
    ArtistResource.add_child(AddArtistResource)
    MusicianResource.add_child(CreationResource)
    MusicianResource.add_child(UtilisationIMPMusicianResource)


class MusicfanResource(ResourceBase):
    __name__ = "musicfan"
    __parent__ = BackendResource
    __children__ = {}
    __acl__ = []

    @property
    def __registry__(self):
        reg = self.dict()
        # css
        reg['static']['css'] = [
            self.request.static_path(
                'collecting_society_portal_imp:static/css/backend.css'
            )
        ]
        # logo
        reg['static']['logo'] = self.request.static_path(
            'collecting_society_portal_imp:static/img/musicfan/logo.png'
        )
        # menue main
        reg['menues']['main'] = [
            {
                'name': _(u'Dashboard'),
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/icon.png'
                ),
                'url': self.request.resource_path(
                    MusicfanResource(self.request), 'dashboard'
                )
            },
            {
                'name': _(u'Clients'),
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/icon.png'
                ),
                'url': self.request.resource_path(
                    ClientResource(self.request), 'list'
                )
            },
            {
                'name': _(u'Music Utilization'),
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/icon.png'
                ),
                'url': self.request.resource_path(
                    UtilisationIMPMusicfanResource(self.request), 'list'
                )
            },
            {
                'name': _(u'My Account'),
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/icon.png'
                ),
                'url': None
            },
            {
                'name': _(u'News'),
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/icon.png'
                ),
                'url': None
            },
            {
                'name': _(u'Contact'),
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/icon.png'
                ),
                'url': None
            },
            {
                'name': _(u'Settings'),
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/icon.png'
                ),
                'url': None
            }
        ]
        # widgets content-right
        reg['widgets']['content-right'] = [
            news_widget,
            # pocket_widget,
            plugins_widget,
            todo_musician_widget
        ]
        return reg


class MusicianResource(ResourceBase):
    __name__ = "musician"
    __parent__ = BackendResource
    __children__ = {}
    __acl__ = []

    @property
    def __registry__(self):
        reg = self.dict()
        # css
        reg['static']['css'] = [
            self.request.static_path(
                'collecting_society_portal_imp:static/css/backend.css'
            )
        ]
        # logo
        reg['static']['logo'] = self.request.static_path(
            'collecting_society_portal_imp:static/img/musicfan/logo.png'
        )
        # menue main
        reg['menues']['main'] = [
            {
                'name': _(u'Dashboard'),
                'url': self.request.resource_path(
                    MusicianResource(self.request), 'dashboard'
                ),
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/icon.png'
                )
            },
            {
                'name': _(u'My Artists'),
                'url': self.request.resource_path(
                    ArtistResource(self.request), ''
                ),
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/icon.png'
                )
            },
            {
                'name': _(u'My Creations'),
                'url': self.request.resource_path(
                    CreationResource(self.request), ''
                ),
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/icon.png'
                )
            },
            {
                'name': _(u'Music Utilisation'),
                'url': self.request.resource_path(
                    UtilisationIMPMusicianResource(self.request), 'list'
                ),
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/icon.png'
                )
            },
            {
                'name': _(u'My Account'),
                'url': None,
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/icon.png'
                )
            },
            {
                'name': _(u'News'),
                'url': None,
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/icon.png'
                )
            },
            {
                'name': _(u'Contact'),
                'url': None,
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/icon.png'
                )
            },
            {
                'name': _(u'Settings'),
                'url': None,
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/icon.png'
                )
            }
        ]
        # widgets content-right
        reg['widgets']['content-right'] = [
            news_widget,
            todo_musicfan_widget
        ]
        return reg


class MusicfanDummyResource(ResourceBase):
    __name__ = "musicfan"
    __parent__ = MusicfanResource


class ClientResource(ResourceBase):
    __name__ = "clients"
    __parent__ = MusicfanResource
    __children__ = {}
    __registry__ = {}
    __acl__ = []


class UtilisationIMPMusicfanResource(ResourceBase):
    __name__ = "utilisations"
    __parent__ = MusicfanResource
    __children__ = {}
    __registry__ = {}
    __acl__ = []


class UtilisationIMPMusicianResource(ResourceBase):
    __name__ = "utilisations"
    __parent__ = MusicianResource
    __children__ = {}
    __registry__ = {}
    __acl__ = []
