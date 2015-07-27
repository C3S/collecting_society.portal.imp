# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal.imp

import logging

from pyramid.security import NO_PERMISSION_REQUIRED
from pyramid.view import (
    view_config,
    view_defaults
)

from collecting_society_portal.models import (
    Tdb,
    WebUser
)
from collecting_society_portal.views import ViewBase
from collecting_society_portal_creative.models import Artist
from ..models import (
    Client,
    CreationUtilisationIMP
)

log = logging.getLogger(__name__)


@view_defaults(permission=NO_PERMISSION_REQUIRED)
class WebDebugViews(ViewBase):

    def development(context, request):
        return request.registry.settings['env'] == 'development'

    def objects_view(self):
        web_users_all = WebUser.search_all()
        _clients = Client.search_all()
        _utilisations = CreationUtilisationIMP.search_all()
        _artists = Artist.search_all()
        return {
            'web_users': web_users_all,
            'clients': _clients,
            'artists': _artists,
            'utilisations': _utilisations,
        }

    @view_config(
        name='objects',
        renderer='../templates/debug/objects.pt',
        decorator=Tdb.transaction(),
        custom_predicates=[development])
    def objects(self):
        return self.objects_view()
