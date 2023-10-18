# coding: utf-8
from sqlalchemy import BigInteger, Column, DECIMAL, Float, ForeignKey, ForeignKeyConstraint, Index, Integer, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ChargeInfoMercadoLivre(Base):
    __tablename__ = 'charge_info_mercado_livre'

    document_id = Column(String(255), primary_key=True, nullable=False)
    user_id = Column(String(255), primary_key=True, nullable=False)
    legal_document_number = Column(String(100))
    legal_document_status = Column(String(100))
    legal_document_status_description = Column(String(100))
    creation_date_time = Column(TIMESTAMP)
    detail_id = Column(BigInteger)
    transaction_detail = Column(String(100))
    debited_from_operation = Column(String(100))
    debited_from_operation_description = Column(String(100))
    status = Column(String(100))
    status_description = Column(String(100))
    charge_bonified_id = Column(String(100))
    detail_amount = Column(DECIMAL(10, 2))
    detail_type = Column(String(100))
    detail_sub_type = Column(String(100))
    charge_amount_without_discount = Column(DECIMAL(10, 2))
    discount_amount = Column(DECIMAL(10, 2))
    discount_reason = Column(String(100))
    shipping_id = Column(String(100))
    pack_id = Column(String(100))
    receiver_shipping_cost = Column(DECIMAL(10, 2))
    marketplace = Column(String(100))
    currency_id = Column(String(100))
    data_atualizacao = Column(TIMESTAMP)
    data_insercao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255), unique=True)
    senha = Column(String(255))
    data_criacao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    data_vencimento = Column(TIMESTAMP, nullable=False)
    ativo = Column(TINYINT(1), server_default=text("'1'"))
    root = Column(TINYINT(1), server_default=text("'0'"))
    modulo_shopee = Column(TINYINT(1), server_default=text("'0'"))
    modulo_bling = Column(TINYINT(1), server_default=text("'0'"))
    modulo_ads = Column(TINYINT(1), server_default=text("'0'"))
    modulo_api = Column(TINYINT(1), server_default=text("'0'"))
    modulo_mercado_livre = Column(TINYINT(1), server_default=text("'0'"))
    qtd_lojas = Column(Integer, server_default=text("'3'"))
    qtd_lojas_mercadolivreint = Column(Integer, server_default=text("'3'"))
    email = Column(String(255))
    telefone = Column(String(255))
    cnpj = Column(String(255))
    modulo_shein = Column(TINYINT(1), server_default=text("'0'"))


class LojaMercadoLivre(Base):
    __tablename__ = 'loja_mercado_livre'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    access_token = Column(String(255))
    token_type = Column(String(255))
    expires_in = Column(String(255))
    user_id = Column(String(255), index=True)
    refresh_token = Column(String(255))
    data_insercao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


class LojaShopee(Base):
    __tablename__ = 'loja_shopee'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    acess_token = Column(String(255))
    refresh_token = Column(String(255))
    shop_id = Column(Integer, unique=True)
    data_criacao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    ativo = Column(TINYINT(1), server_default=text("'1'"))
    is_conected = Column(TINYINT(1), server_default=text("'1'"))


class PagamentosShopee(Base):
    __tablename__ = 'pagamentos_shopee'
    __table_args__ = (
        Index('ix_shop_id_order_sn', 'shop_id', 'order_sn'),
    )

    shop_id = Column(Integer, primary_key=True, nullable=False, index=True)
    transaction_id = Column(String(255), primary_key=True, nullable=False)
    status = Column(String(255))
    wallet_type = Column(String(255))
    transaction_type = Column(String(255))
    amount = Column(DECIMAL(15, 2))
    current_balance = Column(DECIMAL(15, 2))
    create_time = Column(String(255), index=True)
    reason = Column(String(255))
    order_sn = Column(String(255))
    refund_sn = Column(String(255))
    withdrawal_type = Column(String(255))
    transaction_fee = Column(DECIMAL(15, 2))
    description = Column(String(255))
    withdrawal_id = Column(String(255))
    root_withdrawal_id = Column(String(255))
    data_atualizacao = Column(TIMESTAMP)
    data_insercao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


