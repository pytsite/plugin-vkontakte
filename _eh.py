"""PytSite Vkontakte Event Handlers
"""
from pytsite import router as _router, lang as _lang, reg as _reg
from plugins import auth as _auth

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    if _auth.get_current_user().has_permission('vkontakte.settings.manage'):
        if not _reg.get('vkontakte.app_id') or not _reg.get('vkontakte.app_secret'):
            _router.session().add_warning_message(_lang.t('vkontakte@plugin_setup_required_warning'))
