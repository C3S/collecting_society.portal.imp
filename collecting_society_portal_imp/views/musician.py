# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal.imp

from pyramid.view import (
    view_config,
    view_defaults
)

from collecting_society_portal.views import ViewBase
from ..resources import MusicianResource


@view_defaults(
    context='..resources.MusicianResource',
    permission='read')
class MusicianViews(ViewBase):

    @view_config(
        name='')
    def root(self):
        return self.redirect(MusicianResource, 'dashboard')

    @view_config(
        name='dashboard',
        renderer='../templates/musician/dashboard.pt')
    def dashboard(self):
        return {}
