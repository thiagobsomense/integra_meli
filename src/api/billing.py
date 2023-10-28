class Billings():
    api_orders = 'https://api.mercadolibre.com/billing/integration/periods'

    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': f'Bearer {self.token}', }

    async def billing_periods(self, session, group, document_type, offset=0):
        params = {
            'group': group,
            'document_type': document_type,
            'offset': offset
        }
        url = self.api_orders

        async with session.get(url, headers=self.headers, params=params) as response:
            resp = await response.json() if response.status == 200 else response.status
            return resp
        
    async def billing_documents(self, session, group, key, limit=150, offset=0):
        params = {
            'group': group,
            # 'document_type': document_type,
            'limit': limit,
            'offset': offset
        }
        url = f'{self.api_orders}/key/{key}/documents'

        async with session.get(url, headers=self.headers, params=params) as response:
            resp = await response.json() if response.status == 200 else response.status
            return resp
    
    async def billing_summary(self, session, group, document_type, key):
        params = {
            'group': group,
            'document_type': document_type
        }
        url = f'{self.api_orders}/key/{key}/summary'

        async with session.get(url, headers=self.headers, params=params) as response:
            resp = await response.json() if response.status == 200 else response.status
            return resp
        
    async def billing_details(self, session, group, document_type, key, limit=150, offset=0):
        params = {
            'document_type': document_type,
            'limit': limit,
            'offset': offset
        }
        url = f'{self.api_orders}/key/{key}/group/{group}/details'

        async with session.get(url, headers=self.headers, params=params) as response:
            resp = await response.json() if response.status == 200 else response.status
            return resp
    
    async def billing_fulfillment(self, session, group, document_type, key, limit=150, offset=0):
        params = {
            'document_type': document_type,
            'limit': limit,
            'offset': offset
        }
        url = f'{self.api_orders}/key/{key}/group/{group}/full/details'

        async with session.get(url, headers=self.headers, params=params) as response:
            resp = await response.json() if response.status == 200 else response.status
            return resp
    
    async def billing_insurtech(self, session, group, document_type, key, limit=150, offset=0):
        params = {
            'document_type': document_type,
            'limit': limit,
            'offset': offset
        }
        url = f'{self.api_orders}/key/{key}/group/{group}/insurtech/details'

        async with session.get(url, headers=self.headers, params=params) as response:
            resp = await response.json() if response.status == 200 else response.status
            return resp
        