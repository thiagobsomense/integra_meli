import aiohttp
import asyncio
from decouple import config
from datetime import datetime, timedelta
from math import ceil
from database.conn import *
from database.orders import *
from  config.logging import logger


async def get_orders(order_api, user_id):
    init_at = datetime.now()
    count_add = 0
    count_update = 0
    shipping_tasks = []

    try:
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
                    logger.info(f'Tarefa Concluída - {count_add} novos registros e {count_update} registros atualizados', extra={'user_id': user_id, 'body': None, 'init_at': init_at, 'end_at': datetime.now()})
                else:
                    logger.warning('Falha na solicitação', extra={'user_id': user_id, 'body': f'status: {orders}', 'init_at': init_at, 'end_at': datetime.now()})

    except Exception as err:
        logger.error('Falha na execução', extra={'user_id': user_id, 'body': err, 'init_at': init_at, 'end_at': datetime.now()})

    finally:
        return shipping_tasks


async def get_shipping(data, order, user_id):
    init_at = datetime.now()
    count_add = 0

    try:
        async with async_session as session:
            async with aiohttp.ClientSession() as client_session:
                if isinstance(data, list):
                    tasks = []
                    for shipping in data:
                        tasks.append(asyncio.create_task(order.shipping(client_session, shipping)))

                    results = await asyncio.gather(*tasks)
                    for result in results:
                        await add_shipping(session, result)
                        count_add += 1

                    await session.commit()
                    logger.info(f'Tarefa finalizada: Total de {count_add} novos registros.', extra={'user_id': user_id, 'body': None, 'init_at': init_at, 'end_at': datetime.now()})
    
                else:
                    print(data)

    except Exception as err:
        logger.error('Falha na execução', extra={'user_id': user_id, 'body': err, 'init_at': init_at, 'end_at': datetime.now()})



def get_new_shipping(order):
    # TODO(Feat): Verificar como realizar o New Shipping
    
    # BUSCA NA BASE DE DADOS A LISTA DE SELLER ID QUE NÃO EXISTE NA TABELA DE SHIPPING PARA QUE A BUSCA E A ADIÇÃO SEJAM FEITAS
    # - CREATE NON EXISTING SHIPPINGS:

    # countResult = SELECT count(id) FROM orders WHERE seller_id = xxxx
    # total = countResult
    # offset = orders['paging']['offset']
    # limit = orders['paging']['limit']
    # max_pages = floor(total / limit)

    # SELECT o.mlorder_id, o.shipping_id
    # FROM orders o
    # LEFT JOIN shipping s ON s.id = o.shipping_id
    # WHERE s.id IS NULL
    # AND o.seller_id = XXXX
    # LIMIT $limit
    # OFFSET $offset

    # ADICIONA UM ARRAY DE PROMISES

    # EXECUTA AS PROMISES E SALVA O RESULTADO

    pass


async def update_shippings(order_api, user_id):
    init_at = datetime.now()
    count_update = 0

    try:
        async with async_session as session:
            to_date = datetime.now()
            from_date = to_date - timedelta(days=int(config('SHIPPING_RANGE')) or 15)
            data = await session.scalars(select(PedidoEnvioML).where(PedidoEnvioML.user_id == user_id, PedidoEnvioML.last_updated > from_date, PedidoEnvioML.date_created != to_date))
            
            async with aiohttp.ClientSession() as client_session:
                tasks = []
                for shipping in data:
                    tasks.append(asyncio.create_task(order_api.shipping(client_session, shipping.shipping_id)))

                results = await asyncio.gather(*tasks)
                for result in results:
                    await update_shipping(session, result)

            await session.commit()
            logger.info(f'Tarefa finalizada: Total de {count_update} registros atualizados.', extra={'user_id': user_id, 'body': None, 'init_at': init_at, 'end_at': datetime.now()})
    
    except Exception as err:
        logger.error('Falha na execução', extra={'user_id': user_id, 'body': err, 'init_at': init_at, 'end_at': datetime.now()})



async def get_claims(order_api, user_id):
    init_at = datetime.now()
    count = 0

    try: 
        async with async_session as session:
            async with aiohttp.ClientSession() as client_session:
                claims = await order_api.claims(client_session)

                if isinstance(claims, dict):
                    offset = 0
                    total = claims['paging']['total']
                    limit = claims['paging']['limit']
                    max_pages = ceil(total / limit)

                    tasks = []
                    for page in range(0, max_pages):
                        tasks.append(asyncio.create_task(order_api.claims(client_session, offset)))
                        offset += limit

                    results = await asyncio.gather(*tasks)
                    for result in results:
                        for data in result['data']:
                            await update_claim(session, data)

                    await session.commit()
                    logger.info(f'Tarefa finalizada: Total de {count} atualizados', extra={'user_id': user_id, 'body': None, 'init_at': init_at, 'end_at': datetime.now()})
                
                else:
                    logger.warning('Falha na solicitação', extra={'user_id': user_id, 'body': f'status: {claims}', 'init_at': init_at, 'end_at': datetime.now()})
                    return claims

    except Exception as err:
        logger.error('Falha na execução', extra={'user_id': user_id, 'body': err, 'init_at': init_at, 'end_at': datetime.now()})


async def get_returns(order_api, user_id):
    init_at = datetime.now()
    count_add = 0
    count_update = 0

    try:
        async with async_session as session:
            returns = await session.execute(select(PedidoML).filter(PedidoML.user_id == str(user_id), PedidoML.claim_status == 'opened', PedidoML.claim_try_number < int(config('MAX_CLAIM_TRY_NUMBER'))))
            async with aiohttp.ClientSession() as client_session:
                tasks, orders = [], []
                for order in returns.scalars():
                    tasks.append(asyncio.create_task(order_api.returns(client_session, order.claim_id)))
                    orders.append({'claim_id':  order.claim_id,  'order_id': order.ml_order_id, 'user_id': order.user_id, 'claim_try_number': order.claim_try_number})

                results = await asyncio.gather(*tasks)
                for result in results:
                    if result['status'] == 200:
                        order = [x for x in orders if x['claim_id'] == str(result['claim_id'])][0]
                        res = await create_or_update_returns(session, order, result['response'])
                        
                        if res == 'created':
                            count_add += 1
                        
                        if res =='update':
                            count_update += 1
                        
                        if result['response']['date_closed']:
                            await session.execute(update(PedidoML).where(PedidoML.claim_id == result['claim_id']).values(claim_status='closed', claim_date_closed=result['response']['date_closed']))
                            count_update += 1
                    
                    elif result['status'] == 404:
                        order = [x for x in orders if x['claim_id'] == str(result['claim_id'])][0]
                        count = order['claim_try_number'] + 1
                        obj = {'claim_try_number': count}
                        
                        if count >= int(config('MAX_CLAIM_TRY_NUMBER')):
                            obj['claim_status'] = 'not_found'
                        
                        await session.execute(update(PedidoML).where(PedidoML.claim_id == result['claim_id']).values(obj))
                    else:
                        logger.war('Falha na execução', extra={'user_id': user_id, 'body': result['response'], 'init_at': init_at, 'end_at': datetime.now()})
                        return result['status']

            await session.commit()
            logger.info(f'Tarefa finalizada: Total de {count_add} novos registros e {count_update} registros atualizados', extra={'user_id': user_id, 'body': None, 'init_at': init_at, 'end_at': datetime.now()})
    except Exception as err:
        logger.error('Falha na execução', extra={'user_id': user_id, 'body': err, 'init_at': init_at, 'end_at': datetime.now()})
