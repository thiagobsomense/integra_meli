from retrying_async import retry
from decouple import config
from datetime import datetime, timedelta


class Orders():
    api_orders = 'https://api.mercadolibre.com/orders/search'

    def __init__(self, client_id, token):
        self.client_id = client_id
        self.token = token
        self.headers = {'Authorization': f'Bearer {self.token}', }

    @retry(attempts=int(config('RETRAY_NUMBER')), delay=int(config('RETRAY_DELAY')))
    async def orders_period(self, session, offset=0):
        # TODO(Fix): verificar formtado de data e deixa-la dinamica
        now = datetime.now()
        formatted_to = now.strftime("%Y-%m-%dT%H:%M:%SZ")

        subtract_day = now - timedelta(days=int(config('ORDER_RANGE')) or 30)
        formatted_from = subtract_day.strftime("%Y-%m-%dT%H:%M:%SZ")

        params = {
            'seller': self.client_id,
            'order.date_last_updated.from': formatted_from,
            'order.date_last_updated.to': formatted_to,
            'order.status': 'paid',
            'offset': offset
        }
        url = self.api_orders

        async with session.get(url, headers=self.headers, params=params) as response:
            resp = await response.json() if response.status == 200 else response.status
            return resp

    @retry(attempts=int(config('RETRAY_NUMBER')), delay=int(config('RETRAY_DELAY')))
    async def archived_orders(self, session, offset=0):
        params = {
            'seller': self.client_id,
            'offset': offset
        }
        url = f'{self.api_orders}/archived'

        async with session.get(url, headers=self.headers, params=params) as response:
            resp = await response.json() if response.status == 200 else response.status
            return resp

    @retry(attempts=int(config('RETRAY_NUMBER')), delay=int(config('RETRAY_DELAY')))
    async def recents_orders(self, session, offset=0):
        params = {
            'seller': self.client_id,
            'offset': offset
        }
        url = f'{self.api_orders}/recent'
        async with session.get(url, headers=self.headers, params=params) as response:
            resp = await response.json() if response.status == 200 else response.status
            return resp

    def products():
        pass
    
    @retry(attempts=int(config('RETRAY_NUMBER')), delay=int(config('RETRAY_DELAY')))
    async def shipping(self, session, shipment_id):
        url = f'https://api.mercadolibre.com/shipments/{shipment_id}'

        async with session.get(url, headers=self.headers) as response:
            resp = await response.json() if response.status == 200 else response.status
            return resp

    def payments():
        pass
    
    @retry(attempts=int(config('RETRAY_NUMBER')), delay=int(config('RETRAY_DELAY')))
    async def claims(self, session, offset=0):
        params = {
            'status': 'opened',
            # 'type': 'return',
            'offset': offset
        }
        url = f'https://api.mercadolibre.com/v1/claims/search'

        async with session.get(url, headers=self.headers, params=params) as response:
            resp = await response.json() if response.status == 200 else response.status
            return resp

    @retry(attempts=int(config('RETRAY_NUMBER')), delay=int(config('RETRAY_DELAY')))
    async def returns(self, session, claim_id):
        url = f'https://api.mercadolibre.com/v2/claims/{claim_id}/returns'

        async with session.get(url, headers=self.headers) as response:
            # resp = await response.json() if response.status == 200 else response.status

            obj = {
                "status": response.status,
                'claim_id': claim_id,
                "response": await response.json()
            }

            return obj
