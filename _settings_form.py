"""PytSite Vkontakte Settings Form.
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang as _lang, validation as _validation
from plugins import widget as _widget, settings as _settings


class Form(_settings.Form):
    def _on_setup_widgets(self):
        self.add_widget(_widget.input.Text(
            uid='setting_app_id',
            weight=10,
            label=_lang.t('vkontakte@app_id'),
            required=True,
            help=_lang.t('vkontakte@app_id_setup_help'),
            rules=_validation.rule.Integer(),
        ))

        self.add_widget(_widget.input.Text(
            uid='setting_app_secret',
            weight=20,
            label=_lang.t('vkontakte@app_secret'),
            required=True,
            help=_lang.t('vkontakte@app_secret_setup_help'),
            rules=_validation.rule.Regex(pattern='[0-9a-zA-Z]{20}'),
        ))

        super()._on_setup_widgets()
