import aiohttp
import asyncio
from datetime import datetime
from math import ceil
from sqlalchemy import delete
from database.conn import *
from database.billing import *
from config.logging import logger


groups = ['ML', 'MP']
document_types = ['BILL', 'CREDIT_NOTE']


async def get_documets(billing_api, session, user_id, key, group, document_type, operation):
    try:
        if operation:
            async with aiohttp.ClientSession() as client_session:
                api_call = await billing_api.billing_documents(client_session, key, group, document_type)
                
                if isinstance(api_call, dict):
                    offset = 0
                    total = api_call['total']
                    limit = api_call['limit']
                    max_pages = ceil(total / limit)

                    tasks = []
                    for page in range(0, max_pages):
                        tasks.append(asyncio.create_task(billing_api.billing_documents(client_session, key, group, document_type, offset)))
                        offset += limit

                    results = await asyncio.gather(*tasks)
                    for result in results:
                        for document in result['results']:
                            
                            if operation == 'create':
                                await add_documents(session, user_id, key, group, document_type, document)

                            if operation == 'update':
                                await update_documents(session, user_id, document)

                    # logger.info(f'Tarefa Concluída - {count} novos registros', extra={'user_id': user_id, 'body': None, 'init_at': init_at, 'end_at': datetime.now()})
                
                else:
                    # logger.warning('Falha na solicitação', extra={'user_id': user_id, 'body': f'status: {api_call}', 'init_at': init_at, 'end_at': datetime.now()})
                    print(api_call)

    except Exception as err:
        #logger.error('Falha na execução', extra={'user_id': user_id, 'body': err, 'init_at': init_at, 'end_at': datetime.now()})
        print(err)


async def get_summary(billing_api, session, user_id, key, group, document_type, operation):
    try:
        if operation:
            async with aiohttp.ClientSession() as client_session:
                response = await billing_api.billing_summary(client_session, key, group, document_type)

                if isinstance(response, dict):
                    if operation == 'create':
                        await add_summary(session, user_id, key, group, document_type, response)
                        # logger.info(f'Tarefa Concluída - {count} novos registros', extra={'user_id': user_id, 'body': None, 'init_at': init_at, 'end_at': datetime.now()})
                
                    if operation == 'update':
                        await update_summary(session, user_id, key, group, document_type, response)
                        # logger.info(f'Tarefa Concluída - {count} novos registros', extra={'user_id': user_id, 'body': None, 'init_at': init_at, 'end_at': datetime.now()})
                
                else:
                    print(response)
                    # logger.warning('Falha na solicitação', extra={'user_id': user_id, 'body': f'status: {api_call}', 'init_at': init_at, 'end_at': datetime.now()})

    except Exception as err:
        print(err)
        #logger.error('Falha na execução', extra={'user_id': user_id, 'body': err, 'init_at': init_at, 'end_at': datetime.now()})


async def get_details(billing_api, session, user_id, key, group, document_type, operation):
    try:
        if operation:
            async with aiohttp.ClientSession() as client_session:
                api_call = await billing_api.billing_details(client_session, key, group, document_type)
                
                if isinstance(api_call, dict):
                    offset = 0
                    total = api_call['total']
                    limit = api_call['limit']
                    max_pages = ceil(total / limit)

                    tasks = []
                    for page in range(0, max_pages):
                        tasks.append(asyncio.create_task(billing_api.billing_details(client_session, key, group, document_type, offset)))
                        offset += limit

                    results = await asyncio.gather(*tasks)
                    print(results)
                    # for result in results:
                    #     for info in result['results']:
                            
                    #         if operation == 'create':
                    #             await add_details(session, user_id, key, group, document_type, info)

                    #         if operation == 'update':
                    #             await update_details(session, user_id, info)

                    # logger.info(f'Tarefa Concluída - {count} novos registros', extra={'user_id': user_id, 'body': None, 'init_at': init_at, 'end_at': datetime.now()})
                
                else:
                    # logger.warning('Falha na solicitação', extra={'user_id': user_id, 'body': f'status: {api_call}', 'init_at': init_at, 'end_at': datetime.now()})
                    print(api_call)

    except Exception as err:
        #logger.error('Falha na execução', extra={'user_id': user_id, 'body': err, 'init_at': init_at, 'end_at': datetime.now()})
        print(err)


