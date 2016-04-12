# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal.imp

from pyramid.view import (
    view_config,
    view_defaults
)

from collecting_society_portal.views import ViewBase
from collecting_society_portal.models import (
    Tdb,
    WebUser
)
from ..resources import (
    UtilisationIMPMusicfanResource,
    UtilisationIMPMusicianResource
)
from ..models import CreationUtilisationIMP


@view_defaults(
    permission='read')
class UtilisationIMPViews(ViewBase):

    @view_config(
        context='..resources.UtilisationIMPMusicfanResource',
        name='')
    def musicfan_root(self):
        return self.redirect(UtilisationIMPMusicfanResource, 'list')

    @view_config(
        context='..resources.UtilisationIMPMusicfanResource',
        name='list',
        renderer='../templates/utilisation_imp/musicfan_list.pt',
        decorator=Tdb.transaction(readonly=True))
    def musicfan_list(self):
        web_user = WebUser.current_web_user(self.request)
        utilisations = CreationUtilisationIMP.search_by_musicfan(
            web_user.id
        )
        return {'utilisations': utilisations}

    @view_config(
        context='..resources.UtilisationIMPMusicianResource',
        name='')
    def musician_root(self):
        return self.redirect(UtilisationIMPMusicianResource, 'list')

    @view_config(
        context='..resources.UtilisationIMPMusicianResource',
        name='list',
        renderer='../templates/utilisation_imp/musician_list.pt',
        decorator=Tdb.transaction(readonly=True))
    def musician_list(self):
        web_user = WebUser.current_web_user(self.request)
        utilisations = CreationUtilisationIMP.search_by_musician(
            web_user.party.id
        )
        return {'utilisations': utilisations}
