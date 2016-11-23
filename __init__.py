"""PytSite VK Package.
"""
from ._session import Session

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def __init():
    from pytsite import content_export, assetman, lang, events, settings, permissions
    from . import _eh, _settings_form
    from ._content_export import Driver as ContentExportDriver

    # Resources
    lang.register_package(__name__, alias='vk')
    assetman.register_package(__name__, alias='vk')

    # Lang globals
    lang.register_global('vkontakte_admin_settings_url', lambda: settings.form_url('vk'))

    # Content export driver
    content_export.register_driver(ContentExportDriver())

    # Permissions
    permissions.define_permission('vkontakte.settings.manage', 'vkontakte@manage_vkontakte_settings', 'app')

    # Settings
    settings.define('vkontakte', _settings_form.Form, 'vkontakte@vkontakte', 'fa fa-vk', 'vkontakte.settings.manage')

    # Event handlers
    events.listen('pytsite.router.dispatch', _eh.router_dispatch)
    events.listen('pytsite.odm.entity.pre_save.content_export', _eh.odm_entity_pre_save_content_export)


__init()