class Pedido(Base):
    __tablename__ = 'pedidos'

    shop_id = Column(Integer, primary_key=True, nullable=False)
    order_sn = Column(String(255), primary_key=True, nullable=False)
    order_status = Column(String(255))
    data_criacao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    data_atualizacao = Column(TIMESTAMP)


class PedidosDado(Pedido):
    __tablename__ = 'pedidos_dados'
    __table_args__ = (
        ForeignKeyConstraint(['shop_id', 'order_sn'], ['pedidos.shop_id', 'pedidos.order_sn']),
        Index('ix_pd_shop_id_order_sn', 'shop_id', 'order_sn')
    )

    shop_id = Column(Integer, primary_key=True, nullable=False)
    order_sn = Column(String(255), primary_key=True, nullable=False)
    cancel_by = Column(String(255))
    cancel_reason = Column(String(255))
    create_time = Column(TIMESTAMP)
    currency = Column(String(255))
    days_to_ship = Column(Integer)
    pay_time = Column(TIMESTAMP)
    payment_method = Column(String(255))
    prescription_check_status = Column(String(255))
    region = Column(String(255))
    reverse_shipping_fee = Column(DECIMAL(15, 2))
    ship_by_date = Column(TIMESTAMP)
    update_time = Column(TIMESTAMP)
    package_number = Column(String(255))
    logistics_status = Column(String(255))
    shipping_carrier = Column(String(255))
    parcel_chargeable_weight_gram = Column(DECIMAL(15, 2))
    data_criacao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    data_atualizacao = Column(TIMESTAMP)


class PedidosEntrega(Pedido):
    __tablename__ = 'pedidos_entrega'
    __table_args__ = (
        ForeignKeyConstraint(['shop_id', 'order_sn'], ['pedidos.shop_id', 'pedidos.order_sn']),
    )

    shop_id = Column(Integer, primary_key=True, nullable=False)
    order_sn = Column(String(255), primary_key=True, nullable=False)
    ra_name = Column(String(255))
    ra_phone = Column(String(255))
    ra_town = Column(String(255))
    ra_district = Column(String(255))
    ra_city = Column(String(255))
    ra_state = Column(String(255))
    ra_region = Column(String(255))
    ra_zipcode = Column(String(255))
    ra_full_address = Column(String(255))
    data_criacao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    data_atualizacao = Column(TIMESTAMP)


