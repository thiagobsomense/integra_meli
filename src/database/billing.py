import json
import warnings
from datetime import datetime
from sqlalchemy import select, update
from sqlalchemy import exc as sa_exc
from database.conn import FatPeriodosML, FatDocumentosML, FatResumoML, FatDetalhesML, FatGarantiasML, FatLogFullML


async def add_periods(session, user_id, group, document_type, billing):
    data = {
        'user_id': user_id,
        'key': billing['key'],
        'group': group,
        'document_type': document_type,
        'amount': billing['amount'],
        'unpaid_amount': billing['unpaid_amount'],
        'period_date_from': billing['period']['date_from'],
        'period_date_to': billing['period']['date_to'],
        'expiration_date': billing['expiration_date'],
        'debt_expiration_date': billing['debt_expiration_date'],
        'debt_expiration_date_move_reason': billing['debt_expiration_date_move_reason'],
        'debt_expiration_date_move_reason_description': billing['debt_expiration_date_move_reason_description'],
        'period_status': billing['period_status']
    }

    session.add(FatPeriodosML(data_atualizacao=datetime.now(), **data))


async def update_periods(session, id, billing):
    data = {
        'amount': billing['amount'],
        'unpaid_amount': billing['unpaid_amount'],
        'expiration_date': billing['expiration_date'],
        'debt_expiration_date': billing['debt_expiration_date'],
        'debt_expiration_date_move_reason': billing['debt_expiration_date_move_reason'],
        'debt_expiration_date_move_reason_description': billing['debt_expiration_date_move_reason_description'],
        'period_status': billing['period_status'],
        'data_atualizacao': datetime.now()
    }

    await session.execute(update(FatPeriodosML).where(FatPeriodosML.id == id).values(data))


async def create_or_update_periods(session, user_id, group, document_type, billing):
    billing_key = str(billing['key'])
    query = select(FatPeriodosML).where(FatPeriodosML.user_id == user_id, FatPeriodosML.key ==
                                        billing_key, FatPeriodosML.group == group, FatPeriodosML.document_type == document_type)
    result = (await session.scalars(query)).first()

    if not result:
        await add_periods(session, user_id, group, document_type, billing)
        return 'create'
    else:
        # if any(x.period_status == 'OPEN' for x in result): para scalars all()
        if result.period_status == 'OPEN':
            await update_periods(session, result.id, billing)
            return 'update'


async def add_documents(session, user_id, key, group, document_type, document):
    data = {
        'user_id': user_id,
        'key': key,
        'group': group,
        'document_type': document_type,
        'document_id': document['id'],
        'associated_document_id': document['associated_document_id'],
        'expiration_date': document['expiration_date'],
        'amount': document['amount'],
        'unpaid_amount': document['unpaid_amount'],
        'document_status': document['document_status'],
        'site_id': document['site_id'],
        'period_date_from': document['period']['date_from'],
        'period_date_to': document['period']['date_to'],
        'currency_id': document['currency_id'],
        'count_details': document['count_details'],
        'files_json': json.dumps(document['files'])
    }

    session.add(FatDocumentosML(data_atualizacao=datetime.now(), **data))
    query = update(FatPeriodosML).where(FatPeriodosML.user_id == user_id, FatPeriodosML.key == key, FatPeriodosML.group ==
                                        group, FatPeriodosML.document_type == document_type).values(data_atualizacao=datetime.now(), is_documents=True)
    await session.execute(query)


async def update_documents(session, user_id, document):
    data = {
        'associated_document_id': document['associated_document_id'],
        'expiration_date': document['expiration_date'],
        'amount': document['amount'],
        'unpaid_amount': document['unpaid_amount'],
        'document_status': document['document_status'],
        'period_date_from': document['period']['date_from'],
        'period_date_to': document['period']['date_to'],
        'count_details': document['count_details'],
        'files_json': json.dumps(document['files'])
    }

    doc_id = str(document['id'])
    query = update(FatDocumentosML).where(FatDocumentosML.user_id == user_id, FatDocumentosML.document_id == doc_id).values(data_atualizacao=datetime.now(), **data)
    await session.execute(query)


async def create_or_update_documents(session, user_id, key, group, document_type, document):
    doc_id = str(document['id'])
    query = select(FatDocumentosML).where(FatDocumentosML.user_id == user_id, FatDocumentosML.document_id == doc_id)
    result = (await session.scalars(query)).first()

    if not result:
        await add_documents(session, user_id, key, group, document_type, document)
        return 'create'
    else:
        await update_documents(session, document, result.id)
        return 'update'


async def add_summary(session, user_id, key, group, document_type, response):
    data = {
        'user_id': user_id,
        'key': key,
        'group': group,
        'document_type': document_type,
        'period_date_from': response['period']['date_from'],
        'period_date_to': response['period']['date_to'],
        'expiration_date': response['period']['expiration_date'],
        'amount': response['summary']['amount'],
        'credit_note': response['summary']['credit_note'],
        'tax': response['summary']['tax'],
        'bonuses_json': json.dumps(response['summary']['bonuses']),
        'charges_json': json.dumps(response['summary']['charges'])
    }

    session.add(FatResumoML(data_atualizacao=datetime.now(), **data))
    query = update(FatPeriodosML).where(FatPeriodosML.user_id == user_id, FatPeriodosML.key == key, FatPeriodosML.group ==
                                        group, FatPeriodosML.document_type == document_type).values(data_atualizacao=datetime.now(), is_summary=True)
    await session.execute(query)


