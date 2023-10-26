import requests
from urllib.parse import urlencode


class Client(object):
    api_url = 'https://api.mercadolibre.com'
    logout_url = 'https://www.mercadolibre.com/jms/mlb/lgz/logout?go='

    auth_urls = {
        'MLA': "https://auth.mercadolibre.com.ar",  # Argentina
        'MLB': "https://auth.mercadolivre.com.br",  # Brasil
        'MCO': "https://auth.mercadolibre.com.co",  # Colombia
        'MCR': "https://auth.mercadolibre.com.cr",  # Costa Rica
        'MEC': "https://auth.mercadolibre.com.ec",  # Equuador
        'MLC': "https://auth.mercadolibre.cl",      # Chile
        'MLM': "https://auth.mercadolibre.com.mx",  # Mexico
        'MLU': "https://auth.mercadolibre.com.uy",  # Uruguai
        'MLV': "https://auth.mercadolibre.com.ve",  # Venezuela
        'MPA': "https://auth.mercadolibre.com.pa",  # Panama
        'MPE': "https://auth.mercadolibre.com.pe",  # Peru
        'MPT': "https://auth.mercadolibre.com.pt",  # Portugal
        'MRD': "https://auth.mercadolibre.com.do"   # Republica Dominicana
    }

    def __init__(self, client_id, client_secret, site='MLB'):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self._refresh_token = None
        self.user_id = None
        self.expires_in = None
        self.expires_at = None

        try:
            self.auth_url = self.auth_urls[site]
        except KeyError as e:
            raise ValueError(
                f'Site inválido, verifique o código informado. {e}')

    def authorization_url(self, redirect_url):
        params = {
            'response_type': 'code',
            'client_id': self.client_id,
            #'redirect_uri': redirect_url
        }
        url = f'{self.auth_url}/authorization?{urlencode(params)}'
        return url

    def exchange_code(self, redirect_url, code):
        params = {
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': code,
            'redirect_uri': redirect_url,
            'code_verifier': ''
        }
        url = f'{self.api_url}/oauth/token'

        headers = {
            'accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(url, headers=headers, data=urlencode(params))
        return response.json()

    def set_token(self, token):
        if isinstance(token, dict):
            self.access_token = token.get('access_token', None)
            self._refresh_token = token.get('refresh_token', None)
            self.user_id = token.get('user_id', None)
            self.expires_in = token.get('expires_in', None)
        else:
            self.access_token = token

    def refresh_token(self):
        params = {
            'grant_type': 'refresh_token',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': self._refresh_token,
        }
        url = f'{self.api_url}/oauth/token'

        headers = {
            'accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(url, headers=headers, data=urlencode(params))
        return response.json()


    def new_token(self, refresh_token):
        params = {
            'grant_type': 'refresh_token',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': refresh_token,
        }
        url = f'{self.api_url}/oauth/token'

        headers = {
            'accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(url, headers=headers, data=urlencode(params))
        return response.json()
