# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal.imp

import logging

from pyramid.security import NO_PERMISSION_REQUIRED
from pyramid.view import (
    view_config,
    view_defaults
)

# from collecting_society_portal.views import ViewBase
from collecting_society_portal.models import (
    Tdb,
    WebUser
)

from ..debug import WebDebugViews

log = logging.getLogger(__name__)


@view_defaults(permission=NO_PERMISSION_REQUIRED, environment="development")
class ApiDebugViews(WebDebugViews):

    @view_config(
        route_name="whoami",
        renderer="json")
    def whoami(self):
        """
        View returning the authenticated user's credentials.
        """
        login = self.request.unauthenticated_userid
        principals = WebUser.current_roles(self.request)
        return {"login": login, "principals": principals}

    @view_config(
        route_name='objects',
        renderer='../../templates/debug/objects.pt',
        decorator=Tdb.transaction())
    def objects(self):
        return self.objects_view()
