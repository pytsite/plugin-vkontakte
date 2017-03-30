"""PytSite Vkontakte Event Handlers
"""
from pytsite import settings as _settings, router as _router, lang as _lang, auth as _auth
from plugins import content_export as _content_export
from . import _session

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    if _auth.get_current_user().has_permission('vkontakte.settings.manage'):
        if not _settings.get('vkontakte.app_id') or not _settings.get('vkontakte.app_secret'):
            _router.session().add_warning_message(_lang.t('vkontakte@plugin_setup_required_warning'))


def odm_entity_pre_save_content_export(entity: _content_export.model.ContentExport):
    if 'access_token' in entity.driver_opts and 'screen_name' not in entity.driver_opts:
        driver_opts = dict(entity.driver_opts)
        s = _session.Session(entity.driver_opts['access_token'])
        driver_opts['title'] = s.get_screen_name(entity.driver_opts['user_id'])
        entity.f_set('driver_opts', driver_opts)