async def get_insurtech(billing_api, session, user_id, key, group, document_type, operation):
    try:
        if operation:
            async with aiohttp.ClientSession() as client_session:
                api_call = await billing_api.billing_insurtech(client_session, key, group, document_type)
                
                if isinstance(api_call, dict):
                    offset = 0
                    total = api_call['total']
                    limit = api_call['limit']
                    max_pages = ceil(total / limit)

                    tasks = []
                    for page in range(0, max_pages):
                        tasks.append(asyncio.create_task(billing_api.billing_insurtech(client_session, key, group, document_type, offset)))
                        offset += limit

                    results = await asyncio.gather(*tasks)
                    for result in results:
                        for info in result['results']:
                            
                            if operation == 'create':
                                await add_insurtech(session, user_id, key, group, document_type, info)

                            if operation == 'update':
                                await update_insurtech(session, user_id, info)

                    # logger.info(f'Tarefa Concluída - {count} novos registros', extra={'user_id': user_id, 'body': None, 'init_at': init_at, 'end_at': datetime.now()})
                
                else:
                    # logger.warning('Falha na solicitação', extra={'user_id': user_id, 'body': f'status: {api_call}', 'init_at': init_at, 'end_at': datetime.now()})
                    print(api_call)

    except Exception as err:
        #logger.error('Falha na execução', extra={'user_id': user_id, 'body': err, 'init_at': init_at, 'end_at': datetime.now()})
        print(err)


async def get_fulfillment(billing_api, session, user_id, key, group, document_type, operation):
    try:
        if operation:
            async with aiohttp.ClientSession() as client_session:
                api_call = await billing_api.billing_fulfillment(client_session, key, group, document_type)
                
                if isinstance(api_call, dict):
                    offset = 0
                    total = api_call['total']
                    limit = api_call['limit']
                    max_pages = ceil(total / limit)

                    tasks = []
                    for page in range(0, max_pages):
                        tasks.append(asyncio.create_task(billing_api.billing_fulfillment(client_session, key, group, document_type, offset)))
                        offset += limit

                    results = await asyncio.gather(*tasks)
                    for result in results:
                        for info in result['results']:
                            
                            if operation == 'create':
                                await add_fulfillment(session, user_id, key, group, document_type, info)

                            if operation == 'update':
                                await update_fulfillment(session, user_id, info)

                    # logger.info(f'Tarefa Concluída - {count} novos registros', extra={'user_id': user_id, 'body': None, 'init_at': init_at, 'end_at': datetime.now()})
                
                else:
                    # logger.warning('Falha na solicitação', extra={'user_id': user_id, 'body': f'status: {api_call}', 'init_at': init_at, 'end_at': datetime.now()})
                    print(api_call)

    except Exception as err:
        #logger.error('Falha na execução', extra={'user_id': user_id, 'body': err, 'init_at': init_at, 'end_at': datetime.now()})
        print(err)


async def get_billings(billing_api, user_id):
    for group in groups:
        for document_type in document_types:
            try:
                init_at = datetime.now()
                count_add = 0
                count_update = 0

                async with async_session as session:
                    async with aiohttp.ClientSession() as client_session:
                        api_call = await billing_api.billing_periods(client_session, group, document_type)
                        if isinstance(api_call, dict):
                            offset = 0
                            total = api_call['total']
                            limit = api_call['limit']
                            max_pages = ceil(total / limit)

                            tasks = []
                            for page in range(0, max_pages):
                                tasks.append(asyncio.create_task(billing_api.billing_periods(client_session, group, document_type, offset)))
                                offset += limit

                            results = await asyncio.gather(*tasks)
                            for result in results:
                                for billing in result['results']:
                                    key = str(billing['key'])
                                    operation = await create_or_update_periods(session, user_id, group, document_type, billing)
                                    
                                    await get_documets(billing_api, session, user_id, key, group, document_type,operation)
                                    # await get_summary(billing_api, session, user_id, key, group, document_type, operation)
                                    await get_details(billing_api, session, user_id, key, group, document_type, operation)
                                    # await get_insurtech(billing_api, session, user_id, key, group, document_type, operation)
                                    # await get_fulfillment(billing_api, session, user_id, key, group, document_type, operation)

                                    if operation == 'create':
                                        count_add += 1

                                    if operation =='update':
                                        count_update += 1

                            await session.commit()
                            logger.info(f'Tarefa finalizada({group} / {document_type}): Total de {count_add} novos registros e {count_update} registros atualizados', extra={'user_id': user_id, 'body': None, 'init_at': init_at, 'end_at': datetime.now()})
                        else:
                            logger.warning('Falha na solicitação --', extra={'user_id': user_id, 'body': f'status: {api_call}', 'init_at': init_at, 'end_at': datetime.now()})
                            return api_call

            except Exception as err:
                logger.error('Falha na execução', extra={'user_id': user_id, 'body': err, 'init_at': init_at, 'end_at': datetime.now()})
            