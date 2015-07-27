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
from ..services import _
from ..models import Client
from ..resources import (
    ClientResource
)
from .forms import AddClient

log = logging.getLogger(__name__)


@view_defaults(
    context='..resources.ClientResource',
    permission='authenticated')
class ClientViews(ViewBase):

    @view_config(
        name='')
    def root(self):
        return self.redirect(ClientResource, 'list')

    @view_config(
        name='list',
        renderer='../templates/client/list.pt',
        decorator=Tdb.transaction())
    def list_clients(self):
        web_user = WebUser.current_web_user(self.request)
        return {
            'player_names': Client.get_player_names_by_web_user(web_user.id),
            'clients': Client.search_by_web_user(web_user.id)
        }

    @view_config(
        name='add',
        renderer='../templates/client/add.pt',
        permission=NO_PERMISSION_REQUIRED)
    def add_client(self):
        self.register_form(AddClient)
        return self.process_forms()

    @view_config(
        name='delete',
        decorator=Tdb.transaction(readonly=False))
    def delete_client(self):
        _uuid = self.request.subpath[0]
        if _uuid is None:
            self.request.session.flash(
                _(u"Could not delete client - uuid is missing"),
                'main-alert-warning'
            )
            return self.redirect(ClientResource, 'list')

        client = Client.search_by_uuid(_uuid)
        if client is None:
            self.request.session.flash(
                _(u"Could not delete client - client not found"),
                'main-alert-warning'
            )
            return self.redirect(ClientResource, 'list')

        Client.disable(client)
        self.request.session.flash(
            _(u"Client deleted: ") + _uuid,
            'main-alert-success'
        )
        return self.redirect(ClientResource, 'list')
