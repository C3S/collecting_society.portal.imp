# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal

import logging

from pyramid.renderers import render
from pyramid.security import NO_PERMISSION_REQUIRED
from pyramid.view import (
    view_config,
    view_defaults
)

from collecting_society_portal.resources import (
    FrontendResource,
    BackendResource
)
from collecting_society_portal.views import ViewBase
from collecting_society_portal.views.forms import (
    LoginWebuser,
    RegisterWebuser
)
from .forms import RegisterMailinglist

log = logging.getLogger(__name__)


@view_defaults(
    context=FrontendResource,
    permission=NO_PERMISSION_REQUIRED)
class PagePortalViews(ViewBase):

    @view_config(
        name='',
        renderer='../templates/page/home.pt')
    def home(self):
        self.register_form(LoginWebuser)
        self.register_form(RegisterWebuser)
        self.register_form(RegisterMailinglist)
        return self.process_forms()

    @view_config(
        name='register',
        renderer='../templates/page/register.pt')
    def register(self):
        self.register_form(RegisterWebuser)
        return self.process_forms()

    @view_config(
        name='login',
        renderer='../templates/page/login.pt')
    def login(self):
        self.register_form(LoginWebuser)
        return self.process_forms()

    # static pages

    @view_config(
        name='overview',
        context=FrontendResource,
        renderer='collecting_society_portal:templates/page/page.pt')
    @view_config(
        name='overview',
        context=BackendResource,
        renderer='collecting_society_portal:templates/web_user/page.pt')
    def overview(self):
        page = render(
            '../templates/page/overview.pt', {}, request=self.request
        )
        return {'page': page}

    @view_config(
        name='details',
        context=FrontendResource,
        renderer='collecting_society_portal:templates/page/page.pt')
    @view_config(
        name='details',
        context=BackendResource,
        renderer='collecting_society_portal:templates/web_user/page.pt')
    def details(self):
        page = render(
            '../templates/page/details.pt', {}, request=self.request
        )
        return {'page': page}

    @view_config(
        name='aboutc3s',
        context=FrontendResource,
        renderer='collecting_society_portal:templates/page/page.pt')
    @view_config(
        name='aboutc3s',
        context=BackendResource,
        renderer='collecting_society_portal:templates/web_user/page.pt')
    def aboutc3s(self):
        page = render(
            '../templates/page/aboutc3s.pt', {}, request=self.request
        )
        return {'page': page}

    @view_config(
        name='contact',
        context=FrontendResource,
        renderer='collecting_society_portal:templates/page/page.pt')
    @view_config(
        name='contact',
        context=BackendResource,
        renderer='collecting_society_portal:templates/web_user/page.pt')
    def contact(self):
        page = render(
            '../templates/page/contact.pt', {}, request=self.request
        )
        return {'page': page}

    @view_config(
        name='imprint',
        context=FrontendResource,
        renderer='collecting_society_portal:templates/page/page.pt')
    @view_config(
        name='imprint',
        context=BackendResource,
        renderer='collecting_society_portal:templates/web_user/page.pt')
    def imprint(self):
        page = render(
            '../templates/page/imprint.pt', {}, request=self.request
        )
        return {'page': page}
