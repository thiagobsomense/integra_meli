import json
from datetime import datetime
from sqlalchemy import select, update
from database.conn import PedidoML, PedidoItemML, PedidoPgtoML, PedidoEnvioML, PedidoDevolucaoML, PedidoDanfeML


async def add_order(session, order):
    data = {
        'user_id': order['seller']['id'],
        'ml_order_id': order['id'],
        'fulfilled': order['fulfilled'],
        'expiration_date': order['expiration_date'],
        'date_closed': order['date_closed'],
        'last_updated': order['last_updated'],
        'date_created': order['date_created'],
        'shipping_id': order['shipping']['id'],
        'payment_id': order['payments'][0]['id'] or None,
        'status': order['status'],
        'total_amount': order['total_amount'],
        'paid_amount': order['paid_amount']
    }

    pedido = session.add(PedidoML(data_atualizacao=datetime.now(), **data))

    return pedido


async def update_order(session, order):
    data = {
        'fulfilled': order['fulfilled'],
        'expiration_date': order['expiration_date'],
        'date_closed': order['date_closed'],
        'last_updated': order['last_updated'],
        'status': order['status'],
        'total_amount': order['total_amount'],
        'paid_amount': order['paid_amount']
    }

    await session.execute(update(PedidoML).where(PedidoML.ml_order_id == str(order['id'])).values(data))


async def create_or_update_order(session, order):
    data_obj = datetime.strptime(order['last_updated'], "%Y-%m-%dT%H:%M:%S.%f%z")
    data_obj = data_obj.replace(tzinfo=None)
    pedido = await session.execute(select(PedidoML).filter(PedidoML.ml_order_id == str(order['id'])))
    if len(pedido.fetchall()) == 0:
        await add_order(session, order)
        return 'create'
    else:
        for x in pedido.scalars():
            if x.last_updated < data_obj:
                await update_order(session, order)
                return 'update'


async def add_items(session, order):
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

        session.add(PedidoItemML(data_atualizacao=datetime.now(), **item_data))


async def add_payments(session, order):
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

        session.add(PedidoPgtoML(data_atualizacao=datetime.now(), **payment_data))


async def update_payments(session, order):
    # TODO(Fix): melhorar filtro de pagamento utilizando date_last_modified
    for payment in order['payments']:
        data = {
            'status_code': payment['status_code'],
            'status_detail': payment['status_detail'],
            'status': payment['status'],
            'date_last_modified': payment['date_last_modified'],
            'data_atualizacao': datetime.now()
        }

        await session.execute(update(PedidoPgtoML).where(PedidoPgtoML.payment_id == str(payment['id'])).values(data))


async def add_shipping(session, data):
    shipping_data = {
        'user_id': str(data['sender_id']),
        'ml_order_id': str(data['order_id']),
        'substatus_history_json': json.dumps(data['substatus_history']),
        'snapshot_packing_json':  json.dumps(data['snapshot_packing']),
        'receiver_id': data['receiver_id'],
        'base_cost': data['base_cost'],
        'cost_components_json': json.dumps(data['cost_components']),
        'type': data['type'],
        'return_details_json': json.dumps(data['return_details']),
        'sender_id': data['sender_id'],
        'mode': data['mode'],
        'order_cost': data['order_cost'],
        'priority_class_json': json.dumps(data['priority_class']),
        'service_id': data['service_id'],
        'tracking_number': data['tracking_number'],
        'shipping_id': data['id'],
        'shipping_items_json': json.dumps(data['shipping_items']),
        'tracking_method': data['tracking_method'],
        'last_updated': data['last_updated'],
        'items_types_json': json.dumps(data['items_types']),
        'comments': data['comments'],
        'substatus': data['substatus'],
        'date_created': data['date_created'],
        'date_first_printed': data['date_first_printed'],
        'created_by': data['created_by'],
        'application_id': data['application_id'],
        'return_tracking_number': data['return_tracking_number'],
        'site_id': data['site_id'],
        'carrier_info': data['carrier_info'],
        'market_place': data['market_place'],
        'customer_id': data['customer_id'],
        'quotation': data['quotation'],
        'status': data['status'],
        'logistic_type': data['logistic_type']
    }

    session.add(PedidoEnvioML(data_atualizacao=datetime.now(), **shipping_data))


