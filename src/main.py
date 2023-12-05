import sys
import asyncio
from sqlalchemy import select
from database.conn import async_session, LojaML
from controllers.utils import verify_access_token, clear_logs
from controllers.orders import *
from controllers.billing import *
from api.orders import Orders
from api.billing import Billings


if len(sys.argv) > 1:
    executor = sys.argv[1]
else:
    executor = 'all'


async def main():  
    async with async_session as session:
        stores = await session.execute(select(LojaML))

    for store in stores.scalars():
        user_id = store.user_id
        access_token = await verify_access_token(store)

        order = Orders(user_id, access_token)
        billing = Billings(access_token)

        if executor in ['all', 'orders']:
            task_order = await get_orders(order, user_id)
            await get_shipping(task_order, order, user_id)

        if executor in ['all', 'shippings']:
            await update_shippings(order, user_id)

        if executor in ['all', 'returns']:
            await get_returns(order, user_id)
            await get_claims(order, user_id)

        if executor in ['all', 'billings']:
            await get_billings(billing, user_id)
    
    await clear_logs()   

asyncio.run(main())