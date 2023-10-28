import sys
import asyncio
from sqlalchemy import select
from database.conn import async_session, LojaML
from  controllers.utils import verify_access_token
from controllers.orders import *
from api.orders import Orders


if len(sys.argv) > 1:
    executor = sys.argv[1]
else:
    executor = 'all'

# TODO(Feat): Adicionar o crontab para criar lista de tarefas
async def main():
    async with async_session as session:
        stores = await session.execute(select(LojaML))

    for store in stores.scalars():

        access_token = await verify_access_token(store)

        order = Orders(store.user_id, access_token)

        if executor in ['all', 'orders']:
            shippingOrError = await get_orders(order, store.user_id)
            shippingOrError = shippingOrError if (isinstance(shippingOrError, list)) else []
            await get_shipping(shippingOrError, order)

        if executor in ['all', 'shipping']:
            await update_shippings(order, store.user_id)

        if executor in ['all', 'claims']:
            await get_claims(order)

        if executor in ['all', 'returns']:
            await get_returns(order, store.user_id)


asyncio.run(main())
