import aiohttp
import asyncio
from datetime import datetime, timedelta
from math import ceil
from sqlalchemy import update
from decouple import config
from api.auth import Client
from database.conn import *
from database.orders import *
from  config.logging import logger


""" def download_order(order_api, api_offset):
    orders = order_api.archived_orders(api_offset)

    if isinstance(orders, dict):
        for order in orders['results']:
            data = {
                'user_id': order['seller']['id'],
                'ml_order_id': order['id'],
                'fulfilled': order['fulfilled'],
                'expiration_date': order['expiration_date'],
                'date_closed': order['date_closed'],
                'last_updated': order['last_updated'],
                'date_created': order['date_created'],
                'shipping_id': order['shipping']['id'],
                'status': order['status'],
                'total_amount': order['total_amount'],
                'paid_amount': order['paid_amount']
            }

            pedido = session.query(PedidoML).filter(
                PedidoML.ml_order_id == func.binary(order['id']))
            if pedido.count() == 0:
                seq_item = 1

                for item in order['order_items']:
                    item_data = {
                        'user_id': order['seller']['id'],
                        'ml_order_id': order['id'],
                        'seq': seq_item,
                        'ml_item_id': item['item']['id'],
                        'title': item['item']['title'],
                        'category_id': item['item']['category_id'],
                        'variation_id': item['item']['variation_id'],
                        'seller_custom_field': item['item']['seller_custom_field'],
                        'global_price': item['item']['global_price'],
                        'net_weight': item['item']['net_weight'],
                        'warranty': item['item']['warranty'],
                        'condition_item': item['item']['condition'],
                        'seller_sku': item['item']['seller_sku'],
                        'quantity': item['quantity'],
                        'unit_price': item['unit_price'],
                        'full_unit_price': item['full_unit_price'],
                        'currency_id': item['currency_id'],
                        'manufacturing_days': item['manufacturing_days'],
                        'picked_quantity': item['picked_quantity'],
                        'listing_type_id': item['listing_type_id'],
                        'base_exchange_rate': item['base_exchange_rate'],
                        'base_currency_id': item['base_currency_id'],
                        'bundle': item['bundle'],
                        'element_id': item['element_id']
                    }

                    seq_item += 1
                    session.add(PedidoItemML(
                        data_atualizacao=datetime.now(), **item_data))

                for payment in order['payments']:
                    payment_data = {
                        'payment_id': payment['id'],
                        'user_id': order['seller']['id'],
                        'ml_order_id': order['id'],
                        'reason': payment['reason'],
                        'status_code': payment['status_code'],
                        'total_paid_amount': payment['total_paid_amount'],
                        'operation_type': payment['operation_type'],
                        'transaction_amount': payment['transaction_amount'],
                        'transaction_amount_refunded': payment['transaction_amount_refunded'],
                        'date_approved': payment['date_approved'],
                        'collector_id': payment['collector']['id'],
                        'coupon_id': payment['coupon_id'],
                        'installments': payment['installments'],
                        'authorization_code': payment['authorization_code'],
                        'taxes_amount': payment['taxes_amount'],
                        'date_last_modified': payment['date_last_modified'],
                        'coupon_amount': payment['coupon_amount'],
                        'shipping_cost': payment['shipping_cost'],
                        'installment_amount': payment['installment_amount'],
                        'activation_uri': payment['activation_uri'],
                        'overpaid_amount': payment['overpaid_amount'],
                        'card_id': payment['card_id'],
                        'status_detail': payment['status_detail'],
                        'issuer_id': payment['issuer_id'],
                        'payment_method_id': payment['payment_method_id'],
                        'payment_type': payment['payment_type'],
                        'deferred_period': payment['deferred_period'],
                        'atm_transfer_reference_transaction_id': payment['atm_transfer_reference']['transaction_id'],
                        'atm_transfer_reference_company_id': payment['atm_transfer_reference']['company_id'],
                        'site_id': payment['site_id'],
                        'payer_id': payment['payer_id'],
                        'order_id': payment['order_id'],
                        'currency_id': payment['currency_id'],
                        'status': payment['status'],
                        'transaction_order_id': payment['transaction_order_id']
                    }

                    session.add(PedidoPgtoML(
                        data_atualizacao=datetime.now(), **payment_data))

                    shipping = order_api.shipping(order['shipping']['id'])
                    shipping_data = {
                        'user_id': order['seller']['id'],
                        'ml_order_id': order['id'],
                        'substatus_history': None,  # convert to json
                        'snapshot_packing':  None,  # convert to json
                        'receiver_id': shipping['receiver_id'],
                        'base_cost': 0.0,
                        'type': shipping['type'],
                        'return_details': None,  # convert to json
                        'sender_id': shipping['sender_id'],
                        'mode': shipping['mode'],
                        'order_cost': 0.0,  # convert to json
                        'priority_class': shipping['priority_class'],
                        'service_id': shipping['service_id'],
                        'tracking_number': shipping['tracking_number'],
                        'shipping_id': shipping['id'],
                        'tracking_method': shipping['tracking_method'],
                        'last_updated': shipping['last_updated'],
                        'items_types': shipping['items_types'],
                        'comments': shipping['comments'],
                        'substatus': shipping['substatus'],
                        'date_created': shipping['date_created'],
                        'date_first_printed': shipping['date_first_printed'],
                        'created_by': shipping['created_by'],
                        'application_id': shipping['application_id'],
                        'return_tracking_number': shipping['return_tracking_number'],
                        'site_id': shipping['site_id'],
                        'carrier_info': shipping['carrier_info'],
                        'market_place': shipping['market_place'],
                        'customer_id': shipping['customer_id'],
                        'quotation': shipping['quotation'],
                        'status': shipping['status'],
                        'logistic_type': shipping['logistic_type']
                        # adicionar shipping_items como json
                        # adicionar cost_components como json

                    }

                    session.add(PedidoEnvioML(
                        data_atualizacao=datetime.now(), **shipping_data))

                print(
                    f"ADICIONANDO VENDA {order['id']} - {len(order['order_items'])} ITEM(S)")
                session.add(PedidoML(data_atualizacao=datetime.now(), **data))
            else:
                print(
                    f"ATUALIZANDO VENDA {order['id']} - {len(order['order_items'])} ITEM(S)")
                pedido.update(data)
                session.query(PedidoEnvioML).filter(shipping_id=data['shipping_id']).update(shipping_data)

                if len(order['payments']) > 0: 
                    for payment in order['payments']:
                        print(payment['id'])
                        payment_updated = session.query(PedidoPgtoML).filter(PedidoPgtoML.payment_id == func.binary(payment['id']))
                        
                        if payment_updated.count() > 0:
                            payment_data = {
                                'status_code': payment['status_code'],
                                'status_detail': payment['status_detail'],
                                'status': payment['status'],
                            }

                            payment_updated.update(payment_data)

        session.commit()
    else:
        return orders

    total = orders['paging']['total']
    offset = orders['paging']['offset']
    limit = orders['paging']['limit']

    max_pages = floor(total / limit)
    max_offset = max_pages * limit
    new_offset = offset + limit if offset < max_offset else False

    if new_offset:
        download_order(order_api, new_offset) """


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


