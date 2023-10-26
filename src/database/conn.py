from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.automap import automap_base


username = config('DB_USERNAME')
password = config('DB_PASSWORD')
server = config('DB_HOST')
port = config('DB_PORT', cast=int)
database = config('DB_DATABASE')

str_conn = f'mysql+pymysql://{username}:{password}@{server}:{port}/{database}'
engine = create_engine(str_conn)

async_str_conn = f'mysql+asyncmy://{username}:{password}@{server}:{port}/{database}'
async_engine = create_async_engine(async_str_conn)

Base = automap_base()
Base.prepare(autoload_with=engine)

# Clientes = Base.classes.clientes
LojaML = Base.classes.ml_loja
PedidoML = Base.classes.ml_pedidos
PedidoItemML = Base.classes.ml_pedidos_itens
PedidoPgtoML = Base.classes.ml_pedidos_pagamentos
PedidoEnvioML = Base.classes.ml_pedidos_envios
PedidoDevolucaoML = Base.classes.ml_pedidos_devolucao
LogsML = Base.classes.ml_logs

try:
    async_session = AsyncSession(async_engine)
except Exception as e:
    print(f'Não foi possível conectar ao banco de dados {e}')
