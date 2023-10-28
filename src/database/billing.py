import json
from datetime import datetime
from sqlalchemy import select, update
from database.conn import FatPeriodosML


async def add_periods(session, user_id, billing):
    data = {
        'user_id': user_id,
        'key': billing['key'],
        'amount': billing['amount'],
        'unpaid_amount': billing['unpaid_amount'],
        'period_date_from': billing['period']['period_date_from'],
        'period_date_to': billing['period']['period_date_to'],
        'expiration_date': billing['expiration_date'],
        'debt_expiration_date': billing['debt_expiration_date'],
        'debt_expiration_date_move_reason': billing['debt_expiration_date_move_reason'],
        'debt_expiration_date_move_reason_description': billing['debt_expiration_date_move_reason_description'],
        'period_status': billing['period_status'],
    }

    periods = session.add(FatPeriodosML(data_atualizacao=datetime.now(), **data))

    return periods


async def update_periods(session, billing):
    data = {
        'expiration_date': billing['expiration_date'],
        'debt_expiration_date': billing['debt_expiration_date'],
        'debt_expiration_date_move_reason': billing['debt_expiration_date_move_reason'],
        'debt_expiration_date_move_reason_description': billing['debt_expiration_date_move_reason_description'],
        'period_status': billing['period_status'],
    }

    await session.execute(update(FatPeriodosML).where(FatPeriodosML.key == str(billing['key'])).values(data))


async def create_or_update_periods(session, billing):
    periods = await session.execute(select(FatPeriodosML).filter(FatPeriodosML.key == str(billing['key'])))
    if len(periods.fetchall()) == 0:
        await add_periods(session, billing)
        return 'create'
    else:
        for x in periods.scalars():
            if x.status == 'OPNE':
                await update_periods(session, billing)
                return 'update'
            
            