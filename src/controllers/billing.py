import aiohttp
import asyncio
from datetime import datetime
from math import ceil
from database.conn import *
from database.orders import *
from  config.logging import logger


async def get_orders(order_api, user_id):
    init_at = datetime.now()
    count_add = 0
    count_update = 0
    shipping_tasks = []

    async with async_session as session:
        async with aiohttp.ClientSession() as client_session:
            orders = await order_api.orders_period(client_session)
            if isinstance(orders, dict):
                offset = 0
                total = orders['paging']['total']
                limit = orders['paging']['limit']
                max_pages = ceil(total / limit)

                tasks = []
                for page in range(0, max_pages):
                    tasks.append(asyncio.create_task(order_api.orders_period(client_session, offset)))
                    offset += limit

                results = await asyncio.gather(*tasks)
                for orders in results:
                    for order in orders['results']:
                        pedido = await create_or_update_order(session, order)
                        if pedido == 'create':
                            await add_items(session, order)
                            await add_payments(session, order)
                            shipping_tasks.append(order['shipping']['id'])
                            count_add += 1
                        else:
                            await update_payments(session, order)
                        
                        if pedido == 'update':
                            count_update += 1

                await session.commit()
                logger.info(f'Tarefa Concluída - {count_add} novos registros e {count_update} registros atualizados', extra={'user_id': user_id, 'init_at': init_at, 'end_at': datetime.now()})
            else:
                logger.warning(f'Erro na solicitação {orders}', extra={'user_id': user_id, 'init_at': init_at, 'end_at': datetime.now()})

    return shipping_tasks
