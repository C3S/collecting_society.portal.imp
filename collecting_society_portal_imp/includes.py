# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal.imp

"""
Functions to include resources/views and register content by the plugin system.

The following functions are called by convention on app creation:

- web_resources
- web_registry
- web_views
- api_views
"""

from collections import OrderedDict

from collecting_society_portal.views.widgets import news_widget
from collecting_society_portal.resources import (
    FrontendResource,
    BackendResource,
    NewsResource
)

from collecting_society_portal_creative.resources import (
    ArtistResource,
    AddArtistResource,
    CreationResource
)

from .services import _
from .resources import (
    MusicfanResource,
    MusicianResource,
    MusicfanDummyResource,
    ClientResource,
    UtilisationIMPMusicfanResource,
    UtilisationIMPMusicianResource
)
from .views.widgets import (
    plugins_widget,
    todo_musician_widget,
    todo_musicfan_widget,
    # pocket_widget
)


def web_resources(config):
    '''
    Extends the resource tree for the web service.

    Note:
        The function is called by the plugin system, when the app is created.

    Args:
        config (pyramid.config.Configurator): App config

    Returns:
        None
    '''
    FrontendResource.add_child(MusicfanDummyResource)
    MusicfanDummyResource.add_child(ClientResource)
    BackendResource.add_child(MusicfanResource)
    BackendResource.add_child(MusicianResource)
    BackendResource.add_child(NewsResource)
    MusicfanResource.add_child(ClientResource)
    MusicfanResource.add_child(UtilisationIMPMusicfanResource)
    MusicianResource.add_child(ArtistResource)
    ArtistResource.add_child(AddArtistResource)
    MusicianResource.add_child(CreationResource)
    MusicianResource.add_child(UtilisationIMPMusicianResource)


