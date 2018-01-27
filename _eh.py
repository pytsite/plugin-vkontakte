"""PytSite Vkontakte Event Handlers
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import router as _router, lang as _lang, reg as _reg
from plugins import auth as _auth


def router_dispatch():
    if _auth.get_current_user().has_role('dev'):
        if not _reg.get('vkontakte.app_id') or not _reg.get('vkontakte.app_secret'):
            _router.session().add_warning_message(_lang.t('vkontakte@plugin_setup_required_warning'))
