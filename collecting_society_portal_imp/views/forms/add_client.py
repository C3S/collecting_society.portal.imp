# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal.imp

import colander
import deform
import logging

from pyramid.security import remember

from collecting_society_portal.models import (
    Tdb,
    WebUser
)
from collecting_society_portal.views.forms import (
    LoginWebuser
)
from collecting_society_portal.views.forms.login_web_user import (
    authentication_is_successful,
    EmailField,
    PasswordField
)
from ...services import _
from ...models import Client
from ...resources import ClientResource

log = logging.getLogger(__name__)


# --- Controller --------------------------------------------------------------

class AddClient(LoginWebuser):
    """
    form controller for web_user login
    """

    def controller(self):

        self.form = add_client_form()

        if self.submitted() and self.validate():
            self.create_client()

        else:
            self.read_uuid()

        return self.response

    # --- Stages --------------------------------------------------------------

    # --- Conditions ----------------------------------------------------------

    # --- Actions -------------------------------------------------------------

    def read_uuid(self):
        get = self.request.GET
        uuid = get['uuid'] if 'uuid' in get else None
        if not uuid:
            self.redirect(self.request.root.__class__)
        else:
            self.render({'uuid': uuid})

    @Tdb.transaction(readonly=False)
    def create_client(self):
        uuid = self.appstruct['uuid']
        email = self.appstruct['email']

        if Client.search_by_uuid(uuid, active=False):
            self.request.session.flash(
                _('Client already exists: ') + uuid,
                'main-alert-warning'
            )
            self.redirect(
                ClientResource, 'list', headers=remember(self.request, email)
            )
            return

        _client = {
            'web_user': WebUser.search_by_email(email),
            'uuid': uuid,
            'player_name': 'Clementine',
            'player_version': '1.2',
            'plugin_name': 'Clementine IMP Prototyp',
            'plugin_version': '0.5',
            'plugin_vendor': 'C3S',
            'active': True
        }

        clients = Client.create([_client])

        if not clients:
            log.info("client add failed for %s: %s" % (email, _client))
            self.request.session.flash(
                _(u"Client could not be added: ") + uuid,
                'main-alert-danger'
            )
            self.redirect(
                ClientResource, 'list', headers=remember(self.request, email)
            )
            return
        client = clients[0]

        log.info("client add successful for %s: %s" % (email, client.uuid))
        self.request.session.flash(
            _(u"Client added: ") + client.uuid,
            'main-alert-success'
        )

        self.redirect(
            ClientResource, 'list', headers=remember(self.request, email)
        )


# --- Validators --------------------------------------------------------------

# --- Options -----------------------------------------------------------------

# --- Fields ------------------------------------------------------------------

class UuidField(colander.SchemaNode):
    oid = "uuid"
    schema_type = colander.String
    widget = deform.widget.HiddenWidget()


# --- Schemas -----------------------------------------------------------------

class AddClientSchema(colander.MappingSchema):
    title = _(u"Add Client")
    uuid = UuidField(
        title=_(u"Uuid")
    )
    email = EmailField(
        title=_(u"Email")
    )
    password = PasswordField(
        title=_(u"Password")
    )


# --- Forms -------------------------------------------------------------------

def add_client_form():
    return deform.Form(
        formid='add_client_form',
        schema=AddClientSchema(
            validator=colander.Function(authentication_is_successful)
        ),
        buttons=[
            deform.Button('submit', _(u"Submit"))
        ]
    )
