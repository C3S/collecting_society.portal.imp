# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal.imp
"""
Cornice service for Utilisations.
"""

from datetime import datetime
import json
import logging

from pyramid.security import NO_PERMISSION_REQUIRED
from cornice import Service
from colander import (
    MappingSchema,
    SchemaNode,
    String,
    DateTime
)

from ...models import (
    Client,
    CreationUtilisationIMP
)

# see also
# http://cornice.readthedocs.org/en/latest/validation.html -> colander !
# http://makina-corpus.com/blog/metier/2013/multi-format-restful-api-with-cornice
# https://mail.mozilla.org/pipermail/services-dev/2011-November/000737.html

log = logging.getLogger(__name__)


utilisation_imp = Service(
    name='util_imp',
    path='/v1/util_imp',
    description="Utilisation IMP",
    permission=NO_PERMISSION_REQUIRED
)


class UtilisationSchema(MappingSchema):
    """
    a schema for validation of utilisations
    """
    client_uuid = SchemaNode(
        String(),
        location='body',
        type='str',
    )
    time_played = SchemaNode(
         DateTime(),
         location='body',
         type='str',
    )
    time_submitted = SchemaNode(
         DateTime(),
         location='body',
         type='str',
    )
    artist = SchemaNode(
        String(),
        location='body',
        type='str',
    )
    title = SchemaNode(
        String(),
        location='body',
        type='str',
    )
    release = SchemaNode(
        String(),
        location='body',
        type='str',
    )
    track_number = SchemaNode(
        String(),
        location='body',
        type='str',
    )
    duration = SchemaNode(
        String(),
        location='body',
        type='str',
    )
    fingerprinting_algorithm = SchemaNode(
        String(),
        location='body',
        type='str',
    )
    fingerprinting_version = SchemaNode(
        String(),
        location='body',
        type='str',
    )
    fingerprint = SchemaNode(
        String(),
        location='body',
        type='str',
    )


# @utilisation_imp.post(schema=UtilisationSchema)
@utilisation_imp.post()
def post_imp_utilization(request):
    """
    A place to put an imp clients utilisations

    takes a POST request with utilisation data
    XXX TODO: check headers for auth&auth

    returns JSON
    """

    log.debug('the request:\n%s\n' % request)

    content = json.loads(request.body)  # load the json from the body

    log.debug('the content:\n%s\n' % content)

    # XXX TODO how about the device token?
    # log.debug('the device token: %s' % content['client_uuid'])

    # log.debug(
    #     "-- the uuid from the utilisation: {}".format(content['client_uuid'])
    # )

    # get the user to attribute this utilisation to by matching the client_uuid
    try:
        _client = Client.search_by_uuid(content['client_uuid'])
        if _client is None:
            return {
                'status': 422,
                'status_title': 'ERROR -- client not found',
                'created-at': datetime.strftime(datetime.now(), '%Y-%m-%d'),
                'hostname': '123.4.5.6',
                # 'docs': request.static_url(_doc_url, _anchor=_doc_anchor),
            }
    except IndexError:
        _client = []

    _util = None
    try:
        _util = CreationUtilisationIMP.create([
            {
                'client': _client.id,  # only works with numbers, i.e. web_user.id
                'artist': content['artist'].encode('utf-8'),
                'release': content['release'].encode('utf-8'),
                'title': content['title'].encode('utf-8'),
                'track_number': content['track_number'],
                'duration': content['duration'],
                'time_played': content['time_played'],
                # set in tryton: 'time_submitted': content['time_submitted'],
                'fingerprint': content['fingerprint'],
                'fingerprinting_algorithm': content['fingerprinting_algorithm'],
                'fingerprinting_version': content['fingerprinting_version'],
            }
        ])
    except:
        pass

    if not _util:
        return {
            'status': 422,
            'status_title': 'ERROR -- utilisation could not be created',
            'created-at': datetime.strftime(datetime.now(), '%Y-%m-%d'),
            'hostname': '123.4.5.6',
            # 'docs': request.static_url(_doc_url, _anchor=_doc_anchor),
        }

    # fingerprint = content['fingerprint']
    # if fingerprint == '':  # never hit because never empty, see schema?
    #     fingerprint = 'not found'
    #     log.debug(
    #         'FINGERPRINT NOT FOUND!!!\n'
    #         'results status code: 422 Unprocessable Entity\n'
    #     )
    #     return {
    #        'got': fingerprint,
    #        'status': 422,
    #        'status_title': 'Unprocessable entity',
    #        'url': 'https://0.0.0.0:6543/api/v1/docs/422_unprocessable.html',
    #     }

    # log.debug('results status code: 200 OK')

    # _doc_url = 'collecting_society_portal_imp:docs/rest-api/v1/index.html'
    # _doc_anchor = 'module-collecting_society_portal_imp.api_utilizations_imp'
    # print 'DOCS: %s' % request.static_url(_doc_url, _anchor=_doc_anchor)

    return {
        'status': 200,
        'status_title': 'OK -- success',
        'created-at': datetime.strftime(datetime.now(), '%Y-%m-%d'),
        'hostname': '123.4.5.6',
        'id': '_util.id',
        'url': 'https://0.0.0.0:6543/api/v1/my/utilizations/ID.html',
        # 'docs': request.static_url(_doc_url, _anchor=_doc_anchor),
    }
