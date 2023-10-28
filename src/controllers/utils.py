from datetime import datetime, timedelta
from sqlalchemy import update
from decouple import config
from api.auth import Client
from database.conn import *
from  config.logging import logger


async def verify_access_token(store):

    async with async_session as session:
        store_id = store.user_id
        token = store.access_token
        date_expire = store.last_updated + timedelta(seconds=int(store.expires_in))

        if date_expire < datetime.now():
            client_id = config('CLIENT_ID')
            client_secret = config('CLIENT_SECRET')

            client = Client(client_id, client_secret)
            new_token = client.new_token(refresh_token=store.refresh_token)
            
            if not 'error' in new_token:
                token = new_token['access_token']
                expires_in = new_token['expires_in']
                refresh_token = new_token['refresh_token']

                data = {'access_token': token, 'expires_in': expires_in,
                        'refresh_token': refresh_token, 'last_updated': datetime.now()}

                await session.execute(update(LojaML).where(LojaML.user_id == str(store_id)).values(data))
                await session.commit()
        
        # log.wraning {'message': 'Error validating grant. Your authorization code or refresh token may be expired or it was already used', 'error': 'invalid_grant', 'status': 400, 'cause': []}
        return token