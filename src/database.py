from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session


username = config('DB_USERNAME')
password = config('DB_PASSWORD')
server = config('DB_HOST')
port = config('DB_PORT', cast=int)
database = config('DB_DATABASE')

str_conn = f'mysql+pymysql://{username}:{password}@{server}:{port}/{database}'
engine = create_engine(str_conn)

Base = automap_base()
Base.prepare(autoload_with=engine)

# Clientes = Base.classes.clientes
LojaML = Base.classes.loja_mercado_livre
PedidoML = Base.classes.pedidos_mercado_livre
PedidoItemML = Base.classes.pedidos_itens_mercado_livre
PedidoPgtoML = Base.classes.pedidos_pagamentos_mercado_livre

session = Session(engine)
