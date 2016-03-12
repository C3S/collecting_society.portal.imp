# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal

import colander
import deform
import logging
import requests

from collecting_society_portal.views.forms import FormController
from collecting_society_portal.resources import FrontendResource

from ...services import _

log = logging.getLogger(__name__)


# --- Controller --------------------------------------------------------------

class RegisterMailinglist(FormController):
    """
    form controller for registration on the betatest mailinglist
    """

    def controller(self):

        self.form = login_form()

        if self.submitted() and self.validate():
            self.register()

        return self.response

    # --- Stages --------------------------------------------------------------

    # --- Conditions ----------------------------------------------------------

    # --- Actions -------------------------------------------------------------

    def register(self):
        payload = {
            'name': '',
            'email': self.appstruct['email']
        }
        subresponse = requests.post(
            'https://lists.c3s.cc/mailman/subscribe/adore',
            data=payload
        )
        log.info(
            "SUBRESPONSE: %s"
            % subresponse.status_code
        )
        if subresponse.status_code == 200:
            self.redirect(FrontendResource, '')
            self.request.session.flash(
                _(u"Registration successfull")+": "+self.appstruct['email'],
                'main-alert-success'
            )
            log.info(
                "registration for mailinglist successful: %s"
                % self.appstruct['email']
            )


# --- Validators --------------------------------------------------------------

# --- Options -----------------------------------------------------------------

# --- Fields ------------------------------------------------------------------

class EmailField(colander.SchemaNode):
    oid = "email"
    schema_type = colander.String
    validator = colander.Email()


# --- Schemas -----------------------------------------------------------------

class RegisterMailinglistSchema(colander.MappingSchema):
    title = ""
    email = EmailField(
        title=_(u"Your e-mail"),
        description=_(u'Receive a notification when the beta version launches')
    )


# --- Forms -------------------------------------------------------------------

def login_form():
    return deform.Form(
        schema=RegisterMailinglistSchema(),
        buttons=[
            deform.Button('submit', _(u"Submit"))
        ]
    )
