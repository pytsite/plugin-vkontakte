"""PytSite VK Plugin
"""
# Public API
from ._api import get_app_id, get_app_secret
from . import _session as session, _widget as widget

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    # Locally necessary import
    from pytsite import assetman, lang, settings, permissions, router
    from . import _eh, _settings_form

    # Resources
    lang.register_package(__name__, alias='vkontakte')
    assetman.register_package(__name__, alias='vkontakte')

    # Lang globals
    lang.register_global('vkontakte_admin_settings_url', lambda language, args: settings.form_url('vkontakte'))

    # Permissions
    permissions.define_permission('vkontakte.settings.manage', 'vkontakte@manage_vkontakte_settings', 'app')

    # Settings
    settings.define('vkontakte', _settings_form.Form, 'vkontakte@vkontakte', 'fa fa-vk', 'vkontakte.settings.manage')

    # Event handlers
    router.on_dispatch(_eh.router_dispatch)


_init()
