# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal.imp

from pyramid.renderers import render

from ...services import _


def todo_musician_widget(request):
    heading = _(u'To Do')
    body = render(
        '../../templates/widgets/todo#musician.pt',
        {},
        request=request
    )
    return {'heading': heading, 'body': body}


def todo_musicfan_widget(request):
    heading = _(u'To Do')
    body = render(
        '../../templates/widgets/todo#musicfan.pt',
        {},
        request=request
    )
    return {'heading': heading, 'body': body}