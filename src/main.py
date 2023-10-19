from database import session, LojaML
from controllers.orders import get_orders


stores = session.query(LojaML).all()

for store in stores:
    pedidos = get_orders(store.user_id, store.access_token)
    