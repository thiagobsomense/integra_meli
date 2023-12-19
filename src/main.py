import sys
sys.path.append('/home/PedroLucas/integra_meli')

import asyncio
from sqlalchemy import select
from database.conn import async_session, LojaML
from controllers.utils import verify_access_token, clear_logs
from controllers.orders import get_orders, get_shipping, update_shippings, get_danfe, get_returns, get_claims
from controllers.billing import get_billings
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
            shipping_tasks, order_tasks = await get_orders(order, user_id)
            await get_shipping(shipping_tasks, order, user_id)
            await get_danfe(order_tasks, order, user_id)

        if executor in ['all', 'shippings']:
            await update_shippings(order, user_id)

        if executor in ['all', 'returns']:
            await get_returns(order, user_id)
            await get_claims(order, user_id)

        if executor in ['billings']:
            await get_billings(billing, user_id)
    
    await clear_logs()   

asyncio.run(main())