class PedidosEscrow(Pedido):
    __tablename__ = 'pedidos_escrow'
    __table_args__ = (
        ForeignKeyConstraint(['shop_id', 'order_sn'], ['pedidos.shop_id', 'pedidos.order_sn']),
    )

    shop_id = Column(Integer, primary_key=True, nullable=False)
    order_sn = Column(String(255), primary_key=True, nullable=False)
    actual_shipping_fee = Column(DECIMAL(15, 2))
    buyer_paid_shipping_fee = Column(DECIMAL(15, 2))
    buyer_total_amount = Column(DECIMAL(15, 2))
    buyer_transaction_fee = Column(DECIMAL(15, 2))
    campaign_fee = Column(DECIMAL(15, 2))
    coins = Column(DECIMAL(15, 2))
    commission_fee = Column(DECIMAL(15, 2))
    cost_of_goods_sold = Column(DECIMAL(15, 2))
    credit_card_promotion = Column(DECIMAL(15, 2))
    credit_card_transaction_fee = Column(DECIMAL(15, 2))
    cross_border_tax = Column(DECIMAL(15, 2))
    delivery_seller_protection_fee_premium_amount = Column(DECIMAL(15, 2))
    drc_adjustable_refund = Column(DECIMAL(15, 2))
    escrow_amount = Column(DECIMAL(15, 2))
    escrow_tax = Column(DECIMAL(15, 2))
    estimated_shipping_fee = Column(DECIMAL(15, 2))
    final_escrow_product_gst = Column(DECIMAL(15, 2))
    final_escrow_shipping_gst = Column(DECIMAL(15, 2))
    final_product_protection = Column(DECIMAL(15, 2))
    final_product_vat_tax = Column(DECIMAL(15, 2))
    final_return_to_seller_shipping_fee = Column(DECIMAL(15, 2))
    final_shipping_fee = Column(DECIMAL(15, 2))
    final_shipping_vat_tax = Column(DECIMAL(15, 2))
    order_chargeable_weight = Column(DECIMAL(15, 2))
    original_cost_of_goods_sold = Column(DECIMAL(15, 2))
    original_price = Column(DECIMAL(15, 2))
    original_shopee_discount = Column(DECIMAL(15, 2))
    payment_promotion = Column(DECIMAL(15, 2))
    reverse_shipping_fee = Column(DECIMAL(15, 2))
    rsf_seller_protection_fee_claim_amount = Column(DECIMAL(15, 2))
    rsf_seller_protection_fee_premium_amount = Column(DECIMAL(15, 2))
    seller_coin_cash_back = Column(DECIMAL(15, 2))
    seller_discount = Column(DECIMAL(15, 2))
    seller_lost_compensation = Column(DECIMAL(15, 2))
    seller_return_refund = Column(DECIMAL(15, 2))
    seller_shipping_discount = Column(DECIMAL(15, 2))
    seller_transaction_fee = Column(DECIMAL(15, 2))
    service_fee = Column(DECIMAL(15, 2))
    shipping_fee_discount_from_3pl = Column(DECIMAL(15, 2))
    shopee_discount = Column(DECIMAL(15, 2))
    shopee_shipping_rebate = Column(DECIMAL(15, 2))
    voucher_from_seller = Column(DECIMAL(15, 2))
    voucher_from_shopee = Column(DECIMAL(15, 2))
    data_criacao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    data_atualizacao = Column(TIMESTAMP)


class PedidosNota(Pedido):
    __tablename__ = 'pedidos_nota'
    __table_args__ = (
        ForeignKeyConstraint(['shop_id', 'order_sn'], ['pedidos.shop_id', 'pedidos.order_sn']),
    )

    shop_id = Column(Integer, primary_key=True, nullable=False)
    order_sn = Column(String(255), primary_key=True, nullable=False)
    ia_number = Column(String(255))
    ia_series_number = Column(String(255))
    ia_access_key = Column(String(255))
    ia_issue_date = Column(TIMESTAMP)
    ia_total_value = Column(DECIMAL(15, 2))
    ia_products_total_value = Column(DECIMAL(15, 2))
    ia_tax_code = Column(String(255))
    data_criacao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    data_atualizacao = Column(TIMESTAMP)


class PedidosTrackingNumber(Pedido):
    __tablename__ = 'pedidos_tracking_number'
    __table_args__ = (
        ForeignKeyConstraint(['shop_id', 'order_sn'], ['pedidos.shop_id', 'pedidos.order_sn']),
    )

    shop_id = Column(Integer, primary_key=True, nullable=False)
    order_sn = Column(String(255), primary_key=True, nullable=False)
    tracking_number = Column(String(255))
    data_criacao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    data_atualizacao = Column(TIMESTAMP)


class ProcessamentoShopeeGeral(Base):
    __tablename__ = 'processamento_shopee_geral'

    seq = Column(BigInteger, primary_key=True)
    qtd_lojas = Column(Integer, nullable=False)
    rotina = Column(String(255), nullable=False, index=True)
    processo = Column(String(255), nullable=False, index=True)
    periodo_processo_ini = Column(TIMESTAMP, nullable=False)
    periodo_processo_fim = Column(TIMESTAMP, nullable=False)
    data_ini = Column(TIMESTAMP, nullable=False)
    data_fim = Column(TIMESTAMP)
    status_processo = Column(String(25), nullable=False, index=True)
    descricao = Column(String(255))