def web_registry(config):
    '''
    Extends the registry for content elements for the web service.

    Note:
        The function is called by the plugin system, when the app is created.

    Args:
        config (pyramid.config.Configurator): App config

    Returns:
        None
    '''
    @FrontendResource.extend_registry
    def frontend(self):
        reg = self.dict()
        # css
        reg['static']['css'] = [
            self.request.static_path(
                'collecting_society_portal_imp:static/css/frontend.css'
            )
        ]
        # logo
        reg['static']['logo'] = self.request.static_path(
            'collecting_society_portal_imp:static/img/logo-adore.png'
        )
        # menue page
        reg['menues']['page'] = [
            {
                'name': _(u'overview'),
                'page': 'overview'
            },
            {
                'name': _(u'details'),
                'page': 'details'
            },
            {
                'name': _(u'about c3s'),
                'page': 'aboutc3s'
            },
            {
                'name': _(u'contact'),
                'page': 'contact'
            },
            {
                'name': _(u'imprint'),
                'page': 'imprint'
            }
        ]
        return reg

    @BackendResource.extend_registry
    def backend(self):
        reg = self.dict()
        # css
        reg['static']['css'] = [
            self.request.static_path(
                'collecting_society_portal_imp:static/css/backend.css'
            )
        ]
        # logo
        reg['static']['logo'] = self.request.static_path(
            'collecting_society_portal_imp:static/img/logo-adore.png'
        )
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
        # menue portal
        reg['menues']['portal'] = [
            {
                'name': _(u'News'),
                'url': self.request.resource_path(
                    BackendResource(self.request), 'news'
                )
            },
            {
                'name': _(u'Contact'),
                'url': self.request.resource_path(
                    BackendResource(self.request), 'contact'
                )
            },
            {
                'name': _(u'Imprint'),
                'url': self.request.resource_path(
                    BackendResource(self.request), 'imprint'
                )
            },
            {
                'name': _(u'Logout'),
                'url': self.request.resource_path(
                    BackendResource(self.request), 'logout'
                )
            }
        ]
        # news
        reg['content']['news'] = OrderedDict()
        reg['content']['news']['1'] = {
            'header': _(u'News Article 1'),
            'template': (
                'collecting_society_portal_imp:'
                'templates/content/news/news1'
            )
        }
        reg['content']['news']['2'] = {
            'header': _(u'News Article 2'),
            'template': (
                'collecting_society_portal_imp:'
                'templates/content/news/news2'
            )
        }
        reg['content']['news']['3'] = {
            'header': _(u'News Article 3'),
            'template': (
                'collecting_society_portal_imp:'
                'templates/content/news/news3'
            )
        }
        # widgets content-right
        reg['widgets']['content-right'] = [
            news_widget
        ]
        return reg

    @MusicfanResource.extend_registry
    def musicfan(self):
        reg = self.dict()
        # logo
        reg['static']['logo'] = self.request.static_path(
            'collecting_society_portal_imp:static/img/logo-musicfan.png'
        )
        # menue main
        reg['menues']['main'] = [
            {
                'name': _(u'Dashboard'),
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/element-icon.png'
                ),
                'url': self.request.resource_path(
                    MusicfanResource(self.request), 'dashboard'
                )
            },
            {
                'name': _(u'Clients'),
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/element-icon.png'
                ),
                'url': self.request.resource_path(
                    ClientResource(self.request), 'list'
                )
            },
            {
                'name': _(u'Music Utilization'),
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/element-icon.png'
                ),
                'url': self.request.resource_path(
                    UtilisationIMPMusicfanResource(self.request), 'list'
                )
            },
        ]
        # widgets content-right
        reg['widgets']['content-right'] = [
            news_widget,
            # pocket_widget,
            plugins_widget,
            todo_musician_widget
        ]
        return reg

    @MusicianResource.extend_registry
    def musician(self):
        reg = self.dict()
        # logo
        reg['static']['logo'] = self.request.static_path(
            'collecting_society_portal_imp:static/img/logo-musician.png'
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
                    'static/img/element-icon.png'
                )
            },
            {
                'name': _(u'My Artists'),
                'url': self.request.resource_path(
                    ArtistResource(self.request), ''
                ),
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/element-icon.png'
                )
            },
            {
                'name': _(u'My Creations'),
                'url': self.request.resource_path(
                    CreationResource(self.request), ''
                ),
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/element-icon.png'
                )
            },
            {
                'name': _(u'Music Utilisation'),
                'url': self.request.resource_path(
                    UtilisationIMPMusicianResource(self.request), 'list'
                ),
                'icon': self.request.static_path(
                    'collecting_society_portal_imp:'
                    'static/img/element-icon.png'
                )
            },
        ]
        # widgets content-right
        reg['widgets']['content-right'] = [
            news_widget,
            todo_musicfan_widget
        ]
        return reg


def web_views(config):
    '''
    Adds the views for the web service.

    Note:
        The function is called by the plugin system, when the app is created.

    Args:
        config (pyramid.config.Configurator): App config

    Returns:
        None
    '''
    config.add_static_view('static/imp', 'static', cache_max_age=3600)
    config.scan(ignore='.views.api')


def api_views(config):
    '''
    Adds the views for the api service.

    Note:
        The function is called by the plugin system, when the app is created.

    Args:
        config (pyramid.config.Configurator): App config

    Returns:
        None
    '''

    # routes
    config.add_route('whoami', '/debug/whoami', environment='development')
    config.add_route('objects', '/debug/objects', environment='development')

    config.add_route('request_api_key', '/account/register')

    config.add_route('authorize_client',
                     '/account/authorize_client/{uuid}/{hash}')
    config.add_route('authorize_client_success',
                     '/account/authorize_client/success')
    config.add_route('present_api_key', '/account/registered')
    config.add_route('utilization_form', '/web/utilization_form')

    # views
    config.add_static_view(
        'static/imp', 'static', cache_max_age=3600, environment='development'
    )
    config.scan('.views.api')
