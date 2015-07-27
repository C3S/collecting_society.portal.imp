# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal.imp


def include_web_views(config):
    config.add_static_view('static/imp', 'static', cache_max_age=3600)
    config.scan(ignore='.views.api')


def include_api_views(config):
    settings = config.get_settings()

    # routes
    if settings['env'] == 'development':
        config.add_route('whoami', '/debug/whoami')
        config.add_route('objects', '/debug/objects')
    config.add_route('request_api_key', '/account/register')

    config.add_route('authorize_client',
                     '/account/authorize_client/{uuid}/{hash}')
    config.add_route('authorize_client_success',
                     '/account/authorize_client/success')
    config.add_route('present_api_key', '/account/registered')
    config.add_route('utilization_form', '/web/utilization_form')

    # views
    if settings['env'] == 'development':
        config.add_static_view('static/imp', 'static', cache_max_age=3600)
    config.scan('.views.api')