async def update_summary(session, user_id, key, group, document_type, response):
    data = {
        'period_date_from': response['period']['date_from'],
        'period_date_to': response['period']['date_to'],
        'expiration_date': response['period']['expiration_date'],
        'amount': response['summary']['amount'],
        'credit_note': response['summary']['credit_note'],
        'tax': response['summary']['tax'],
        'bonuses_json': json.dumps(response['summary']['bonuses']),
        'charges_json': json.dumps(response['summary']['charges'])
    }

    query = update(FatResumoML).where(FatResumoML.user_id == user_id, FatResumoML.key == key, FatResumoML.group ==
                                        group, FatResumoML.document_type == document_type).values(data_atualizacao=datetime.now(), **data)
    await session.execute(query)


async def add_details(session, user_id, key, group, document_type, response):
    shipping_info = response['shipping_info']

    data = {
        'user_id': user_id,
        'key': key,
        'group': group,
        'document_type': document_type,
        'legal_document_number': response['charge_info']['legal_document_number'],
        'legal_document_status': response['charge_info']['legal_document_status'],
        'legal_document_status_description': response['charge_info']['legal_document_status_description'],
        'creation_date_time': response['charge_info']['creation_date_time'],
        'detail_id': response['charge_info']['detail_id'],
        'movement_id': response['charge_info']['movement_id'] if group == 'MP' else None,
        'transaction_detail': response['charge_info']['transaction_detail'],
        'debited_from_operation': None if group == 'MP' else response['charge_info']['debited_from_operation'],
        'debited_from_operation_description': None if group == 'MP' else response['charge_info']['debited_from_operation_description'],
        'status': response['charge_info']['status'],
        'status_description': response['charge_info']['status_description'],
        'charge_bonified_id': response['charge_info']['charge_bonified_id'],
        'detail_amount': response['charge_info']['detail_amount'],
        'detail_type': response['charge_info']['detail_type'],
        'detail_sub_type': response['charge_info']['detail_sub_type'],
        'charge_amount_without_discount': 0 if group == 'MP' else response['discount_info']['charge_amount_without_discount'],
        'discount_amount': 0 if group == 'MP' else response['discount_info']['discount_amount'],
        'discount_reason': None if group == 'MP' else response['discount_info']['discount_reason'],
        'sales_info_json': None if group == 'MP' else json.dumps(response['sales_info']),
        'shipping_id': None if shipping_info == None else response['shipping_info']['shipping_id'],
        'pack_id': None if shipping_info == None else response['shipping_info']['pack_id'],
        'receiver_shipping_cost': None if shipping_info == None else response['shipping_info']['receiver_shipping_cost'],
        'items_info_json': None if group == 'MP' else json.dumps(response['items_info']),
        'operation_info_json': json.dumps(response['operation_info']) if group == 'MP' else None,
        'perception_info_json': json.dumps(response['perception_info']) if group == 'MP' else None,
        'document_id': response['document_info']['document_id'],
        'marketplace': response['marketplace_info']['marketplace'],
        'currency_id': response['currency_info']['currency_id']
    }

    with warnings.catch_warnings():
        warnings.simplefilter('ignore', category=sa_exc.SAWarning)
        session.add(FatDetalhesML(data_atualizacao=datetime.now(), **data))
        query = update(FatPeriodosML).where(FatPeriodosML.user_id == user_id, FatPeriodosML.key == key, FatPeriodosML.group ==
                                            group, FatPeriodosML.document_type == document_type).values(data_atualizacao=datetime.now(), is_details=True)
        await session.execute(query)


async def update_details(session, user_id, response):
    data = {
        'legal_document_number': response['charge_info']['legal_document_number'],
        'legal_document_status': response['charge_info']['legal_document_status'],
        'legal_document_status_description': response['charge_info']['legal_document_status_description'],
        'debited_from_operation': response['charge_info']['debited_from_operation'] or None,
        'debited_from_operation_description': response['charge_info']['debited_from_operation_description'],
        'status': response['charge_info']['status'],
        'status_description': response['charge_info']['status_description'],
        'charge_bonified_id': response['charge_info']['charge_bonified_id']
    }

    detail_id = str(response['charge_info']['detail_id'])
    query = update(FatDetalhesML).where(FatDetalhesML.user_id == user_id, FatDetalhesML.detail_id == detail_id).values(data_atualizacao=datetime.now(), **data)
    await session.execute(query)


