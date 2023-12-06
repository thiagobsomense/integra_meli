from retrying_async import retry
from decouple import config


class Billings():
    api_base = 'https://api.mercadolibre.com/billing/integration'

    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': f'Bearer {self.token}', }

    @retry(attempts=int(config('RETRAY_NUMBER')), delay=int(config('RETRAY_DELAY')))
    async def billing_periods(self, session, group, document_type, offset=0, limit=12):
        params = {
            'group': group,
            'document_type': document_type,
            'offset': offset,
            'limit': limit
        }
        url = f'{self.api_base}/monthly/periods'

        async with session.get(url, headers=self.headers, params=params) as response:
            resp = await response.json() if response.status == 200 else response.status
            return resp

    @retry(attempts=int(config('RETRAY_NUMBER')), delay=int(config('RETRAY_DELAY')))  
    async def billing_documents(self, session, key, group, document_type, offset=0, limit=150):
        params = {
            'group': group,
            'document_type': document_type,
            'limit': limit,
            'offset': offset
        }
        url = f'{self.api_base}/periods/key/{key}/documents'

        async with session.get(url, headers=self.headers, params=params) as response:
            resp = await response.json() if response.status == 200 else response.status
            return resp
    
    @retry(attempts=int(config('RETRAY_NUMBER')), delay=int(config('RETRAY_DELAY')))
    async def billing_summary(self, session, key, group, document_type):
        params = {
            'group': group,
            'document_type': document_type
        }
        url = f'{self.api_base}/periods/key/{key}/summary'

        async with session.get(url, headers=self.headers, params=params) as response:
            resp = await response.json() if response.status == 200 else response.status
            return resp

    @retry(attempts=int(config('RETRAY_NUMBER')), delay=int(config('RETRAY_DELAY')), timeout=10)    
    async def billing_details(self, session, key, group, document_type, offset=0, limit=150):
        params = {
            'document_type': document_type,
            'limit': limit,
            'offset': offset
        }
        url = f'{self.api_base}/periods/key/{key}/group/{group}/details'

        async with session.get(url, headers=self.headers, params=params) as response:
            resp = await response.json() if response.status == 200 else response.status
            return resp
    
    @retry(attempts=int(config('RETRAY_NUMBER')), delay=int(config('RETRAY_DELAY')))
    async def billing_fulfillment(self, session, group, document_type, key, offset=0, limit=150):
        params = {
            'document_type': document_type,
            'limit': limit,
            'offset': offset
        }
        url = f'{self.api_base}/periods/key/{key}/group/{group}/full/details'

        async with session.get(url, headers=self.headers, params=params) as response:
            resp = await response.json() if response.status == 200 else response.status
            return resp
    
    @retry(attempts=int(config('RETRAY_NUMBER')), delay=int(config('RETRAY_DELAY')))
    async def billing_insurtech(self, session, group, document_type, key, offset=0, limit=150):
        params = {
            'document_type': document_type,
            'limit': limit,
            'offset': offset
        }
        url = f'{self.api_base}/periods/key/{key}/group/{group}/insurtech/details'

        async with session.get(url, headers=self.headers, params=params) as response:
            resp = await response.json() if response.status == 200 else response.status
            return resp
        