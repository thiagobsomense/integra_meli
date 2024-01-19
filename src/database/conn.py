import logging
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.automap import automap_base


logging.basicConfig(level=logging.INFO, filename="database.log", format="%(asctime)s - %(levelname)s - %(message)s")

username = config('DB_USERNAME')
password = config('DB_PASSWORD')
server = config('DB_HOST')
port = config('DB_PORT', cast=int)
database = config('DB_DATABASE')

str_conn = f'mysql+pymysql://{username}:{password}@{server}:{port}/{database}'
engine = create_engine(str_conn, pool_timeout=20, pool_recycle=280, pool_pre_ping=True)

async_str_conn = f'mysql+asyncmy://{username}:{password}@{server}:{port}/{database}'
async_engine = create_async_engine(async_str_conn, pool_timeout=20, pool_recycle=280, pool_pre_ping=True)

Base = automap_base()
Base.prepare(autoload_with=engine)

LojaML = Base.classes.ml_loja
PedidoML = Base.classes.ml_pedidos
PedidoItemML = Base.classes.ml_pedidos_itens
PedidoPgtoML = Base.classes.ml_pedidos_pagamentos
PedidoEnvioML = Base.classes.ml_pedidos_envios
PedidoDevolucaoML = Base.classes.ml_pedidos_devolucao
PedidoDanfeML = Base.classes.ml_nota_fiscal
FatPeriodosML = Base.classes.ml_faturamento_periodos
FatDocumentosML = Base.classes.ml_faturamento_documentos
FatResumoML = Base.classes.ml_faturamento_resumo
FatDetalhesML = Base.classes.ml_faturamento_detalhes
FatLogFullML = Base.classes.ml_faturamento_logistica_full
FatGarantiasML = Base.classes.ml_faturamento_garantias
LogsML = Base.classes.ml_logs

try:
    async_session = AsyncSession(async_engine, expire_on_commit=False)
except Exception as err:
    logging.error(f'Não foi possível conectar ao banco de dados. Erro: {err}')
