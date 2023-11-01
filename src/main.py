import sys
import asyncio
import sched
import time
from sqlalchemy import select
from database.conn import async_session, LojaML
from controllers.utils import verify_access_token,clear_logs
from controllers.orders import *
from controllers.billing import *
from api.orders import Orders
from api.billing import Billings


if len(sys.argv) > 1:
    executor = sys.argv[1]
else:
    executor = 'all'


async def main():
    t1, t2, t3, t4, t5, t6 = None, None, None, None, None, None
    errors = [403, 443, 500]
    delay = int(config('RETRAY_DELAY'))
    max_rcount = int(config('RETRAY_NUMBER'))
    rcount = 0
    
    retry = sched.scheduler(time.time, time.sleep)
        
    async with async_session as session:
        stores = await session.execute(select(LojaML))

    for store in stores.scalars():
        user_id = store.user_id
        access_token = await verify_access_token(store)

        order = Orders(user_id, access_token)
        billing = Billings(access_token)

        if executor in ['all', 'orders']:
            t1 = await get_orders(order, user_id)
            t2 = await get_shipping(t1, order, user_id)

        if executor in ['all', 'shippings']:
            t3 = await update_shippings(order, user_id)

        if executor in ['all', 'returns']:
            t4 = await get_returns(order, user_id)
            t5 = await get_claims(order, user_id)

        if executor in ['all', 'billings']:
            t6 = await get_billings(billing, user_id)

    
        if t1 in errors and rcount <= max_rcount:
            retry.enter(delay, 1, get_orders, argument=(order, user_id,))
            rcount += 1

        if t2 in errors:
            retry.enter(delay, 1, get_orders, argument=(order, user_id,))
            retry.enter(delay, 1, get_shipping, argument=(t1, order, user_id,))

        if t3 in errors:
            retry.enter(delay, 1, update_shippings, argument=(order, user_id,))
        
        if t4 in errors:
            retry.enter(delay, 1, get_returns, argument=(order, user_id,))
        
        if t5 in errors:
            retry.enter(delay, 1, get_claims, argument=(order, user_id,))
        
        if t6 in errors:
            retry.enter(delay, 1, get_billings, argument=(billing, user_id,))
        print(t6) 

    await clear_logs()   
    retry.run()

asyncio.run(main())
