"""PytSite VK Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Public API
from ._api import get_app_id, get_app_secret
from . import _session as session, _widget as widget


def plugin_load_uwsgi():
    from pytsite import lang, router
    from plugins import settings
    from . import _eh, _settings_form

    # Resources
    lang.register_package(__name__)

    # Lang globals
    lang.register_global('vkontakte_admin_settings_url', lambda language, args: settings.form_url('vkontakte'))

    # Settings
    settings.define('vkontakte', _settings_form.Form, 'vkontakte@vkontakte', 'fa fa-vk', 'dev')

    # Event handlers
    router.on_dispatch(_eh.router_dispatch)