async def add_insurtech(session, user_id, key, group, document_type, response):
    data = {
        'user_id': user_id,
        'key': key,
        'group': group,
        'document_type': document_type,
        'legal_document_number': response['charge_info']['legal_document_number'],
        'legal_document_status': response['charge_info']['legal_document_status'],
        'legal_document_status_description': response['charge_info']['legal_document_status_description'],
        'creation_date_time': response['charge_info']['creation_date_time'],
        'detail_id': response['charge_info']['detail_id'],
        'detail_amount': response['charge_info']['detail_amount'],
        'transaction_detail': response['charge_info']['transaction_detail'],
        'status': response['charge_info']['status'],
        'status_description': response['charge_info']['status_description'],
        'charge_bonified_id': response['charge_info']['charge_bonified_id'],
        'detail_type': response['charge_info']['detail_type'],
        'detail_sub_type': response['charge_info']['detail_sub_type'],
        'concept_type': response['charge_info']['concept_type'],
        'warranty_info_json': json.dumps(response['warranty_info']),
        'prepaid_info_json': json.dumps(response['prepaid_info']),
        'document_id': response['document_info']['document_id']
    }

    session.add(FatGarantiasML(data_atualizacao=datetime.now(), **data))
    query = update(FatPeriodosML).where(FatPeriodosML.user_id == user_id, FatPeriodosML.key == key, FatPeriodosML.group ==
                                        group, FatPeriodosML.document_type == document_type).values(data_atualizacao=datetime.now(), is_insurtech=True)
    await session.execute(query)


async def update_insurtech(session, user_id, response):
    data = {
        'legal_document_number': response['charge_info']['legal_document_number'],
        'legal_document_status': response['charge_info']['legal_document_status'],
        'legal_document_status_description': response['charge_info']['legal_document_status_description'],
        'status': response['charge_info']['status'],
        'status_description': response['charge_info']['status_description'],
        'charge_bonified_id': response['charge_info']['charge_bonified_id'],
        'prepaid_info_json': json.dumps(response['prepaid_info'])
    }

    detail_id = str(response['charge_info']['detail_id'])
    query = update(FatGarantiasML).where(FatGarantiasML.user_id == user_id, FatGarantiasML.detail_id == detail_id).values(data_atualizacao=datetime.now(), **data)
    await session.execute(query)


async def add_fulfillment(session, user_id, key, group, document_type, response):
    data = {
        'user_id': user_id,
        'key': key,
        'group': group,
        'document_type': document_type,
        'legal_document_number': response['charge_info']['legal_document_number'],
        'legal_document_status': response['charge_info']['legal_document_status'],
        'legal_document_status_description': response['charge_info']['legal_document_status_description'],
        'creation_date_time': response['charge_info']['creation_date_time'],
        'detail_id': response['charge_info']['detail_id'],
        'detail_amount': response['charge_info']['detail_amount'],
        'transaction_detail': response['charge_info']['transaction_detail'],
        'charge_bonified_id': response['charge_info']['charge_bonified_id'],
        'detail_type': response['charge_info']['detail_type'],
        'detail_sub_type': response['charge_info']['detail_sub_type'],
        'concept_type': response['charge_info']['concept_type'],
        'payment_id': response['charge_info']['payment_id'],
        'type': response['fulfillment_info']['type'],
        'amount_per_unit': response['fulfillment_info']['amount_per_unit'],
        'sku': response['fulfillment_info']['sku'],
        'ean': response['fulfillment_info']['ean'],
        'item_id': response['fulfillment_info']['item_id'],
        'item_title': response['fulfillment_info']['item_title'],
        'variation': response['fulfillment_info']['variation'],
        'quantity': response['fulfillment_info']['quantity'],
        'volume_type': response['fulfillment_info']['volume_type'],
        'inventory_id': response['fulfillment_info']['inventory_id'],
        'inbound_id': response['fulfillment_info']['inbound_id'],
        'volume_unit': response['fulfillment_info']['volume_unit'],
        'amount_per_volume_unit': response['fulfillment_info']['amount_per_volume_unit'],
        'volume': response['fulfillment_info']['volume'],
        'volume_total': response['fulfillment_info']['volume_total'],
        'document_id': response['document_info']['document_id']
    }

    session.add(FatLogFullML(data_atualizacao=datetime.now(), **data))
    query = update(FatPeriodosML).where(FatPeriodosML.user_id == user_id, FatPeriodosML.key == key, FatPeriodosML.group ==
                                        group, FatPeriodosML.document_type == document_type).values(data_atualizacao=datetime.now(), is_fulfillment=True)
    await session.execute(query)


async def update_fulfillment(session, user_id, response):
    data = {
        'legal_document_number': response['charge_info']['legal_document_number'],
        'legal_document_status': response['charge_info']['legal_document_status'],
        'legal_document_status_description': response['charge_info']['legal_document_status_description'],
        'charge_bonified_id': response['charge_info']['charge_bonified_id']
    }

    detail_id = str(response['charge_info']['detail_id'])
    query = update(FatLogFullML).where(FatLogFullML.user_id == user_id, FatLogFullML.detail_id == detail_id).values(data_atualizacao=datetime.now(), **data)
    await session.execute(query)