class ReturnShopee(Base):
    __tablename__ = 'return_shopee'
    __table_args__ = (
        Index('shop_id', 'shop_id', 'return_sn'),
        Index('ix_return_shopee_order_shop2', 'shop_id', 'order_sn')
    )

    shop_id = Column(Integer, primary_key=True, nullable=False)
    return_sn = Column(String(255), primary_key=True, nullable=False)
    reason = Column(String(255))
    text_reason = Column(Text)
    refund_amount = Column(DECIMAL(15, 2))
    create_time = Column(String(255), index=True)
    update_time = Column(String(255))
    status = Column(String(255))
    due_date = Column(String(255))
    tracking_number = Column(String(255), index=True)
    amount_before_discount = Column(DECIMAL(15, 2))
    order_sn = Column(String(255), index=True)
    return_ship_due_date = Column(String(255))
    return_seller_due_date = Column(String(255))
    negotiation_status = Column(String(255))
    seller_proof_status = Column(String(255))
    seller_compensation_status = Column(String(255))
    data_atualizacao = Column(TIMESTAMP)
    data_insercao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


class TrackingInfoIten(Base):
    __tablename__ = 'tracking_info_itens'

    shop_id = Column(Integer, primary_key=True, nullable=False, index=True)
    order_sn = Column(String(255), primary_key=True, nullable=False, index=True)
    logistics_status = Column(String(255))
    update_time = Column(TIMESTAMP, primary_key=True, nullable=False, index=True)
    description = Column(Text)
    data_atualizacao = Column(TIMESTAMP)
    data_insercao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


class TrackingInfoPai(Base):
    __tablename__ = 'tracking_info_pai'

    shop_id = Column(Integer, primary_key=True, nullable=False, index=True)
    order_sn = Column(String(255), primary_key=True, nullable=False, index=True)
    logistics_status = Column(String(255))
    data_atualizacao = Column(TIMESTAMP)
    data_insercao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


class ClienteLojaMercadoLivre(Base):
    __tablename__ = 'cliente_loja_mercado_livre'

    id_cliente = Column(ForeignKey('clientes.id'), primary_key=True, nullable=False)
    id_loja = Column(ForeignKey('loja_mercado_livre.id'), primary_key=True, nullable=False, index=True)
    data_criacao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    cliente = relationship('Cliente')
    loja_mercado_livre = relationship('LojaMercadoLivre')


class ClienteLojaShopee(Base):
    __tablename__ = 'cliente_loja_shopee'

    id_cliente = Column(ForeignKey('clientes.id'), primary_key=True, nullable=False)
    id_loja = Column(ForeignKey('loja_shopee.id'), primary_key=True, nullable=False, index=True)
    data_criacao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    cliente = relationship('Cliente')
    loja_shopee = relationship('LojaShopee')


class PedidosIten(Base):
    __tablename__ = 'pedidos_itens'
    __table_args__ = (
        ForeignKeyConstraint(['shop_id', 'order_sn'], ['pedidos.shop_id', 'pedidos.order_sn']),
        Index('shop_id', 'shop_id', 'order_sn'),
        Index('shop_id_2', 'shop_id', 'item_id', 'model_id')
    )

    shop_id = Column(Integer, primary_key=True, nullable=False)
    order_sn = Column(String(255), primary_key=True, nullable=False)
    seq = Column(Integer, primary_key=True, nullable=False)
    activity_id = Column(Text)
    activity_type = Column(String(50))
    discount_from_coin = Column(DECIMAL(10, 2))
    discount_from_voucher_seller = Column(DECIMAL(10, 2))
    discount_from_voucher_shopee = Column(DECIMAL(10, 2))
    discounted_price = Column(DECIMAL(10, 2))
    is_b2c_shop_item = Column(TINYINT(1))
    is_main_item = Column(TINYINT(1))
    item_id = Column(String(255), index=True)
    item_name = Column(Text)
    item_sku = Column(String(50), index=True)
    model_id = Column(String(255))
    model_name = Column(String(255))
    model_sku = Column(String(50))
    original_price = Column(DECIMAL(10, 2))
    quantity_purchased = Column(Integer)
    seller_discount = Column(DECIMAL(10, 2))
    shopee_discount = Column(DECIMAL(10, 2))
    data_atualizacao = Column(TIMESTAMP)
    data_insercao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    shop = relationship('Pedido')


