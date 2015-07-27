# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal.imp

import logging

from pyramid.view import (
    view_config,
    view_defaults
)

from collecting_society_portal.views import ViewBase
from ..resources import MusicfanResource

log = logging.getLogger(__name__)


@view_defaults(
    context='..resources.MusicfanResource',
    permission='authenticated')
class MusicfanViews(ViewBase):

    @view_config(
        name='')
    def root(self):
        redirect = self.redirect(MusicfanResource, 'dashboard')
        return redirect

    @view_config(
        name='dashboard',
        renderer='../templates/musicfan/dashboard.pt')
    def dashboard(self):
        return {}