async def update_shipping(session, result):
    data = {
        'substatus_history_json': json.dumps(result['substatus_history']),
        'return_details_json': json.dumps(result['return_details']),
        'last_updated': result['last_updated'],
        'status': result['status'],
        'data_atualizacao': datetime.now()
    }

    await session.execute(update(PedidoEnvioML).where(PedidoEnvioML.shipping_id == str(result['id'])).values(data))


async def update_claim(session, claim):
    data = {
        'claim_id': claim['id'],
        'claim_last_updated': claim['last_updated'],
        'claim_status': claim['status']
    }

    condition = ''
    match claim['resource']:
        case 'order':
            condition = PedidoML.ml_order_id
        case 'shipping':
            condition = PedidoML.shipping_id
        case 'payment':
            condition = PedidoML.payment_id
        case _:
            return
  
    await session.execute(update(PedidoML).where(condition == str(claim['resource_id'])).values(data))


async def add_returns(session, order, result):
    data = {
        'user_id': order['user_id'],
        'ml_order_id': order['order_id'],
        'resource_id': str(result['resource_id']),
        'resource': result['resource'],
        'claim_id': result['claim_id'],
        'status': result['status'],
        'type': result['type'],
        'subtype': result['subtype'],
        'status_money': result['status_money'],
        'refund_at': result['refund_at'],
        'shipping_json': json.dumps(result['shipping']),
        'warehouse_review_json': json.dumps(result['warehouse_review']),
        'date_created': result['date_created'],
        'last_updated': result['last_updated']
    }

    session.add(PedidoDevolucaoML(**data))


async def update_returns(session, result):
    data = {
        'resource': result['resource'],
        'status': result['status'],
        'subtype': result['subtype'],
        'status_money': result['status_money'],
        'refund_at': result['refund_at'],
        'shipping_json': json.dumps(result['shipping']),
        'warehouse_review_json': json.dumps(result['warehouse_review']),
        'last_updated': result['last_updated']
    }

    await session.execute(update(PedidoDevolucaoML).where(PedidoDevolucaoML.claim_id == str(result['claim_id'])).values(data))


async def create_or_update_returns(session, order, result):
    devol = await session.execute(select(PedidoDevolucaoML).filter(PedidoDevolucaoML.claim_id == str(result['claim_id'])))
    if len(devol.fetchall()) == 0:
        await add_returns(session, order, result)
        return 'create'
    else:
        await update_returns(session, result)
        return 'update'


async def add_danfe(session, seller_id, order_id, data):
    danfe_data = {
        'user_id': seller_id,
        'ml_order_id': order_id,
        'status': data['status'],
        'transaction_status': data['transaction_status'],
        'issuer_json': json.dumps(data['issuer']),
        'recipient_json': json.dumps(data['recipient']),
        'shipment_json': json.dumps(data['shipment']),
        'items_json': json.dumps(data['items']),
        'issued_date': data['issued_date'],
        'invoice_series': data['invoice_series'],
        'invoice_number': data['invoice_number'],
        'invoice_key': data['attributes']['invoice_key'],
        'attributes_json': json.dumps(data['attributes']),
        'fiscal_data_json': json.dumps(data['fiscal_data']),
        'amount': data['amount'],
        'items_amount': data['items_amount'],
        'errors_json': json.dumps(data['errors']),
        'items_quantity': data['items_quantity']
    }

    danfe = await session.execute(select(PedidoDanfeML).filter(PedidoDanfeML.ml_order_id == order_id, PedidoDanfeML.invoice_key == danfe_data['invoice_key']))
    if len(danfe.fetchall()) == 0:
        session.add(PedidoDanfeML(**danfe_data))
        return True
