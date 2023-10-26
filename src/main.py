import asyncio
from sqlalchemy import select
from database.conn import async_session, LojaML
from controllers.orders import *
from api.orders import Orders


async def main():
    async with async_session as session:
        stores = await session.execute(select(LojaML))

    for store in stores.scalars():
        executor = 'all'
        shippingOrError = ''

        access_token = await verify_access_token(store)

        order = Orders(store.user_id, access_token)

        # if executor in ['all', 'orders']:
        #     shippingOrError = await get_orders(order, store.user_id)

        # if executor in ['all', 'shipping']:
        #     executionByCron = shippingOrError if (isinstance(shippingOrError, list)) else []
        #     await get_shipping(executionByCron, order)

        await get_claims(order)
        await get_returns(order, store.user_id)

        # ml = download_order(order, 0)
        # download_shipping(order, 0)
        # download_payments(order, 0)
        # download_devolutions(order, 0)


asyncio.run(main())