class ItensShopee(PedidosIten):
    __tablename__ = 'itens_shopee'
    __table_args__ = (
        ForeignKeyConstraint(['shop_id', 'item_id', 'model_id'], ['pedidos_itens.shop_id', 'pedidos_itens.item_id', 'pedidos_itens.model_id']),
        Index('ix_itens_shopee_shop_item', 'shop_id', 'item_id')
    )

    shop_id = Column(Integer, primary_key=True, nullable=False, index=True)
    item_id = Column(String(255), primary_key=True, nullable=False)
    item_sku = Column(String(255), nullable=False)
    model_id = Column(String(255), primary_key=True, nullable=False)
    model_sku = Column(String(255), nullable=False)
    preco_custo = Column(DECIMAL(10, 2), server_default=text("'0.00'"))
    data_atualizacao = Column(TIMESTAMP)
    data_insercao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


class PedidosMercadoLivre(Base):
    __tablename__ = 'pedidos_mercado_livre'

    user_id = Column(ForeignKey('loja_mercado_livre.user_id'), primary_key=True, nullable=False)
    id = Column(String(255), primary_key=True, nullable=False)
    fullfiled = Column(TINYINT(1))
    expiration_date = Column(TIMESTAMP)
    date_closed = Column(TIMESTAMP)
    last_updated = Column(TIMESTAMP)
    date_created = Column(TIMESTAMP)
    shipping = Column(String(255))
    status_pedido = Column(String(255))
    total_amount = Column(DECIMAL(10, 2))
    paid_amount = Column(DECIMAL(10, 2))
    data_atualizacao = Column(TIMESTAMP)
    data_insercao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    user = relationship('LojaMercadoLivre')


class ProcessamentoShopee(Base):
    __tablename__ = 'processamento_shopee'

    seq_geral = Column(ForeignKey('processamento_shopee_geral.seq'), primary_key=True, nullable=False)
    shop_id = Column(Integer, primary_key=True, nullable=False, index=True)
    periodo_processo_ini = Column(TIMESTAMP, nullable=False)
    periodo_processo_fim = Column(TIMESTAMP, nullable=False)
    data_ini = Column(TIMESTAMP, nullable=False)
    data_fim = Column(TIMESTAMP)
    status_processo = Column(String(25), nullable=False, index=True)
    descricao = Column(String(255))

    processamento_shopee_geral = relationship('ProcessamentoShopeeGeral')


class ReturnShopeeIten(Base):
    __tablename__ = 'return_shopee_itens'
    __table_args__ = (
        ForeignKeyConstraint(['shop_id', 'return_sn'], ['return_shopee.shop_id', 'return_shopee.return_sn']),
        Index('shop_id', 'shop_id', 'return_sn')
    )

    cont = Column(Integer, primary_key=True, nullable=False)
    shop_id = Column(Integer, primary_key=True, nullable=False)
    return_sn = Column(String(255), primary_key=True, nullable=False)
    item_id = Column(String(255))
    model_id = Column(Text)
    name = Column(Text)
    amount = Column(DECIMAL(15, 2))
    item_price = Column(DECIMAL(15, 2))
    is_add_on_deal = Column(TINYINT(1))
    is_main_item = Column(TINYINT(1))
    item_sku = Column(String(255))
    variation_sku = Column(String(255))
    add_on_deal_id = Column(String(255))
    data_atualizacao = Column(TIMESTAMP)
    data_insercao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    shop = relationship('ReturnShopee')


