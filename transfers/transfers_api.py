from fastapi import APIRouter

from datetime import datetime

from database.transferservice import create_transaction_db, cancel_transfer_db, get_card_transaction_db

from transfers import CreateTransferValidator, CancelTransferValidator

transfer_router = APIRouter(prefix='/transaction', tags=['Работа с платежами'])


# Запрос на создания транзакций
@transfer_router.post('/create')
async def add_new_transaction(data: CreateTransferValidator):
    transaction_data = data.model_dump()
    result = create_transaction_db(**transaction_data)

    return {'message': result}


# Запрос на отмену транзакции
@transfer_router.post('/cancel')
async def cancel_transaction(data: CancelTransferValidator):
    cancel_data = data.model_dump()
    result = cancel_transfer_db(**cancel_data)
    return {'message': result}


# Запрос на получения всех транзакций определенного карты
@transfer_router.get('/monitoring')
async def get_card_monitoring(card_id: int):
    result = get_card_transaction_db(card_from_id=card_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'No card'}
