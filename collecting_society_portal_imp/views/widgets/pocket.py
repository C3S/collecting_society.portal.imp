# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal.imp

import logging

from pyramid.renderers import render

from ...services import _
from collecting_society_portal.models import (
    Tdb,
    WebUser
)

log = logging.getLogger(__name__)


@Tdb.transaction(readonly=True)
def pocket_widget(request):
    heading = _(u'Pocket')
    web_user = WebUser.current_web_user(request)
    pocket_balance = web_user.party.pocket_balance
    pocket_budget = web_user.party.pocket_budget
    log.debug(
        (
            "pocket_balance: %s\n"
        ) % (
            pocket_balance
        )
    )
    body = render(
        '../../templates/widgets/pocket.pt',
        {
            'pocket_balance': pocket_balance,
            'pocket_budget': pocket_budget
        },
        request=request
    )
    return {'heading': heading, 'body': body}
