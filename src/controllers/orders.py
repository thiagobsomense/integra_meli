import uuid
from datetime import datetime
from math import floor
from sqlalchemy import func
from api.orders import Orders
from database import session, LojaML, PedidoML, PedidoItemML, PedidoPgtoML

def download_order(orderApi, api_offset):

    orders = orderApi.archived_orders(api_offset)

    if isinstance(orders, dict):
        # INSERÇÃO NO BANCO DE DADOS
        for order in orders['results']:
            order_uuid = uuid.uuid4()

            data = {
                'user_id': order['seller']['id'],
                'ml_order_id': order['id'],
                'fullfiled': order['fulfilled'],
                'expiration_date': order['expiration_date'],
                'date_closed': order['date_closed'],
                'last_updated': order['last_updated'],
                'date_created': order['date_created'],
                'shipping': order['shipping']['id'],
                'status_pedido': order['status'],
                'total_amount': order['total_amount'],
                'paid_amount': order['paid_amount']
            }

            pedido = session.query(PedidoML).filter(PedidoML.ml_order_id == func.binary(order['id']))
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
                    session.add(PedidoItemML(id=uuid.uuid4(), id_pedido=order_uuid, data_atualizacao=datetime.now(), **item_data))

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

                    session.add(PedidoPgtoML(id=uuid.uuid4(), id_pedido=order_uuid, data_atualizacao=datetime.now(), **payment_data))

                print(f"ADICIONANDO VENDA {order['id']} - {len(order['order_items'])} ITEM(S)")
                session.add(PedidoML(id=order_uuid, data_atualizacao=datetime.now(), **data))
            else:
                print(f"ATUALIZANDO VENDA {order['id']} - {len(order['order_items'])} ITEM(S)")
                pedido.update(data)

                if len(order['payments']) > 0: 
                    for payment in order['payments']:
                        print(payment['id'])
                        payment_updated = session.query(PedidoPgtoML).filter(PedidoPgtoML.payment_id == func.binary(payment['id']))
                        
                        # print(payment_updated)
                        if payment_updated.count() > 0:
                            payment_data = {
                                'status_code': payment['status_code'],
                                'status_detail': payment['status_detail'],
                                'status': payment['status'],
                            }
                            
                            print(payment_data)

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
        download_order(orderApi, new_offset)


def get_orders(client_id, token):
    order = Orders(client_id, token)
    download_order(order, 3700)
    # download_shipping(order, 0)
    # download_payments(order, 0)
    # download_devolutions(order, 0)
