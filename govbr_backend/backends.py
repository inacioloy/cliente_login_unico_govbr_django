# coding: utf-8

from django.conf import settings
from social_core.backends.oauth import BaseOAuth2

class GovbrOAuth2(BaseOAuth2):
    name = 'govbr'
    AUTHORIZATION_URL = settings.AUTHORIZATION_URL
    ACCESS_TOKEN_METHOD = 'POST'
    ACCESS_TOKEN_URL = settings.ACCESS_TOKEN_URL
    ID_KEY = 'sub'  # id_token
    RESPONSE_TYPE = 'code'
    REDIRECT_STATE = False
    STATE_PARAMETER = False
    USER_DATA_URL = settings.USER_DATA_URL

    def user_data(self, access_token, *args, **kwargs):
        return self.request(url=self.USER_DATA_URL, data={'scope': kwargs['response']['scope']}, method='GET', headers={'Authorization': 'Bearer {0}'.format(access_token)}).json()

    def get_user_details(self, response):
        """
        Retorna um dicionário mapeando os fields do settings.AUTH_USER_MODEL.
        você pode fazer aqui outras coisas, como salvar os dados do usuário
        (`response`) em algum outro model.
        """
        splitted_name = response['name'].split()
        first_name, last_name = splitted_name[0], ''
        if len(splitted_name) > 1:
            last_name = splitted_name[-1]
        return {'username': response['sub'], 'first_name': first_name.strip(), 'last_name': last_name.strip(),
                'name': response['name'], 'email': response['email'], 'email_verified': response['email_verified'],
                'phone_number': response['phone_number']}