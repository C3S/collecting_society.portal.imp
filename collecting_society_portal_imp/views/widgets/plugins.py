# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal.imp

from pyramid.renderers import render

from ...services import _


def plugins_widget(request):
    heading = _(u'Plugin')
    body = render(
        '../../templates/widgets/plugins.pt',
        {},
        request=request
    )
    return {'heading': heading, 'body': body}
