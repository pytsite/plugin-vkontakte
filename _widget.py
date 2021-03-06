"""PytSite Vkontakte Widgets.
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang as _lang, router as _router, reg as _reg, html as _html
from plugins import widget as _widget


class Auth(_widget.Abstract):
    """PytSite Vkontakte oAuth Widget.
    """

    def __init__(self, uid: str, **kwargs):
        """Init.
        """
        super().__init__(uid, **kwargs)

        self._app_id = _reg.get('vkontakte.app_id')
        if not self._app_id:
            raise RuntimeError("Settings parameter 'vkontakte.app_id' is not defined.")

        self._scope = kwargs.get('scope', ('wall', 'offline', 'photos'))
        self._access_url = kwargs.get('access_url', '')
        self._access_token = kwargs.get('access_token', '')
        self._user_id = kwargs.get('user_id', '')
        self._group_id = kwargs.get('group_id', '')

        self._css += ' widget-vk-oauth'

    @property
    def scope(self) -> tuple:
        return self._scope

    @property
    def access_url(self) -> str:
        return self._access_url

    @property
    def group_id(self) -> str:
        return self._group_id

    def _get_element(self, **kwargs) -> _html.Element:
        """Render widget.
        :param **kwargs:
        """
        authorize_url = _router.url('https://oauth.vk.com/authorize', query={
            'client_id': self._app_id,
            'scope': ','.join(self.scope),
            'redirect_uri': 'https://oauth.vk.com/blank.html',
            'display': 'page',
            'response_type': 'token',
            'v': '5.37',
        })

        wrapper = _html.TagLessElement()

        wrapper.append(_widget.input.Text(
            uid=self.uid + '[access_url]',
            weight=10,
            label=_lang.t('vkontakte@access_url'),
            help=_lang.t('vkontakte@access_url_help', {'link': authorize_url}),
            value=self.access_url,
            required=True,
        ).renderable())

        wrapper.append(_widget.input.Integer(
            uid=self.uid + '[group_id]',
            weight=20,
            label=_lang.t('vkontakte@group_id'),
            value=self.group_id,
            h_size='col-sm-2'
        ).renderable())

        return wrapper