async def get_shipping(data, order):
    async with async_session as session:
        async with aiohttp.ClientSession() as client_session:
            tasks = []
            for shipping in data:
                tasks.append(asyncio.create_task(order.shipping(client_session, shipping)))

            results = await asyncio.gather(*tasks)
            for result in results:
                await add_shipping(session, result)

        await session.commit()

    # logger.info()


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


# TODO(Fix): Melhorar desempenho desse processo
async def update_shippings(order_api, user_id):
    async with async_session as session:
        today = datetime.now()
        obj_data = today - timedelta(days=30)
        data = await session.scalars(select(PedidoEnvioML).where(PedidoEnvioML.user_id == user_id, PedidoEnvioML.last_updated > obj_data, PedidoEnvioML.date_created != today))
        
        async with aiohttp.ClientSession() as client_session:
            tasks = []
            for shipping in data:
                tasks.append(asyncio.create_task(order_api.shipping(client_session, shipping.shipping_id)))

            results = await asyncio.gather(*tasks)
            for result in results:
                await update_shipping(session, result)

        await session.commit()

    # logger.info()


async def get_claims(order_api):
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


async def get_returns(order_api, user_id):
    init_at = datetime.now()
    async with async_session as session:
        returns = await session.execute(select(PedidoML).filter(PedidoML.user_id == str(user_id), PedidoML.claim_status == 'opened'))
        async with aiohttp.ClientSession() as client_session:
            tasks, orders = [], []
            for order in returns.scalars():
                tasks.append(asyncio.create_task(order_api.returns(client_session, order.claim_id)))
                orders.append({'claim_id':  order.claim_id,  'order_id': order.ml_order_id, 'user_id': order.user_id})

            results = await asyncio.gather(*tasks)
            for result in results:
                if isinstance(result, dict):
                    order = [x for x in orders if x['claim_id'] == str(result['claim_id'])][0]
                    await create_or_update_returns(session, order, result)
                else:
                    print(result)

            await session.commit()
            logger.info('Testanddo aplicacação', extra={'user_id': user_id, 'init_at': init_at, 'end_at': datetime.now()})

