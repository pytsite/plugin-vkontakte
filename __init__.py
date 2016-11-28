"""PytSite VK Package.
"""
from ._session import Session

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def __init():
    from pytsite import assetman, lang, events, settings, permissions
    from . import _eh, _settings_form
    from ._content_export import Driver as ContentExportDriver

    # Resources
    lang.register_package(__name__, alias='vkontakte')
    assetman.register_package(__name__, alias='vkontakte')

    # Lang globals
    lang.register_global('vkontakte_admin_settings_url', lambda: settings.form_url('vkontakte'))

    # Content export driver
    try:
        from plugins import content_export
        content_export.register_driver(ContentExportDriver())
    except ImportError as e:
        raise RuntimeError("Required plugin is not found: {}".format(e))

    # Permissions
    permissions.define_permission('vkontakte.settings.manage', 'vkontakte@manage_vkontakte_settings', 'app')

    # Settings
    settings.define('vkontakte', _settings_form.Form, 'vkontakte@vkontakte', 'fa fa-vk', 'vkontakte.settings.manage')

    # Event handlers
    events.listen('pytsite.router.dispatch', _eh.router_dispatch)
    events.listen('pytsite.odm.entity.pre_save.content_export', _eh.odm_entity_pre_save_content_export)


__init()