t_sales_info_mercado_livre = Table(
    'sales_info_mercado_livre', metadata,
    Column('document_id', String(255), nullable=False),
    Column('user_id', String(255), nullable=False),
    Column('seq', Integer),
    Column('order_id', String(255)),
    Column('operation_id', BigInteger),
    Column('sale_date_time', TIMESTAMP),
    Column('sales_channel', String(50)),
    Column('payer_nickname', String(100)),
    Column('state_name', String(50)),
    Column('transaction_amount', DECIMAL(10, 2)),
    Column('charge_info_id', Integer),
    Column('data_atualizacao', TIMESTAMP),
    Column('data_insercao', TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")),
    ForeignKeyConstraint(['document_id', 'user_id'], ['charge_info_mercado_livre.document_id', 'charge_info_mercado_livre.user_id']),
    Index('document_id', 'document_id', 'user_id')
)


class PedidosItensMercadoLivre(Base):
    __tablename__ = 'pedidos_itens_mercado_livre'
    __table_args__ = (
        ForeignKeyConstraint(['user_id', 'id_pedido'], ['pedidos_mercado_livre.user_id', 'pedidos_mercado_livre.id']),
    )

    user_id = Column(String(255), primary_key=True, nullable=False)
    id_pedido = Column(String(255), primary_key=True, nullable=False)
    seq = Column(Integer, primary_key=True, nullable=False)
    id = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    category_id = Column(String(255), nullable=False)
    variation_id = Column(String(255), nullable=False)
    seller_custom_field = Column(String(255))
    global_price = Column(DECIMAL(10, 2), server_default=text("'0.00'"))
    net_weight = Column(String(255))
    warranty = Column(String(255))
    condition_item = Column(String(255))
    seller_sku = Column(String(255))
    quantity = Column(DECIMAL(10, 0))
    unit_price = Column(DECIMAL(10, 2), server_default=text("'0.00'"))
    full_unit_price = Column(DECIMAL(10, 2), server_default=text("'0.00'"))
    currency_id = Column(String(255))
    manufacturing_days = Column(String(255))
    picked_quantity = Column(String(255))
    listing_type_id = Column(String(255))
    base_exchange_rate = Column(String(255))
    base_currency_id = Column(String(255))
    bundle = Column(String(255))
    element_id = Column(String(255))
    data_atualizacao = Column(TIMESTAMP)
    data_insercao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    user = relationship('PedidosMercadoLivre')


class PedidosPagamentosMercadoLivre(Base):
    __tablename__ = 'pedidos_pagamentos_mercado_livre'
    __table_args__ = (
        ForeignKeyConstraint(['user_id', 'id_pedido'], ['pedidos_mercado_livre.user_id', 'pedidos_mercado_livre.id']),
    )

    user_id = Column(String(255), primary_key=True, nullable=False)
    id_pedido = Column(String(255), primary_key=True, nullable=False)
    id = Column(BigInteger, primary_key=True, nullable=False)
    reason = Column(String(255))
    status_code = Column(String(255))
    total_paid_amount = Column(Float)
    operation_type = Column(String(255))
    transaction_amount = Column(Float)
    transaction_amount_refunded = Column(Integer)
    date_approved = Column(String(255))
    collector_id = Column(String(255))
    coupon_id = Column(String(255))
    installments = Column(Integer)
    authorization_code = Column(String(255))
    taxes_amount = Column(Float)
    date_last_modified = Column(String(255))
    coupon_amount = Column(Float)
    shipping_cost = Column(Float)
    installment_amount = Column(String(255))
    date_created = Column(String(255))
    activation_uri = Column(String(255))
    overpaid_amount = Column(Float)
    card_id = Column(String(255))
    status_detail = Column(String(255))
    issuer_id = Column(String(255))
    payment_method_id = Column(String(255))
    payment_type = Column(String(255))
    deferred_period = Column(String(255))
    atm_transfer_reference_transaction_id = Column(String(255))
    atm_transfer_reference_company_id = Column(String(255))
    site_id = Column(String(255))
    payer_id = Column(BigInteger)
    order_id = Column(BigInteger)
    currency_id = Column(String(255))
    status = Column(String(255))
    transaction_order_id = Column(String(255))
    data_atualizacao = Column(TIMESTAMP)
    data_insercao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    user = relationship('PedidosMercadoLivre')
