from datetime import datetime
from api.orders import Orders
from database import session,LojaML, PedidoML, PedidoItemML, PedidoPgtoML


def get_orders(client_id, token):
    order = Orders(client_id, token)
    orders = order.archived_orders()
    loja = session.query(LojaML).filter(LojaML.user_id == client_id).first()
    loja = loja.id
    
    if isinstance(orders, dict):
        total = orders['paging']['total']
        for order in orders['results']:
            data = {
                'user_id': order['seller']['id'],
                'id': order['id'],
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
        
            session.add(PedidoML(data_atualizacao=datetime.now(), **data))
        
        session.commit()
                
    else:
        return orders
    
