"""PytSite VK Package.
"""
# Public API
from ._session import Session

# Locally necessary import
from pytsite import assetman as _assetman, lang as _lang, events as _events, settings as _settings, \
    permissions as _permissions
from . import _eh, _settings_form
from ._content_export import Driver as ContentExportDriver

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Resources
_lang.register_package(__name__, alias='vkontakte')
_assetman.register_package(__name__, alias='vkontakte')

# Lang globals
_lang.register_global('vkontakte_admin_settings_url', lambda language, args: _settings.form_url('vkontakte'))

# Content export driver
try:
    from plugins import content_export

    content_export.register_driver(ContentExportDriver())
except ImportError as e:
    raise RuntimeError("Required plugin is not found: {}".format(e))

# Permissions
_permissions.define_permission('vkontakte.settings.manage', 'vkontakte@manage_vkontakte_settings', 'app')

# Settings
_settings.define('vkontakte', _settings_form.Form, 'vkontakte@vkontakte', 'fa fa-vk', 'vkontakte.settings.manage')

# Event handlers
_events.listen('pytsite.router.dispatch', _eh.router_dispatch)
_events.listen('pytsite.odm.entity.pre_save.content_export', _eh.odm_entity_pre_save_content_export)
